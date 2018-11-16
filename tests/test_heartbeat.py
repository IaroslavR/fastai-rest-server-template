import json

from api import __version__


def test_heartbeat(client):
    res = client.get("/")
    assert res.status_code == 200
    assert json.loads(res.json) == {"version": __version__}
