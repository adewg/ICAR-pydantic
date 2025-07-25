from __future__ import annotations

from enum import Enum
from typing import List, Optional

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
