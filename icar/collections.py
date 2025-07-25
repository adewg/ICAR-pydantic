from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field

from . import resources


class IcarErrorCollection(BaseModel):
    errors: Optional[List[resources.IcarResponseMessageResource]] = None


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


class IcarResourceCollection(BaseModel):
    view: Optional[View] = Field(
        None, description="Information about the current view or page of the collection"
    )


class IcarAnimalSetCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalSetResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animal sets.",
    )


class IcarAnimalSetArray(BaseModel):
    __root__: List[resources.IcarAnimalSetResource]


class IcarAnimalSetJoinEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalSetJoinEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animal set join events.",
    )


class IcarAnimalSetJoinEventArray(BaseModel):
    __root__: List[resources.IcarAnimalSetJoinEventResource]


class IcarAnimalSetLeaveEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalSetLeaveEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animal set leave events.",
    )


class IcarAnimalSetLeaveEventArray(BaseModel):
    __root__: List[resources.IcarAnimalSetLeaveEventResource]


class IcarDeviceCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarDeviceResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case weight events.",
    )


class IcarDeviceArray(BaseModel):
    __root__: List[resources.IcarDeviceResource]


class IcarInventoryTransactionCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarInventoryTransactionResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case inventory transactions.",
    )


class IcarInventoryTransactionArray(BaseModel):
    __root__: List[resources.IcarInventoryTransactionResource]


class IcarRemarkEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarRemarkEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case remark events.",
    )


class IcarRemarkEventArray(BaseModel):
    __root__: List[resources.IcarRemarkEventResource]


class IcarTestDayCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTestDayResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case test days.",
    )


class IcarTestDayArray(BaseModel):
    __root__: List[resources.IcarTestDayResource]


class IcarLactationStatusObservedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarLactationStatusObservedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case lactation status events.",
    )


class IcarLactationStatusObservedEventArray(BaseModel):
    __root__: List[resources.IcarLactationStatusObservedEventResource]


class IcarMilkingDryOffEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMilkingDryOffEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case weight events.",
    )


class IcarMilkingDryOffEventArray(BaseModel):
    __root__: List[resources.IcarMilkingDryOffEventResource]


class IcarReproAbortionEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproAbortionEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case abortion events.",
    )


class IcarReproAbortionEventArray(BaseModel):
    __root__: List[resources.IcarReproAbortionEventResource]


class IcarReproDoNotBreedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproDoNotBreedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case do not breed events.",
    )


class IcarReproDoNotBreedEventArray(BaseModel):
    __root__: List[resources.IcarReproDoNotBreedEventResource]


class IcarGestationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGestationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case gestations.",
    )


class IcarGestationArray(BaseModel):
    __root__: List[resources.IcarGestationResource]


class IcarReproStatusObservedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproStatusObservedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case reproductive status events.",
    )


class IcarReproStatusObservedEventArray(BaseModel):
    __root__: List[resources.IcarReproStatusObservedEventResource]


class BatchResults(BaseModel):
    __root__: List[resources.IcarBatchResult]


class IcarFeedCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feeds.",
    )


class IcarFeedArray(BaseModel):
    __root__: List[resources.IcarFeedResource]


class IcarRationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarRationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case rations.",
    )


class IcarRationArray(BaseModel):
    __root__: List[resources.IcarRationResource]


class IcarFeedIntakeEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedIntakeEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feed intakes.",
    )


class IcarFeedIntakeEventArray(BaseModel):
    __root__: List[resources.IcarFeedIntakeEventResource]


class IcarFeedRecommendationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedRecommendationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feed recommendations.",
    )


class IcarFeedRecommendationArray(BaseModel):
    __root__: List[resources.IcarFeedRecommendationResource]


class IcarFeedStorageCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedStorageResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feed storage devices.",
    )


class IcarFeedStorageArray(BaseModel):
    __root__: List[resources.IcarFeedStorageResource]


class IcarFeedReportCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedReportResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feed reports.",
    )


class IcarFeedTransactionCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedTransactionResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case inventory transactions.",
    )


class IcarFeedTransactionArray(BaseModel):
    __root__: List[resources.IcarFeedTransactionResource]


class IcarGroupFeedingEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupFeedingEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case group feeding events.",
    )


class IcarGroupFeedingEventArray(BaseModel):
    __root__: List[resources.IcarGroupFeedingEventResource]


class IcarDiagnosisEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarDiagnosisEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case diagnosis events.",
    )


class IcarDiagnosisEventArray(BaseModel):
    __root__: List[resources.IcarDiagnosisEventResource]


class IcarTreatmentEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTreatmentEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case treatment events.",
    )


class IcarTreatmentEventArray(BaseModel):
    __root__: List[resources.IcarTreatmentEventResource]


class IcarGroupTreatmentEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupTreatmentEventResource]] = Field(
        None, description="Provides the array of objects, in this case weighing events."
    )


class IcarGroupTreatmentEventArray(BaseModel):
    __root__: List[resources.IcarGroupTreatmentEventResource]


class IcarTreatmentProgramEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTreatmentProgramEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case treatment program events.",
    )


class IcarTreatmentProgramEventArray(BaseModel):
    __root__: List[resources.IcarTreatmentProgramEventResource]


class IcarHealthStatusObservedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarHealthStatusObservedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case lactation status events.",
    )


