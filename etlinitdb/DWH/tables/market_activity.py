from .. import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Date, Float, String
import datetime
from sqlalchemy import UniqueConstraint


from sqlalchemy import UniqueConstraint

class MarketActivity(Base):
    __tablename__ = "market_activity"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto")
    name: Mapped[str] = mapped_column(String(50))
    share: Mapped[str] = mapped_column(String(50))
    Date: Mapped[date] = mapped_column(Date, index=True)
    Open: Mapped[float] = mapped_column(Float)
    High: Mapped[float] = mapped_column(Float)
    Low: Mapped[float] = mapped_column(Float)
    Close: Mapped[float] = mapped_column(Float)
    Volume: Mapped[float] = mapped_column(Float)
    SMA: Mapped[float] = mapped_column(Float)
    RSI: Mapped[float] = mapped_column(Float)
    OBV: Mapped[float] = mapped_column(Float)
    MACD: Mapped[float] = mapped_column(Float)
    MACD_SIGNAL: Mapped[float] = mapped_column(Float)
    

    __table_args__ = (UniqueConstraint('name', 'share', 'Date', name='_name_share_date_uc'),)

    def __repr__(self):
        return f"<MarketActivity(name={self.name}, share={self.share}, Date={self.Date}, Open={self.Open}, High={self.High}, Low={self.Low}, Close={self.Close}, Volume={self.Volume}, SMA={self.SMA}, RSI={self.RSI}, OBV={self.OBV}, MACD={self.MACD}, MACD_SIGNAL={self.MACD_SIGNAL})>"
