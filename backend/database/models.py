from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from datetime import datetime

class SportRecord(Base):
    __tablename__ = "sport_records"
    id = Column(Integer, primary_key=True)
    sport = Column(String)
    match = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    value_score = Column(Float)
    bias = Column(String)
    odds = Column(Float)
    probability = Column(Float)
    form = Column(String)  # Új mező a csapat formához
    injuries = Column(String)  # Új mező a sérülésekhez

class MarketRecord(Base):
    __tablename__ = "market_records"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    close = Column(Float)
    volatility = Column(Float)
    trend = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    sentiment = Column(Float)  # Új mező a sentiment analízishez

class FeedbackRecord(Base):
    __tablename__ = "feedback_records"
    id = Column(Integer, primary_key=True)
    system = Column(String)
    accuracy = Column(Float)
    roi = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class ReportLog(Base):
    __tablename__ = "report_logs"
    id = Column(Integer, primary_key=True)
    report_date = Column(DateTime, default=datetime.utcnow)
    accuracy = Column(Float)
    value_bias = Column(Float)
    roi = Column(Float)
    meta_comment = Column(String)
    json_data = Column(JSON)
    emailed = Column(Boolean, default=False)
