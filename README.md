# A-ZION Platform

A-ZION is an institutional investment intelligence operating system.

## Current Build

IE-01 Platform Skeleton

## Core Principles

- Asset-first architecture
- Evidence before conclusions
- ANR is the numerical source of truth
- Every action is auditable
- Engines are replaceable
- Governance cannot be bypassed

## Stack

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Redis
- Neo4j
- Qdrant
- Pytest
- Docker

## Run Dev API

```bash
cd a-zion
pip install -r requirements.txt
uvicorn apps.api.main:app --reload
```
