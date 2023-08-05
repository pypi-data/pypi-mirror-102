import os
import json
import joblib
import optuna
from kdmt.file import create_dir
from optuna.pruners import SuccessiveHalvingPruner

class OptunaTuner:
    def __init__(
        self,
        results_path,
        eval_metric,
        time_budget=3600,
        init_params={},
        verbose=True,
        n_jobs=-1,
        random_state=42,
        direction="maximize"
    ):


        self.study_dir = os.path.join(results_path, "optimizer")
        create_dir(self.study_dir)
        self.tuning_fname = os.path.join(self.study_dir, "optuna.json")
        self.tuning = init_params
        self.eval_metric = eval_metric

        self.direction = direction
        self.n_warmup_steps = (
            500  # set large enough to give small learning rates a chance
        )
        self.time_budget = time_budget
        self.verbose = verbose
#        self.ml_task = ml_task
        self.n_jobs = n_jobs
        self.random_state = random_state


        self.load()
        if not self.verbose:
            optuna.logging.set_verbosity(optuna.logging.CRITICAL)


    def optimize2(
        self,
        objective,
        learner_params,
    ):
        algorithm=learner_params["fixed"]["name"]
        defaults=learner_params["fixed"]['default-params']

        if self.verbose:
            print(
                f"Optuna optimizes {algorithm} with time budget {self.time_budget} seconds "
                f"eval_metric {self.eval_metric} ({self.direction})"
            )

        study = optuna.create_study(
            direction=self.direction,
            sampler=optuna.samplers.TPESampler(seed=self.random_state),
            pruner=SuccessiveHalvingPruner(),
        )
        study.enqueue_trial(defaults)
        study.optimize(objective, n_trials=10, timeout=self.time_budget)

        joblib.dump(study, os.path.join(self.study_dir, str(algorithm) + ".joblib"))

        best = study.best_params
        best["metric"] = objective.eval_metric_name
        best["feature_pre_filter"] = False
        best["seed"] = objective.seed


        self.save()

        return self.update_learner_params(learner_params, best)

    def optimize(self, objective, learner_params,
    ):
        algorithm="pipeline"
        defaults=learner_params

        if self.verbose:
            print(
                f"Optuna optimizes {algorithm} with time budget {self.time_budget} seconds "
                f"eval_metric {self.eval_metric} ({self.direction})"
            )

        study = optuna.create_study(
            direction=self.direction,
            sampler=optuna.samplers.TPESampler(seed=self.random_state),
            pruner=SuccessiveHalvingPruner(),
        )
        study.enqueue_trial(defaults)
        study.optimize(objective, n_trials=5, timeout=self.time_budget)

        joblib.dump(study, os.path.join(self.study_dir, str(algorithm) + ".joblib"))

        best = study.best_params


        self.save()

        return self.update_learner_params(learner_params, best)

    def update_learner_params(self, learner_params, best):
        for k, v in best.items():
            key=k.split('.')
            param=learner_params
            for sub_key in key:
                param=param[sub_key]
            param["value"]=v
        return learner_params

    def save(self):
        with open(self.tuning_fname, "w") as fout:
            fout.write(json.dumps(self.tuning, indent=4))

    def load(self):
        if os.path.exists(self.tuning_fname):
            params = json.loads(open(self.tuning_fname).read())
            for k, v in params.items():
                self.tuning[k] = v
