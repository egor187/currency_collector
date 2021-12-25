from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float


Base = declarative_base()


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    code = Column(String(10))

    currency_data = relationship("CurrencyData", back_populates="currency")

    def __repr__(self):
        return f"{self.name} -- {self.code}"


class CurrencyData(Base):
    __tablename__ = "currency_data"

    id = Column(Integer, primary_key=True)
    currency_id = Column(Integer, ForeignKey("currency.id", ondelete="CASCADE"))
    date = Column(Date)
    value = Column(Float)

    currency = relationship("Currency", back_populates="currency_data")