class IcarHealthStatusObservedArray(BaseModel):
    __root__: List[resources.IcarHealthStatusObservedEventResource]


class IcarMedicineTransactionCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMedicineTransactionResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case inventory transactions.",
    )


class IcarMedicineTransactionArray(BaseModel):
    __root__: List[resources.IcarMedicineTransactionResource]


class IcarAttentionEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAttentionEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case attention events.",
    )


class IcarAttentionEventArray(BaseModel):
    __root__: List[resources.IcarAttentionEventResource]


class IcarStatisticsCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarStatisticsResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case statistics.",
    )


class IcarGroupPositionObservationEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupPositionObservationEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case group position observation events.",
    )


class IcarGroupPositionObservationEventArray(BaseModel):
    __root__: List[resources.IcarGroupPositionObservationEventResource]


class IcarPositionObservationEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarPositionObservationEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case position observation events.",
    )


class IcarPositionObservationEventArray(BaseModel):
    __root__: List[resources.IcarPositionObservationEventResource]


class IcarObservationSummaryCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarObservationSummaryResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case observation summary statistics.",
    )


class IcarObservationSummaryResourceArray(BaseModel):
    __root__: List[resources.IcarObservationSummaryResource]


class IcarMilkingVisitEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMilkingVisitEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case milking visit events.",
    )


class IcarMilkingVisitEventArray(BaseModel):
    __root__: List[resources.IcarMilkingVisitEventResource]


class IcarTestDayResultEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTestDayResultEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case test day result events.",
    )


class IcarTestDayResultEventArray(BaseModel):
    __root__: List[resources.IcarTestDayResultEventResource]


class IcarDailyMilkingAveragesCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarDailyMilkingAveragesResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case test day result events.",
    )


class IcarMilkPredictionsCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMilkPredictionResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case milk prediction events.",
    )


class IcarLactationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarLactationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case lactations.",
    )


class IcarWithdrawalEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarWithdrawalEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case lactation status events.",
    )


class IcarWeightEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarWeightEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case weight events.",
    )


class IcarWeightEventArray(BaseModel):
    __root__: List[resources.IcarWeightEventResource]


class IcarGroupWeightEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupWeightEventResource]] = Field(
        None, description="Provides the array of objects, in this case weighing events."
    )


class IcarGroupWeightEventArray(BaseModel):
    __root__: List[resources.IcarGroupWeightEventResource]


class IcarBreedingValueCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarBreedingValueResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case breeding values.",
    )


class IcarTypeClassificationEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTypeClassificationEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case type classification events.",
    )


class IcarConformationScoreEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarConformationScoreEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case conformation score events.",
    )


class IcarConformationScoreEventArray(BaseModel):
    __root__: List[resources.IcarConformationScoreEventResource]


class IcarLocationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarLocationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case locations.",
    )


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


class IcarReproPregnancyCheckEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproPregnancyCheckEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case pregnancy check events.",
    )


class IcarReproPregnancyCheckEventArray(BaseModel):
    __root__: List[resources.IcarReproPregnancyCheckEventResource]


class IcarReproHeatEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproHeatEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case heat events.",
    )


class IcarReproHeatEventArray(BaseModel):
    __root__: List[resources.IcarReproHeatEventResource]


class IcarReproInseminationEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproInseminationEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case insemination events.",
    )


class IcarReproInseminationEventArray(BaseModel):
    __root__: List[resources.IcarReproInseminationEventResource]


class IcarReproParturitionEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproParturitionEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case parturition events.",
    )


class IcarReproParturitionEventArray(BaseModel):
    __root__: List[resources.IcarReproParturitionEventResource]


class IcarReproMatingRecommendationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproMatingRecommendationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case mating recommendation events.",
    )


class IcarReproMatingRecommendationArray(BaseModel):
    __root__: List[resources.IcarReproMatingRecommendationResource]


class IcarReproEmbryoFlushingEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproEmbryoFlushingEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case embryo flushing events.",
    )


class IcarReproEmbryoFlushingEventArray(BaseModel):
    __root__: List[resources.IcarReproEmbryoFlushingEventResource]


class IcarAnimalSortingCommandCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalSortingCommandResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animal sorting commands (icarAnimalSortingCommandResource).",
    )


class IcarSortingSiteCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarSortingSiteResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case sorting-sites.",
    )


class IcarAnimalCoreCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalCoreResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animals.",
    )


class IcarMovementBirthEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMovementBirthEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case birth events.",
    )


class IcarGroupMovementBirthEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupMovementBirthEventResource]] = Field(
        None, description="Provides the array of objects, in this case birth events."
    )


class IcarMovementDeathEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMovementDeathEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case death events.",
    )


class IcarGroupMovementDeathEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupMovementDeathEventResource]] = Field(
        None, description="Provides the array of objects, in this case death events."
    )


class IcarMovementArrivalEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMovementArrivalEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case arrival events.",
    )


class IcarGroupMovementArrivalEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupMovementArrivalEventResource]] = Field(
        None, description="Provides the array of objects, in this case arrival events."
    )


class IcarMovementDepartureEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMovementDepartureEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case departure events.",
    )


class IcarGroupMovementDepartureEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupMovementDepartureEventResource]] = Field(
        None,
        description="Provides the array of objects, in this case departure events.",
    )
