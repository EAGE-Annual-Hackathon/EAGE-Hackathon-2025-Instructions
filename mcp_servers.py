import modal

app = modal.App("eage-annual-20250mcp-server")

uv_image = modal.Image.from_registry("ghcr.io/astral-sh/uv:python3.12-bookworm-slim").pip_install(
    "fastmcp>=0.2.3"
).add_local_python_source("hello_world_mcp")


@app.function(image=uv_image)
@modal.concurrent(max_inputs=100)
@modal.asgi_app()
def mcp_server():
    from hello_world_mcp.server import mcp as mcp_hello_world

    # For legacy SSE transport (deprecated)
    sse_app = mcp_hello_world.http_app(transport="sse")
    return sse_app