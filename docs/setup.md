# Setup Guide

## Prerequisites

Required:

- Python 3.13+
- Node.js (for MCP Inspector testing)
- Git

## Clone Repository
git clone <repository-url>

## Create Virtual Environment

Windows:

python -m venv .venv

Activate:


.venv\Scripts\activate



## Install Dependencies


pip install -r requirements.txt



## Verify Installation


python --version

fastmcp version



## Run MCP Server


fastmcp run src/mcp_server.py



Expected:


Uvicorn running on http://127.0.0.1:8000



## Inspect MCP Server


fastmcp inspect src/mcp_server.py



Expected:


Tools: 1


## Current Tools

### show_ports

Description:

Returns all ports from the maritime database.