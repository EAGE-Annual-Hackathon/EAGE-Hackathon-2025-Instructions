# EAGE-Hackathon-2025-Instructions
Welcome to the instructions for the EAGE Hackathon hosted at the Annual 2025 in Toulouse, France

## Task
Each team will create tools that can help geoscientists in their daily work which an LLM can leverage. The tool should be able to interact at least with the Github Copilot and use the MCP (Model Context Protocol) to communicate with other tools.

## What is the MCP?
The MCP (Model-Context Protocol) is a protocol that allows LLM Clients such as Github Copilot to communicate with servers providing tools and context to the LLM. 

## Evaluation Criteria
- **Creativity**: How creative is the tool? Does it solve a problem that geoscientists face?
- **Business Value**: Does the tool have a business value? Can it be used in a real-world scenario?
- **Technical Implementation**: How well is the tool implemented? Is it easy to use and understand?
- **Presentation**: How well is the tool presented? Is it easy to understand and use?
- **Teamwork**: How well did the team work together? Did everyone contribute to the project?
- **Documentation**: Is the tool well documented? Is it easy to understand how to use it?
- **Code Quality**: Is the code well written? Is it easy to understand and maintain?

## Getting Setup (do this before the hackathon ideally): 

Please install Microsoft Visual Studio Code Insiders (we need this for the latest MCP features):
- https://code.visualstudio.com/insiders/

Make sure to install the `uv` package manager (think Anaconda but much faster): 
- https://docs.astral.sh/uv/#installation

If possible also install Docker Desktop or Podman: 
- https://www.docker.com/products/docker-desktop/
- https://podman.io/

## Installing the MCP servers (command line)
To install the MCP server you first need to install the `uv` command line tool. This is a command line tool that allows you to run the MCP servers locally.

### Install `uv` command line tool (Skip if already installed)
The `uv` command line tool is available for Windows, Linux and MacOS.
```bash
# Install uv (windows)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install uv (linux, wsl)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Running the MCP server
After installation start the server with the following: 
```bash
uv run hello_world_mcp/server.py
```

## Installing the MCP servers (docker)

To run the MCP servers from command line: 
```bash
docker compose up
```

## Integrating the MCP Servers
Navigate to `.vscode/mcp.json` once the server is running and click on `Start` for the HelloWorldMCP to start the MCP server. 

## Interacting with the MCP Server

### Github Copilot
Go to your Github Copilot window, activate `Ask`-mode and add the tool into your context, or when in `Agent`-mode add the tool through the MCP configuration in the lower left corner. 

## Deploying the MCP servers to Modal (Optional)
The MCP servers can also be deployed to Modal. This allows you to run the servers in the cloud and access them from anywhere.
To deploy the MCP servers you need to have the `uv` command line tool installed.
```bash
uv run modal deploy modal_mcp_servers.py
```
This will deploy the MCP servers to Modal. You can then access the servers from your local machine.

## Development setup

To run the test suite and work on the project, create a virtual environment and install the development dependencies managed by `uv`.

```bash
uv venv .venv            # create a virtual environment in `.venv`
source .venv/bin/activate
uv sync --group dev      # install packages from the `dev` dependency group
```

Once the packages are installed you can run the tests:

```bash
.venv/bin/pytest -q
```
