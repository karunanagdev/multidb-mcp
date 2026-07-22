# AI Data Assistant - Architecture

## Overview

This project is an AI-powered data assistant using Model Context Protocol (MCP).

The goal is to provide a common AI interface to interact with multiple data sources including databases and files.

## Current Architecture
User
|
MCP Client
|
MCP Server
|
Service Layer
|
Database Layer
|
SQLite


## Current Components

### MCP Server

Technology:
- FastMCP

Responsibilities:
- Expose tools
- Handle MCP communication

### Service Layer

Responsibilities:
- Business logic
- Validation
- Transaction handling

### Database Layer

Responsibilities:
- Database connectivity
- Query execution
- Error handling


## Future Architecture
             AI Client

                |

            MCP Server

                |

          Service Layer

                |

    -----------------------

    |                     |
    Repository ML Service

    |                     |

Data Sources Prediction Models

    |

SQLite/PostgreSQL/
SQL Server/CSV/Excel/JSON


## Future Capabilities

- Multiple database support
- File analytics
- Machine learning predictions
- Log analysis
- Generic data assistant