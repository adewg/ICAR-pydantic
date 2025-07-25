from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from . import enums, types


class UnitCode(Enum):
    SEC = "SEC"
    MIN = "MIN"


class SupportedMessage(BaseModel):
    messages: Optional[enums.IcarMessageType] = None


class PlanOrActual(Enum):
    Plan = "Plan"
    Actual = "Actual"


class Type(Enum):
    Point = "Point"


class Geometry1(BaseModel):
    type: Type
    coordinates: List[float] = Field(..., min_items=2)
    bbox: Optional[List[float]] = Field(None, min_items=4)


class Type1(Enum):
    LineString = "LineString"


class Coordinate(BaseModel):
    __root__: List[float]


class Geometry2(BaseModel):
    type: Type1
    coordinates: List[Coordinate] = Field(..., min_items=2)
    bbox: Optional[List[float]] = Field(None, min_items=4)


class Type2(Enum):
    Polygon = "Polygon"


class Geometry3(BaseModel):
    type: Type2
    coordinates: List[List[Coordinate]]
    bbox: Optional[List[float]] = Field(None, min_items=4)


class Type3(Enum):
    MultiPoint = "MultiPoint"


class Geometry4(BaseModel):
    type: Type3
    coordinates: List[List[float]]
    bbox: Optional[List[float]] = Field(None, min_items=4)


class Type4(Enum):
    MultiLineString = "MultiLineString"


class Geometry5(BaseModel):
    type: Type4
    coordinates: List[List[Coordinate]]
    bbox: Optional[List[float]] = Field(None, min_items=4)


class Type5(Enum):
    MultiPolygon = "MultiPolygon"


class Geometry6(BaseModel):
    type: Type5
    coordinates: List[List[List[Coordinate]]]
    bbox: Optional[List[float]] = Field(None, min_items=4)


class Geometry(BaseModel):
    __root__: Union[
        Geometry1, Geometry2, Geometry3, Geometry4, Geometry5, Geometry6
    ] = Field(..., title="GeoJSON Geometry")


class UnitCode2(Enum):
    KGM = "KGM"


class IcarQuarterId(Enum):
    LF = "LF"
    RF = "RF"
    LR = "LR"
    RR = "RR"


class UnitCode3(Enum):
    KGM = "KGM"
    LBR = "LBR"


class Fraction(BaseModel):
    breed: Optional[types.IcarBreedIdentifierType] = Field(
        None, description="The breed for this breed fraction using a scheme and id."
    )
    fraction: Optional[float] = Field(
        None, description="The proportion of the denominator that this breed comprises."
    )


class HeatReportScrSenseTime(BaseModel):
    breedingWindow: Optional[int] = Field(None, description="Number of hours to AI.")
    heatIndex: Optional[int] = Field(
        None, description="Gives an indication of the certainty of the heat indication."
    )


class HeatReportNedapCowControl(BaseModel):
    expirationDateTime: Optional[types.IcarDateTimeType] = Field(
        None,
        description="RFC3339 UTC date/time when the heat will end (see https://ijmacd.github.io/rfc3339-iso8601/ for format guidance).",
    )
    heatChance: Optional[int] = Field(
        None, description="Gives an indication of the certainty of the heat indication."
    )


class VisualDetection(BaseModel):
    heatSigns: Optional[List[enums.IcarReproHeatSignType]] = None
    heatIntensity: Optional[enums.IcarReproHeatIntensityType] = None
