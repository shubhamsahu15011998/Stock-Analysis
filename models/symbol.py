from datetime import datetime

from sqlalchemy import Column, String, Integer, UniqueConstraint, TIMESTAMP

from models import Base


class Symbol(Base):
    __tablename__ = 'symbols'

    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now())
    scrip_code = Column(String(50), nullable=False)
    trading_symbol = Column(String(50), primary_key=True, nullable=False)
    description = Column(String(200))
    instrument_type = Column(Integer)

    # Add unique constraint on trading_symbol
    __table_args__ = (UniqueConstraint('trading_symbol', name='unique_trading_symbol'),)

    def __repr__(self):
        return f"<Symbol(trading_symbol='{self.trading_symbol}')>"

    @classmethod
    def get_primary_key(cls):
        return Symbol.__table__.primary_key.columns.keys()
