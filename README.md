# EAGE-Hackathon-2025-Instructions
Welcome to the instructions for the EAGE Hackathon hosted at the Annual 2025 in Toulouse, France

## Task
Each team will create tools that can help geoscientists in their daily work which an LLM can leverage. The tool should be able to interact at least with the Github Copilot and use the MCP (Multi-Context Protocol) to communicate with other tools.

## What is the MCP?
The MCP (Multi-Context Protocol) is a protocol that allows different tools to communicate with each other. It is designed to be used with LLMs and allows for the creation of tools that can be used in conjunction with LLMs. The MCP is a simple JSON-based protocol that allows for the exchange of data between different tools.

## Evaluation Criteria
- **Creativity**: How creative is the tool? Does it solve a problem that geoscientists face?
- **Business Value**: Does the tool have a business value? Can it be used in a real-world scenario?
- **Technical Implementation**: How well is the tool implemented? Is it easy to use and understand?
- **Presentation**: How well is the tool presented? Is it easy to understand and use?
- **Teamwork**: How well did the team work together? Did everyone contribute to the project?
- **Documentation**: Is the tool well documented? Is it easy to understand how to use it?
- **Code Quality**: Is the code well written? Is it easy to understand and maintain?

## Installing the MCP servers (command line)
To install the MCP server you first need to install the `uv` command line tool. This is a command line tool that allows you to run the MCP servers locally.

### Install `uv` command line tool
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

## Deploying the MCP servers to Modal
The MCP servers can also be deployed to Modal. This allows you to run the servers in the cloud and access them from anywhere.
To deploy the MCP servers you need to have the `uv` command line tool installed.
```bash
uv run modal deploy modal_mcp_servers.py
```
This will deploy the MCP servers to Modal. You can then access the servers from your local machine.

## Integrating the MCP Servers
Navigate to `.vscode/mcp.json` once the server is running and click on `Start` for the HelloWorldMCP to start the MCP server. 

Go to your Github Copilot window, activate `Ask`-mode and add the tool into your context, or when in `Agent`-mode add the tool through the MCP configuration in the lower left corner. 