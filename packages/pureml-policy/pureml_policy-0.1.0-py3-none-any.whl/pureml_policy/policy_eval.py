from pydantic import BaseModel
from pureml.predictor.predictor import BasePredictor
from pureml.components import dataset
from typing import Any
from importlib import import_module
from rich import print
import requests
from pureml_evaluate.evaluators.evaluator import eval as eval_fn
from pureml.cli.auth import get_auth_headers
from pureml.components import get_org_id
from .grade import Grader


class EvalHelper(BaseModel):  # To pass the requirements to eval in pureml_evaluate
    label_model: str
    label_dataset: str
    policy: dict
    predictor: BasePredictor = None
    predictor_path: str = "predict.py"
    dataset: Any = None

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True

    def load_dataset(self):
        self.dataset = dataset.fetch(self.label_dataset)
        print("[bold green] Succesfully fetched the dataset")

    def load_predictor(self):
        module_path = self.predictor_path.replace(".py", "")
        module_import = import_module(module_path)

        predictor_class = getattr(module_import, "Predictor")

        self.predictor = predictor_class()
        print("[bold green] Succesfully fetched the predictor")

    def load_model(self):
        self.predictor.load_models()
        print("[bold green] Succesfully fetched the model")

    def load_policy(self):
        return list(self.policy.keys())

    def load(self):
        self.load_dataset()
        self.load_predictor()
        self.load_model()
        self.load_policy()

    def get_y_pred(self):
        return self.predictor.predict(self.dataset["x_test"])

    def get_y_true(self):
        return self.dataset["y_test"]

    def get_sensitive_features(self):
        print(f"Dataset Keys: {self.dataset.keys()}")
        if 'sensitive_features' in self.dataset.keys():
            print(
                f"Data in sensitive_features: {self.dataset['sensitive_features']}")
            return self.dataset['sensitive_features']
        else:
            return None

    def evaluate(self):
        y_pred = self.get_y_pred()
        y_true = self.get_y_true()
        sensitive_features = self.get_sensitive_features()
        metrics = self.load_policy()
        grader = Grader(references=y_true, predictions=y_pred,
                        sensitive_features=sensitive_features, policy=self.policy, metrics=metrics)

        result = grader.compute()
        labelmodel = self.label_model.split(':')
        print(labelmodel, self.label_model)
        version = labelmodel[1]
        model = labelmodel[0]
        # print(f"version: {version}")
        # print(f"model: {model}")
        formatted_result = {
            "model": f"{model}",
            "version": f"{version}",
            "result": [result]
        }
        return formatted_result


def eval(label_model: str, label_dataset: str, policy: dict):
    evaluator = EvalHelper(label_model=label_model,
                           label_dataset=label_dataset, policy=policy)

    evaluator.load()
    result = evaluator.evaluate()

    return result
