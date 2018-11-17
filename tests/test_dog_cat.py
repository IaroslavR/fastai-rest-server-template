import json
from pathlib import Path
from urllib.parse import urlparse

import pytest
from fastai.vision import open_image

from api import APP_PATH
from api.dog_cat import Predictor

samples_path = Path(APP_PATH).joinpath("tests", "assertions")


def get_sample(*args, **_kwargs):
    fname = samples_path.joinpath(Path(urlparse(args[1]).path).name)
    return open_image(fname)


@pytest.fixture
def mock_get_by_url(monkeypatch):
    """here we replace result of web request to content of local file"""
    monkeypatch.setattr(
        Predictor, "get_by_url", lambda *args, **kwargs: get_sample(*args, **kwargs)
    )


def test_dog_cat(mock_get_by_url, client):
    payload = json.dumps(
        [
            {
                "uri": "https://www.publicdomainpictures.net/pictures/170000/velka/cat-on-the-white-14629665801Rd.jpg"
            },
            {"uri": "https://no.image"},
        ]
    )
    res = client.post("/dog_cat", data=payload, content_type="application/json")
    assert res.status_code == 200
    assert "cats" == json.loads(res.json)[0]["result"]
    assert "processing error" == json.loads(res.json)[1]["result"]
