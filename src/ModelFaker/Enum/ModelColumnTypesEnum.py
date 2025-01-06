from enum import Enum

from sqlalchemy import (
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    Enum as SQLAlchemyEnum,
    Date,
    Float
)
from sqlalchemy.orm import relationship


class ModelColumnTypesEnum(Enum):
    """Enum class for the model column types"""

    STRING = String

    INTEGER = Integer

    FLOAT = Float

    TEXT = Text

    BOOLEAN = Boolean

    DATETIME = DateTime

    DATE = Date

    ENUM = SQLAlchemyEnum

    RELATIONSHIP = relationship
