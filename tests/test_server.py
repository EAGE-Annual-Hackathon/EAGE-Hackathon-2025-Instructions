import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pathlib import Path

from starlette.testclient import TestClient

from hello_world_mcp.server import fetch_F3, hello_world, mcp, show_mona_lisa


def test_hello_world():
    assert hello_world("Alice") == "Hello World, Alice!"


def test_show_mona_lisa():
    image = show_mona_lisa()
    assert image.path == Path("/root/hello_world_mcp/mona_lisa.JPG")


def test_fetch_F3(monkeypatch):
    local_sgy = (
        Path(__file__).resolve().parents[1] / "hello_world_mcp" / "F3_8-bit_int.sgy"
    )
    
    
    def cube_wrapper(path):
        assert path == "/root/hello_world_mcp/F3_8-bit_int.sgy"
        import segyio.tools as tools

        return tools.cube(str(local_sgy))

    monkeypatch.setattr("hello_world_mcp.server.cube", cube_wrapper)
    image = fetch_F3()
    try:
        assert image.path.is_file()
        assert image.path.suffix == ".jpg"
    finally:
        image.path.unlink(missing_ok=True)


def test_health_check_route():
    client = TestClient(mcp.http_app())
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
