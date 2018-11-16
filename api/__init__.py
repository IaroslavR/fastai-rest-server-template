import json
import os
from pathlib import Path

import connexion

from api.config import config

APP_PATH = Path(os.path.realpath(__file__)).parent.parent
MODEL_PATH = os.environ.get(
    "MODEL_PATH", Path(APP_PATH).joinpath("model/lession1-resnet34-2")
)
DOWNLOAD_PATH = os.environ.get("DOWNLOAD_PATH", Path(APP_PATH).joinpath("downloads"))

__version__ = "0.1"


def heartbeat():
    return json.dumps({"version": __version__})


def create_app():
    app = connexion.App(__name__)
    app.app.config.from_object(config[os.environ.get("APP_MODE", "development")])
    app.add_api("swagger.yaml")
    return app.app


app = create_app()
