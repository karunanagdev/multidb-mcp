from mcp.server.fastmcp import FastMCP
from services.port_service import PortService

mcp = FastMCP("Maritime MCP Server")
port_service = PortService()


@mcp.tool()
def show_ports():
    return port_service.show_ports()


if __name__ == "__main__":
    mcp.run()