from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.climate_environmental_monitor.models import AgenticClimateEnvironmentalMonitorSession, AgenticClimateEnvironmentalMonitorItem
from app.domain.climate_environmental_monitor.schemas import AgenticClimateEnvironmentalMonitorSessionCreate, AgenticClimateEnvironmentalMonitorItemCreate

class AgenticClimateEnvironmentalMonitorService:
    @staticmethod
    def create_session(db: Session, data: AgenticClimateEnvironmentalMonitorSessionCreate) -> AgenticClimateEnvironmentalMonitorSession:
        db_obj = AgenticClimateEnvironmentalMonitorSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticClimateEnvironmentalMonitorSession:
        return db.query(AgenticClimateEnvironmentalMonitorSession).filter(AgenticClimateEnvironmentalMonitorSession.id == session_id).first()
