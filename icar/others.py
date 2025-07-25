from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Field

from . import enums, resources, types


class View(BaseModel):
    totalItems: Optional[int] = Field(
        None, description="Provides the number of items in the collection, if known."
    )
    totalPages: Optional[int] = Field(
        None, description="Provides the number of pages in the collection, if known."
    )
    pageSize: Optional[int] = Field(
        None,
        description="If non-zero, specifies the default number of items returned per page.",
    )
    currentPage: Optional[int] = Field(
        None,
        description="Optionally identifies the current page for display purposes, if returned.",
    )
    first: Optional[AnyUrl] = Field(
        None,
        description="Link to the first page of the collection. Link relation: first.",
    )
    next: Optional[AnyUrl] = Field(
        None,
        description="Link to the next page of the collection, if any. Link relation: next.",
    )
    prev: Optional[AnyUrl] = Field(
        None,
        description="Link to the previous page of the collection, if any. Link relation: prev.",
    )
    last: Optional[AnyUrl] = Field(
        None,
        description="Link to the last page of the collection, if any. Link relation: last.",
    )


class UnitCode(Enum):
    SEC = "SEC"
    MIN = "MIN"


class SupportedMessage(BaseModel):
    messages: Optional[enums.IcarMessageType] = None


class PlanOrActual(Enum):
    Plan = "Plan"
    Actual = "Actual"


class IcarAnimalSetArray(BaseModel):
    __root__: List[resources.IcarAnimalSetResource]


class IcarAnimalSetJoinEventArray(BaseModel):
    __root__: List[resources.IcarAnimalSetJoinEventResource]


class IcarAnimalSetLeaveEventArray(BaseModel):
    __root__: List[resources.IcarAnimalSetLeaveEventResource]


class IcarDeviceArray(BaseModel):
    __root__: List[resources.IcarDeviceResource]


class IcarInventoryTransactionArray(BaseModel):
    __root__: List[resources.IcarInventoryTransactionResource]


class IcarRemarkEventArray(BaseModel):
    __root__: List[resources.IcarRemarkEventResource]


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


class IcarTestDayArray(BaseModel):
    __root__: List[resources.IcarTestDayResource]


class IcarLactationStatusObservedEventArray(BaseModel):
    __root__: List[resources.IcarLactationStatusObservedEventResource]


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


class IcarMilkingDryOffEventArray(BaseModel):
    __root__: List[resources.IcarMilkingDryOffEventResource]


class IcarReproAbortionEventArray(BaseModel):
    __root__: List[resources.IcarReproAbortionEventResource]


class IcarReproDoNotBreedEventArray(BaseModel):
    __root__: List[resources.IcarReproDoNotBreedEventResource]


class IcarGestationArray(BaseModel):
    __root__: List[resources.IcarGestationResource]


class IcarReproStatusObservedEventArray(BaseModel):
    __root__: List[resources.IcarReproStatusObservedEventResource]


class BatchResults(BaseModel):
    __root__: List[resources.IcarBatchResult]


class IcarFeedArray(BaseModel):
    __root__: List[resources.IcarFeedResource]


class IcarRationArray(BaseModel):
    __root__: List[resources.IcarRationResource]


class IcarFeedIntakeEventArray(BaseModel):
    __root__: List[resources.IcarFeedIntakeEventResource]


class IcarFeedRecommendationArray(BaseModel):
    __root__: List[resources.IcarFeedRecommendationResource]


class IcarFeedStorageArray(BaseModel):
    __root__: List[resources.IcarFeedStorageResource]


class IcarFeedTransactionArray(BaseModel):
    __root__: List[resources.IcarFeedTransactionResource]


class IcarGroupFeedingEventArray(BaseModel):
    __root__: List[resources.IcarGroupFeedingEventResource]


class IcarDiagnosisEvent(BaseModel):
    __root__: resources.IcarDiagnosisEventResource


class IcarDiagnosisEventArray(BaseModel):
    __root__: List[resources.IcarDiagnosisEventResource]


class IcarTreatmentEvent(BaseModel):
    __root__: resources.IcarTreatmentEventResource


