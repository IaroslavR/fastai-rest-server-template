from pathlib import Path
from urllib.parse import urlparse

import pytest

from api import APP_PATH
from api.dog_cat import ModelLoader

samples_path = Path(APP_PATH).joinpath("tests", "assertions")


def get_sample(*args, **_kwargs):
    fname = samples_path.joinpath(Path(urlparse(args[1]).path).name)
    with open(fname, "rb") as f:
        return f.read()


@pytest.fixture
def mock_get_by_url(monkeypatch):
    monkeypatch.setattr(ModelLoader, "get_by_url", lambda *args, **kwargs: get_sample(*args, **kwargs))


def test_dog_cat(mock_get_by_url):
    url = "https://www.publicdomainpictures.net/pictures/170000/velka/cat-on-the-white-14629665801Rd.jpg"
    processor = ModelLoader()
    processor.get_data(url)
    assert processor.data == get_sample(None, url)
