from fastapi import FastAPI
from core.asset.router import router as asset_router
from core.evidence.router import router as evidence_router

app = FastAPI(
    title="A-ZION API",
    version="0.1.0",
    description="Institutional Investment Intelligence Operating System",
)

app.include_router(asset_router, prefix="/assets", tags=["Assets"])
app.include_router(evidence_router, prefix="/evidence", tags=["Evidence"])


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "system": "A-ZION", "version": "0.1.0"}