class IcarTreatmentEventArray(BaseModel):
    __root__: List[resources.IcarTreatmentEventResource]


class IcarGroupTreatmentEvent(BaseModel):
    __root__: resources.IcarGroupTreatmentEventResource


class IcarGroupTreatmentEventArray(BaseModel):
    __root__: List[resources.IcarGroupTreatmentEventResource]


class IcarTreatmentProgramEvent(BaseModel):
    __root__: resources.IcarTreatmentProgramEventResource


class IcarTreatmentProgramEventArray(BaseModel):
    __root__: List[resources.IcarTreatmentProgramEventResource]


class IcarHealthStatusObservedEvent(BaseModel):
    __root__: resources.IcarHealthStatusObservedEventResource


class IcarHealthStatusObservedArray(BaseModel):
    __root__: List[resources.IcarHealthStatusObservedEventResource]


class IcarMedicineTransactionArray(BaseModel):
    __root__: List[resources.IcarMedicineTransactionResource]


class IcarAttentionEventArray(BaseModel):
    __root__: List[resources.IcarAttentionEventResource]


class IcarGroupPositionObservationEventArray(BaseModel):
    __root__: List[resources.IcarGroupPositionObservationEventResource]


class IcarPositionObservationEventArray(BaseModel):
    __root__: List[resources.IcarPositionObservationEventResource]


class IcarObservationSummaryResourceArray(BaseModel):
    __root__: List[resources.IcarObservationSummaryResource]


class IcarMilkingVisitEventArray(BaseModel):
    __root__: List[resources.IcarMilkingVisitEventResource]


class IcarTestDayResultEventArray(BaseModel):
    __root__: List[resources.IcarTestDayResultEventResource]


class IcarWeightEventArray(BaseModel):
    __root__: List[resources.IcarWeightEventResource]


class IcarGroupWeightEventArray(BaseModel):
    __root__: List[resources.IcarGroupWeightEventResource]


class IcarConformationScoreEventArray(BaseModel):
    __root__: List[resources.IcarConformationScoreEventResource]


class IcarAnimalCoreResourceArray(BaseModel):
    __root__: List[resources.IcarAnimalCoreResource]


class IcarMovementBirthEventArray(BaseModel):
    __root__: List[resources.IcarMovementBirthEventResource]


class IcarGroupMovementBirthEventArray(BaseModel):
    __root__: List[resources.IcarGroupMovementBirthEventResource]


class IcarMovementDeathEventArray(BaseModel):
    __root__: List[resources.IcarMovementDeathEventResource]


class IcarGroupMovementDeathEventArray(BaseModel):
    __root__: List[resources.IcarGroupMovementDeathEventResource]


class IcarMovementArrivalEventArray(BaseModel):
    __root__: List[resources.IcarMovementArrivalEventResource]


class IcarGroupMovementArrivalEventArray(BaseModel):
    __root__: List[resources.IcarGroupMovementArrivalEventResource]


class IcarMovementDepartureEventArray(BaseModel):
    __root__: List[resources.IcarMovementDepartureEventResource]


class IcarGroupMovementDepartureEventArray(BaseModel):
    __root__: List[resources.IcarGroupMovementDepartureEventResource]


class IcarReproPregnancyCheckEventArray(BaseModel):
    __root__: List[resources.IcarReproPregnancyCheckEventResource]


class VisualDetection(BaseModel):
    heatSigns: Optional[List[enums.IcarReproHeatSignType]] = None
    heatIntensity: Optional[enums.IcarReproHeatIntensityType] = None


class IcarReproHeatEventArray(BaseModel):
    __root__: List[resources.IcarReproHeatEventResource]


class IcarReproInseminationEventArray(BaseModel):
    __root__: List[resources.IcarReproInseminationEventResource]


class IcarReproParturitionEventArray(BaseModel):
    __root__: List[resources.IcarReproParturitionEventResource]


class IcarReproMatingRecommendationArray(BaseModel):
    __root__: List[resources.IcarReproMatingRecommendationResource]


class IcarReproEmbryoFlushingEventArray(BaseModel):
    __root__: List[resources.IcarReproEmbryoFlushingEventResource]
