import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hello_world_mcp.server import hello_world


def test_hello_world():
    assert hello_world("Alice") == "Hello World, Alice!"
