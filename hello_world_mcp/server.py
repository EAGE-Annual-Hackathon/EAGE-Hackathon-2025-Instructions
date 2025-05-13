from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP(name="HelloWorldMCP",
    instructions="""
        This server provides basic functionalities to demonstrate MCP!
        """)

@mcp.tool()
def hello_world(name: str) -> str:
    """Greet a user Hellow World!"""
    return f"Hello World, {name}!"

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "healthy"})

if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=9000,
        log_level="debug",
        path="/hello_world_mcp"
       )