from .. import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Date, Float
from datetime import date


class GME(Base):
    __tablename__ = "GME"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement='auto')
    date: Mapped[date] = mapped_column(Date, unique=True, index=True)
    open: Mapped[float] = mapped_column(Float)
    high: Mapped[float] = mapped_column(Float)
    low: Mapped[float] = mapped_column(Float)
    close: Mapped[float] = mapped_column(Float)
    volume: Mapped[float] = mapped_column(Float)
    SMA: Mapped[float] = mapped_column(Float)
    RSI: Mapped[float] = mapped_column(Float)
    OBV: Mapped[float] = mapped_column(Float)
    
    def __repr__(self) -> str:
        return f"GME(id={self.id!r}, date={self.date!r}, open={self.open!r}, high={self.high!r}, low={self.low!r}, close={self.close!r}, volume={self.volume!r}, SMA={self.SMA!r}, RSI={self.RSI!r}, OBV={self.OBV!r})"
