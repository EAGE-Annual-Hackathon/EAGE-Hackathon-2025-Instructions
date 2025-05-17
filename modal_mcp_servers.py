"""
Modal server definitions for the EAGE Hackathon 2025 project.

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

import modal

app = modal.App("eage-annual-2025-mcp-server")



uv_image = modal.Image.from_registry("ghcr.io/astral-sh/uv:python3.12-bookworm-slim").pip_install(
    "fastmcp>=0.2.3",
    "matplotlib>=3.10.3",
    "segyio>=1.9.13",
).add_local_python_source("hello_world_mcp").add_local_file(
    "./hello_world_mcp/mona_lisa.JPG", "/root/hello_world_mcp/mona_lisa.JPG"
).add_local_file("./hello_world_mcp/F3_8-bit_int.sgy", "/root/hello_world_mcp/F3_8-bit_int.sgy")


@app.function(image=uv_image)
@modal.concurrent(max_inputs=100)
@modal.asgi_app()
def mcp_server():
    from hello_world_mcp.server import mcp as mcp_hello_world

    # For legacy SSE transport (deprecated)
    sse_app = mcp_hello_world.http_app(transport="sse")
    return sse_app