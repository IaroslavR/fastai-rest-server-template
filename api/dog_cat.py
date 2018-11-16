from pathlib import Path

import attr
import requests


from urllib.parse import urlparse
from api import APP_PATH

path_to_model = Path(APP_PATH).joinpath("models/lesson1-rxt50.h5")
download_path = Path(APP_PATH).joinpath("downloads")


@attr.s
class ModelLoader:
    custom_model_path: str = attr.ib(default=path_to_model)
    download_path: str = attr.ib(default=download_path)
    model = attr.ib()
    data = attr.ib(default=None)
    data_file = attr.ib(default=None)

    @model.default
    def init_model(self):
        # model = resnet50()
        # state = torch.load(self.custom_model_path)
        # model.load_state_dict(state)
        # model.eval()
        # return model
        pass

    @staticmethod
    def get_by_url(url):
        return requests.get(url).content

    def get_data(self, url: str, save=True) -> None:
        self.data = self.get_by_url(url)
        if save:
            self.data_file = Path(self.download_path).joinpath(
                Path(urlparse(url).path).name
            )
            with open(self.data_file, "wb") as f:
                f.write(self.data)

    def classify(self, url):
        self.get_data(url)


model = ModelLoader()


def predict(*args, **kwargs):
    #
    # normalize = torchvision.transforms.Normalize(
    #     mean=[0.485, 0.456, 0.406],
    #     std=[0.229, 0.224, 0.225]
    # )
    # preprocess = torchvision.transforms.Compose([
    #     torchvision.transforms.Scale(256),
    #     torchvision.transforms.CenterCrop(224),
    #     torchvision.transforms.ToTensor(),
    #     normalize
    # ])
    #
    # img_tensor = preprocess(img).unsqueeze_(0)
    # img_variable = Variable(img_tensor.cuda())
    #
    # log_probs = torch_model(img_variable)
    # preds = np.argmax(log_probs.cpu().data.numpy(), axis=1)
    pass
