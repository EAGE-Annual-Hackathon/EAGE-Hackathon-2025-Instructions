FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

EXPOSE 9000

#(Needed to write logs in pod)
ENV PYTHONUNBUFFERED=1
#(Needed to write logs in pod)
ENV PYTHONIOENCODING=UTF-8

# Add user group to be able to write to file when deployed in NITRO platform (related to Network security)
# https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user`
RUN groupadd --gid 1000 appuser \
   && useradd --uid 1000 --gid 1000 -m appuser

WORKDIR /hello_world_mcp

COPY --chown=appuser:appuser uv.lock pyproject.toml /hello_world_mcp/

COPY --chown=appuser:appuser ./hello_world_mcp/pyproject.toml /hello_world_mcp/pyproject.toml

RUN uv sync \
   --frozen \
   --compile-bytecode \
   --no-install-workspace \
   --no-install-project \
   --no-dev \
   --package="hello_world_mcp"


COPY --chown=appuser:appuser ./hello_world_mcp /hello_world_mcp/hello_world_mcp

RUN uv sync \
   --frozen \
   --package=hello_world_mcp

ENV PATH="/hello_world_mcp/.venv/bin:$PATH"

# Give user group write acces to /app (related to Network security)
RUN chown -R appuser:appuser /hello_world_mcp
USER appuser

WORKDIR /hello_world_mcp/hello_world_mcp/

ENTRYPOINT ["uv", "run", "server.py"]
