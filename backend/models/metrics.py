from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NodeMetric(Base):

    __tablename__ = "node_metrics"

    id = Column(Integer, primary_key=True, index=True)

    node_name = Column(String)

    cpu_usage = Column(Float)

    memory_usage = Column(Float)

    disk_usage = Column(Float)

    timestamp = Column(DateTime)