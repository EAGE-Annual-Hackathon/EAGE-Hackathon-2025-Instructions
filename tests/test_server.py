from hello_world_mcp.server import hello_world

def test_hello_world():
    assert hello_world('Alice') == "Hello World, Alice!"
