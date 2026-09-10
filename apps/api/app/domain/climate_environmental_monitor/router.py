from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.climate_environmental_monitor.schemas import AgenticClimateEnvironmentalMonitorSessionCreate, AgenticClimateEnvironmentalMonitorSessionResponse
from app.domain.climate_environmental_monitor.service import AgenticClimateEnvironmentalMonitorService

router = APIRouter(prefix="/api/v1/climate_environmental_monitor", tags=["Agentic Climate Environmental Monitor Domain"])

@router.post("/sessions", response_model=AgenticClimateEnvironmentalMonitorSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticClimateEnvironmentalMonitorSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Climate Environmental Monitor.
    """
    return AgenticClimateEnvironmentalMonitorService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticClimateEnvironmentalMonitorSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticClimateEnvironmentalMonitorService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
