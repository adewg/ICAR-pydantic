from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field

from . import others, resources


class IcarErrorCollection(BaseModel):
    errors: Optional[List[resources.IcarResponseMessageResource]] = None


class IcarResourceCollection(BaseModel):
    view: Optional[others.View] = Field(
        None, description="Information about the current view or page of the collection"
    )


class IcarAnimalSetCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalSetResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animal sets.",
    )


class IcarAnimalSetJoinEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalSetJoinEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animal set join events.",
    )


class IcarAnimalSetLeaveEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAnimalSetLeaveEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case animal set leave events.",
    )


class IcarDeviceCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarDeviceResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case weight events.",
    )


class IcarInventoryTransactionCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarInventoryTransactionResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case inventory transactions.",
    )


class IcarRemarkEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarRemarkEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case remark events.",
    )


class IcarTestDayCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTestDayResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case test days.",
    )


class IcarLactationStatusObservedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarLactationStatusObservedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case lactation status events.",
    )


class IcarMilkingDryOffEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMilkingDryOffEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case weight events.",
    )


class IcarReproAbortionEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproAbortionEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case abortion events.",
    )


class IcarReproDoNotBreedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproDoNotBreedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case do not breed events.",
    )


class IcarGestationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGestationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case gestations.",
    )


class IcarReproStatusObservedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproStatusObservedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case reproductive status events.",
    )


class IcarFeedCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feeds.",
    )


class IcarRationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarRationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case rations.",
    )


class IcarFeedIntakeEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedIntakeEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feed intakes.",
    )


class IcarFeedRecommendationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedRecommendationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feed recommendations.",
    )


class IcarFeedStorageCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarFeedStorageResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case feed storage devices.",
    )


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


class IcarGroupFeedingEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupFeedingEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case group feeding events.",
    )


class IcarDiagnosisEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarDiagnosisEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case diagnosis events.",
    )


class IcarTreatmentEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTreatmentEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case treatment events.",
    )


class IcarGroupTreatmentEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupTreatmentEventResource]] = Field(
        None, description="Provides the array of objects, in this case weighing events."
    )


class IcarTreatmentProgramEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTreatmentProgramEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case treatment program events.",
    )


class IcarHealthStatusObservedEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarHealthStatusObservedEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case lactation status events.",
    )


class IcarMedicineTransactionCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMedicineTransactionResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case inventory transactions.",
    )


class IcarAttentionEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarAttentionEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case attention events.",
    )


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


class IcarPositionObservationEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarPositionObservationEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case position observation events.",
    )


class IcarObservationSummaryCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarObservationSummaryResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case observation summary statistics.",
    )


class IcarMilkingVisitEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarMilkingVisitEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case milking visit events.",
    )


class IcarTestDayResultEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarTestDayResultEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case test day result events.",
    )


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


class IcarGroupWeightEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarGroupWeightEventResource]] = Field(
        None, description="Provides the array of objects, in this case weighing events."
    )


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


class IcarLocationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarLocationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case locations.",
    )


class IcarReproPregnancyCheckEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproPregnancyCheckEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case pregnancy check events.",
    )


class IcarReproHeatEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproHeatEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case heat events.",
    )


class IcarReproInseminationEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproInseminationEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case insemination events.",
    )


class IcarReproParturitionEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproParturitionEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case parturition events.",
    )


class IcarReproMatingRecommendationCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproMatingRecommendationResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case mating recommendation events.",
    )


class IcarReproEmbryoFlushingEventCollection(IcarResourceCollection):
    member: Optional[List[resources.IcarReproEmbryoFlushingEventResource]] = Field(
        None,
        description="As per JSON-LD Hydra syntax, member provides the array of objects, in this case embryo flushing events.",
    )


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
