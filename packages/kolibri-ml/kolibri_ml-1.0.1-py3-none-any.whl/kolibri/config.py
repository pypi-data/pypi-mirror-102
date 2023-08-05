import copy

from kolibri.logger import get_logger
from enum import Enum

logger = get_logger(__name__)
from kolibri.backend.sklearn.models import get_model


class TaskType(str, Enum):
    CLASSIFICATION = 'classification'
    LABELING = 'labeling'
    SCORING = 'scoring'
    REGRESSION = 'regression'
    MULTI_TARGET_CLASSIFICATION = 'multi_target_classification'
    MULTI_TARGET_REGRESSION = 'multi_target_regression'
    BINARY_CLASSIFICATION = 'binary_classification'


from kdmt.dict import nested_dict_has_key, nested_dict_get_values


class ParamType(str, Enum):
    INTEGER = 'integer'
    CATEGORICAL = "categorical"
    RANGE = "range"


def component_config_from_pipeline(
        name,
        pipeline,
        defaults=None):
    for c in pipeline:
        if c.get("name") == name:
            return override_defaults(defaults, c)
    else:
        return override_defaults(defaults, {})


class ModelConfig:
    def __init__(self, configuration_values=None):
        """Create a model configuration, optionally overriding
        defaults with a dictionary ``configuration_values``.
        """
        if not configuration_values:
            configuration_values = {}

        if "language" in configuration_values:
            self.language = configuration_values["language"]
        else:
            self.language = "en"

        if "model" in configuration_values:
            configuration_values["model"] = get_model(configuration_values["model"])

        self.override(configuration_values)

        for key, value in self.items():
            setattr(self, key, value)

    def __getitem__(self, key):
        return self.__dict__[key]


    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __getstate__(self):
        return self.as_dict()

    def __setstate__(self, state):
        self.override(state)

    def items(self):
        return list(self.__dict__.items())

    def as_dict(self):
        return dict(list(self.items()))

    def for_component(self, index, defaults=None):
        return component_config_from_pipeline(index, self.pipeline, defaults)

    @property
    def component_names(self):
        if self.pipeline:
            return [c.get("name") for c in self.pipeline]
        else:
            return []

    def override(self, config):
        if config:
            self.__dict__.update(config)


from kdmt.dict import update


def override_defaults(defaults, custom):
    if defaults:
        cfg = copy.deepcopy(defaults)
    else:
        cfg = {}

    if custom:
        if isinstance(custom, dict) or isinstance(custom, ModelConfig):
            cfg = update(cfg, custom)
        else:
            cfg.update(custom)

    return cfg
