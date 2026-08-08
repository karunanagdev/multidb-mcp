from mcp.server.fastmcp import FastMCP
from services.port_service import PortService


mcp = FastMCP("Maritime MCP Server")

port_service = PortService()


@mcp.tool()
def show_ports():
    """Show all maritime ports."""
    return port_service.show_ports()


@mcp.tool()
def search_ports(country: str):
    """Search maritime ports by country."""
    return port_service.search_ports(country)


@mcp.tool()
def get_port_statistics():
    """Get basic statistics about maritime ports."""
    return port_service.get_port_statistics()


if __name__ == "__main__":
    mcp.run()