import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hello_world_mcp.server import hello_world, show_mona_lisa, fetch_F3, mcp
from starlette.testclient import TestClient


def test_hello_world():
    assert hello_world('Alice') == "Hello World, Alice!"


def test_show_mona_lisa():
    image = show_mona_lisa()
    assert str(image.path).endswith("mona_lisa.JPG")


def test_fetch_F3():
    image = fetch_F3()
    assert str(image.path).endswith(".jpg")
    assert os.path.exists(image.path)
    os.remove(image.path)


def test_health_check_route():
    app = mcp.http_app()
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}
