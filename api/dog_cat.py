import io
import json
import time
from pathlib import Path, PosixPath
from urllib.parse import urlparse

import attr
import fastai
import requests
import torch
from fastai.vision import open_image, ImageDataBunch, imagenet_stats, create_cnn

from api import MODEL_PATH, DOWNLOAD_PATH

CLASES = ["cats", "dogs"]
MODEL = fastai.vision.models.resnet34

fastai.defaults.device = torch.device("cpu")


@attr.s
class Predictor:
    model = attr.ib(default=MODEL)
    custom_model_path: str = attr.ib(default=MODEL_PATH)
    classes: list = attr.ib(default=CLASES)
    predictor = attr.ib()
    download_path: str = attr.ib(default=DOWNLOAD_PATH)
    data = attr.ib(default=None)
    data_file: str = attr.ib(default=None)

    @predictor.default
    def init_predictor(self):
        data = ImageDataBunch.single_from_classes("", self.classes, size=224).normalize(
            imagenet_stats
        )
        learn = create_cnn(data, self.model).load(self.custom_model_path)
        return learn

    @staticmethod
    def get_by_url(url):
        return open_image(io.BytesIO(requests.get(url).content))

    @staticmethod
    def get_by_path(path: PosixPath):
        return open_image(path)

    def get_data(self, uri: str, save=True) -> None:
        path = urlparse(uri)
        if path.scheme == "file":
            self.data = self.get_by_path(Path(path.path))
        else:
            self.data = self.get_by_url(uri)
        if save:
            self.data.save(Path(self.download_path).joinpath(Path(path.path).name))

    def classify(self, uri: str) -> dict:
        stime = time.time()
        try:
            self.get_data(uri)
            result, _, _ = self.predictor.predict(self.data)
        except Exception:
            result = "processing error"
        return {"result": result, "source": uri, "processing_time": time.time() - stime}


predictor = Predictor()


def predict(**kwargs):
    response = []
    for item in kwargs["query"]:
        response.append(predictor.classify(item["uri"]))
    return json.dumps(response)
