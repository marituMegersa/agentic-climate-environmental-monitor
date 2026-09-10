from sqlalchemy import Column, String, Boolean, DateTime, Float, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class AgenticClimateEnvironmentalMonitorSession(Base):
    __tablename__ = "climate_environmental_monitor_sessions"

    id = Column(String, primary_key=True, index=True)
    task_prompt = Column(String, nullable=False)
    status = Column(String, default="PENDING", index=True) # PENDING, IN_PROGRESS, COMPLETED, FAILED
    safety_tier = Column(String, default="GREEN") # GREEN, AMBER, RED
    confidence_score = Column(Float, default=0.95)
    metadata_json = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

class AgenticClimateEnvironmentalMonitorItem(Base):
    __tablename__ = "climate_environmental_monitor_items"

    id = Column(String, primary_key=True, index=True)
    session_id = Column(String, ForeignKey("climate_environmental_monitor_sessions.id"))
    item_type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    payload = Column(JSON, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
