from mcp.server.fastmcp import FastMCP
from maritime_service import get_all_ports

mcp = FastMCP("Maritime MCP Server")


@mcp.tool()
def show_ports():
    return get_all_ports().to_string(index=False)


if __name__ == "__main__":
    mcp.run()