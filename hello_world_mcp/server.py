import tempfile

import matplotlib.pyplot as plt
from fastmcp import FastMCP, Image
from segyio.tools import cube
from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP(
    name="HelloWorldMCP",
    instructions="""
        This server provides basic functionalities to demonstrate MCP!
        """,
)


@mcp.tool()
def hello_world(name: str) -> str:
    """Greet a user Hello World!"""
    return f"Hello World, {name}!"


@mcp.tool()
def show_mona_lisa() -> Image:
    """Returns the Mona Lisa image."""
    return Image(path="/root/hello_world_mcp/mona_lisa.JPG")


@mcp.tool()
def fetch_F3() -> Image:
    """Fetches the F3 8-bit int data and returns the first inline as a JPEG image."""
    data = cube("/root/hello_world_mcp/F3_8-bit_int.sgy")
    # data shape: (iline, xline, samples)
    # Select the first inline
    inline = data[0, :, :]
    # Plot and save to a temporary JPEG file
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmpfile:
        plt.figure(figsize=(8, 6))
        plt.imshow(inline.T, aspect="auto", cmap="gray")
        # Title uses the correct filename of the SEG-Y file
        plt.title("First Inline of F3_8-bit_int.sgy")
        plt.xlabel("Xline")
        plt.ylabel("Samples")
        plt.colorbar(label="Amplitude")
        plt.tight_layout()
        plt.savefig(tmpfile.name, format="jpeg")
        plt.close()
        jpeg_path = tmpfile.name
    return Image(path=jpeg_path)


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> JSONResponse:
    return JSONResponse({"status": "healthy"})


if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=9000,
        log_level="debug",
        path="/hello_world_mcp",
    )
