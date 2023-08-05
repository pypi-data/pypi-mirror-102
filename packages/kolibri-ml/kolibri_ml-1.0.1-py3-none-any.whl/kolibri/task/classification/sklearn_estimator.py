import copy

import joblib
from kolibri.config import ModelConfig
from kolibri.backend.base.estimator import BaseEstimator
from kdmt.dict import update
from kolibri.optimizers.optuna.objective import EstimatorObjective
from copy import deepcopy
from kolibri.logger import get_logger
from kdmt.objects import class_from_module_path
logger = get_logger(__name__)

class SklearnEstimator(BaseEstimator):

    name = 'sklearn_classifier'
    hyperparameters= {
        "fixed": {
            "default-params": None
        },

        "tunable": {
        }
    }
    def __init__(self, hyperparameters=None, classifier=None, indexer=None):
        """Construct a new class classifier using the sklearn framework."""
        self.hyperparameters=update(self.hyperparameters, BaseEstimator.hyperparameters)
        super(SklearnEstimator, self).__init__(params=hyperparameters, classifier=classifier, indexer=indexer)

        if isinstance(hyperparameters, ModelConfig):
            self.override_default_parameters(hyperparameters.as_dict())
        elif isinstance(hyperparameters, dict):
            self.hyperparameters = hyperparameters
        else:
            raise ValueError("Expecting dictionnary or model config, got "+str(type(hyperparameters)))

        self.model=self.load_model_from_parameters(self.get_prameter("model"))

    def load_model_from_parameters(self, model_params):
        model_params=deepcopy(model_params)
        model=class_from_module_path(model_params["class"])
        default_params={p:model_params["parameters"][p]["value"] for p in model_params["parameters"]}
        for param, param_val in default_params.items():
            if isinstance(param_val, list):
                for i, p in enumerate(param_val):
                    if isinstance(p, dict):
                        default_params[param][i]=self.load_model_from_parameters(p)
            elif isinstance(param, dict):
                default_params[param] = self.load_model_from_parameters(param_val)

        return model(**default_params)

    def fit(
        self,
        X,
        y,
        sample_weight=None,
        X_validation=None,
        y_validation=None,
        sample_weight_validation=None,
        log_to_file=None,
        max_time=None,
    ):

        self.indexer.build_vocab(None, y)
        y = self.indexer.transform(y)

        super(SklearnEstimator, self).fit(X, y)
        if self.get_prameter('priors-thresolding'):
            self.compute_priors(y)

        if self.sampler:

            Xt, yt = self.sampler.fit_resample(X, y)

            self.model.fit(Xt, yt)
        else:
            self.model.fit(X, y)

        if not self.get_prameter('evaluate-performance') and X_validation is not None and y_validation is not None:
            self.evaluate(X_validation, y_validation)

    def copy(self):
        return copy.deepcopy(self)

    def save(self, model_file_path):
        logger.debug("SklearnAlgorithm save to {0}".format(model_file_path))
        joblib.dump(self.model, model_file_path, compress=True)
        self.model_file_path = model_file_path

    def load_model(self, model_file_path):
        logger.debug("SklearnAlgorithm loading model from {0}".format(model_file_path))
        self.model = joblib.load(model_file_path)
        self.model_file_path = model_file_path

    def is_fitted(self):
        return (
            hasattr(self.model, "n_features_")
            and self.model.n_features_ is not None
            and self.model.n_features_ > 0
        )

    def objective(self, X, y):
        objective=EstimatorObjective(X, y, self.get_prameter("model"), None, eval_metric=self.get_prameter('opt-metric-name'),n_jobs=-1, random_state=42)
        return objective

from kolibri.registry import ModulesRegistry
ModulesRegistry.add_module(SklearnEstimator.name, SklearnEstimator)
