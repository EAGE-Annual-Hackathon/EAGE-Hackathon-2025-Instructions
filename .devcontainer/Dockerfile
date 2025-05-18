FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install git (required for pre-commit)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set environment to output logs immediately
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

WORKDIR /workspace
