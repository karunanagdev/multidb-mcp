SInce mcp inspector issue, tested om python prompt

cd C:\Karuna\Learning\Maritime_AI_Poc

.venv\Scripts\activate

python
import sys
sys.path.append("src")

from services.port_service import PortService

service = PortService()

print(service.show_ports())

from repositories.port_repository import PortRepository

repo = PortRepository()

print(repo.get_all_ports())

from database.database import Database

db = Database()

print(db.query("SELECT * FROM ports"))
exit() or quit()

testing hierarchy
Database
    ↓
Repository
    ↓
Service
    ↓
MCP Tool