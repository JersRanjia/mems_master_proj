from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint, text, BigInteger, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class BaseModel(object):

    __abstract__ = True

    def __str__(self):
        fmt = u'{}.{}({})'
        package = self.__class__.__module__
        class_ = self.__class__.__name__
        attrs = sorted(
            (k, getattr(self, k)) for k in self.__mapper__.columns.keys()
        )
        sattrs = u', '.join(f'{x[0]}={x[1]!r}' for x in attrs)
        return f"{class_}({sattrs})"
        # return fmt.format(package, class_, sattrs)


Base = declarative_base(cls=BaseModel)
metadata = Base.metadata
