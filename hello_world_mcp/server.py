"""
This file is part of the EAGE Hackathon 2025 project.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License in the LICENSE file at the
root of this repository or at
http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from fastmcp import FastMCP, Image
from starlette.requests import Request
from starlette.responses import JSONResponse
from segyio.tools import cube
import matplotlib.pyplot as plt
import tempfile

mcp = FastMCP(name="HelloWorldMCP",
    instructions="""
        This server provides basic functionalities to demonstrate MCP!
        """)

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
        plt.imshow(inline.T, aspect='auto', cmap='gray')
        # Title uses the correct filename of the SEG-Y file
        plt.title("First Inline of F3_8-bit_int.sgy")
        plt.xlabel("Xline")
        plt.ylabel("Samples")
        plt.colorbar(label="Amplitude")
        plt.tight_layout()
        plt.savefig(tmpfile.name, format='jpeg')
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
        path="hello_world_mcp",
       )
