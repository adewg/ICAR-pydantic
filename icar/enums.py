from __future__ import annotations

from enum import Enum


class IcarBatchResultSeverityType(Enum):
    Information = "Information"
    Warning = "Warning"
    Error = "Error"


class IcarFeedCategoryType(Enum):
    Concentrate = "Concentrate"
    Roughage = "Roughage"
    Additives = "Additives"
    Other = "Other"


class UncefactMassUnitsType(Enum):
    KGM = "KGM"
    GRM = "GRM"
    LBR = "LBR"
    TNE = "TNE"
    MC = "MC"
    MGM = "MGM"
    ONZ = "ONZ"
    PN = "PN"


class IcarMethodType(Enum):
    Analyzed = "Analyzed"
    Derived = "Derived"


class IcarMessageType(Enum):
    MilkingVisits = "MilkingVisits"
    TestDayResults = "TestDayResults"
    Births = "Births"
    Deaths = "Deaths"
    Arrivals = "Arrivals"
    Departures = "Departures"
    Animals = "Animals"
    PregnancyChecks = "PregnancyChecks"
    Heats = "Heats"
    DryingOffs = "DryingOffs"
    Inseminations = "Inseminations"
    Abortions = "Abortions"
    Parturitions = "Parturitions"
    MatingRecommendations = "MatingRecommendations"
    Devices = "Devices"
    Weights = "Weights"
    Locations = "Locations"
    AnimalSetJoins = "AnimalSetJoins"
    AnimalSetLeaves = "AnimalSetLeaves"
    ProgenyDetails = "ProgenyDetails"
    BreedingValues = "BreedingValues"
    FeedIntakes = "FeedIntakes"
    FeedReports = "FeedReports"
    FeedRecommendations = "FeedRecommendations"
    Rations = "Rations"
    FeedStorages = "FeedStorages"
    Gestations = "Gestations"
    DoNotBreedInstructions = "DoNotBreedInstructions"
    ReproductionStatusObservations = "ReproductionStatusObservations"
    Lactations = "Lactations"
    LactationStatusObservations = "LactationStatusObservations"
    Withdrawals = "Withdrawals"
    DailyMilkingAverages = "DailyMilkingAverages"
    Diagnoses = "Diagnoses"
    Treatments = "Treatments"
    TreatmentPrograms = "TreatmentPrograms"
    HealthStatusObservations = "HealthStatusObservations"
    ConformationScores = "ConformationScores"
    TypeClassifications = "TypeClassifications"
    Statistics = "Statistics"
    Schemes = "Schemes"
    Embryos = "Embryos"
    SemenStraws = "SemenStraws"
    Flushings = "Flushings"
    GroupTreatments = "GroupTreatments"
    GroupBirths = "GroupBirths"
    GroupArrivals = "GroupArrivals"
    GroupDepartures = "GroupDepartures"
    GroupDeaths = "GroupDeaths"
    GroupWeights = "GroupWeights"
    Other = "Other"


class IcarInventoryTransactionKindType(Enum):
    Receipt = "Receipt"
    Disposal = "Disposal"
    OnHand = "OnHand"
    Produce = "Produce"
    StockTake = "StockTake"
    Use = "Use"


class IcarProductFamilyType(Enum):
    Animal_Feeds = "Animal Feeds"
    Animal_Reproductive_Products = "Animal Reproductive Products"
    Veterinary_Supplies = "Veterinary Supplies"
    Seed_and_Plant_Material = "Seed and Plant Material"
    Fertilisers_and_Nutrients = "Fertilisers and Nutrients"
    Pest_Control_Products = "Pest Control Products"
    Other_Animal_Products = "Other Animal Products"
    Milking_Supplies = "Milking Supplies"
    Fencing_Supplies = "Fencing Supplies"
    Water_System_Supplies = "Water System Supplies"
    Fuel = "Fuel"
    Other = "Other"


class IcarGroupEventMethodType(Enum):
    ExistingAnimalSet = "ExistingAnimalSet"
    EmbeddedAnimalSet = "EmbeddedAnimalSet"
    InventoryClassification = "InventoryClassification"
    EmbeddedAnimalSetAndInventoryClassification = (
        "EmbeddedAnimalSetAndInventoryClassification"
    )


class IcarAnimalSpecieType(Enum):
    Buffalo = "Buffalo"
    Cattle = "Cattle"
    Deer = "Deer"
    Elk = "Elk"
    Goat = "Goat"
    Horse = "Horse"
    Pig = "Pig"
    Sheep = "Sheep"


class IcarAnimalGenderType(Enum):
    Female = "Female"
    FemaleNeuter = "FemaleNeuter"
    Male = "Male"
    MaleCryptorchid = "MaleCryptorchid"
    MaleNeuter = "MaleNeuter"
    Unknown = "Unknown"


class IcarAnimalReproductionStatusType(Enum):
    Open = "Open"
    Inseminated = "Inseminated"
    Pregnant = "Pregnant"
    NotPregnant = "NotPregnant"
    Birthed = "Birthed"
    DoNotBreed = "DoNotBreed"
    PregnantMultipleFoetus = "PregnantMultipleFoetus"


class IcarAnimalLactationStatusType(Enum):
    Dry = "Dry"
    Lead = "Lead"
    Fresh = "Fresh"
    Early = "Early"
    Lactating = "Lactating"


class IcarProductionPurposeType(Enum):
    Meat = "Meat"
    Milk = "Milk"
    Wool = "Wool"


class IcarSetPurposeType(Enum):
    Enclosure = "Enclosure"
    Feeding = "Feeding"
    Finishing = "Finishing"
    Growing = "Growing"
    Health = "Health"
    Lactation = "Lactation"
    Movement = "Movement"
    Rearing = "Rearing"
    Reproduction = "Reproduction"
    Session = "Session"
    Other = "Other"


class IcarDiagnosisStageType(Enum):
    Early = "Early"
    Acute = "Acute"
    SubAcute = "SubAcute"
    Chronic = "Chronic"
    AcuteOnChronic = "AcuteOnChronic"
    EndStage = "EndStage"
    Other = "Other"


class IcarDiagnosisSeverityType(Enum):
    Light = "Light"
    Moderate = "Moderate"
    Severe = "Severe"


class IcarPositionOnAnimalType(Enum):
    LegsFrontLeft = "LegsFrontLeft"
    LegsFrontRight = "LegsFrontRight"
    LegsRearLeft = "LegsRearLeft"
    LegsRearRight = "LegsRearRight"
    UdderFrontLeft = "UdderFrontLeft"
    UdderFrontRight = "UdderFrontRight"
    UdderRearLeft = "UdderRearLeft"
    UdderRearRight = "UdderRearRight"
    OvariesLeft = "OvariesLeft"
    OvariesRight = "OvariesRight"
    OvariesUnknown = "OvariesUnknown"
    Neck = "Neck"
    Head = "Head"
    Mouth = "Mouth"
    Back = "Back"
    Testes = "Testes"
    Other = "Other"


class IcarWithdrawalProductType(Enum):
    Meat = "Meat"
    Milk = "Milk"
    Eggs = "Eggs"
    Honey = "Honey"
    Velvet = "Velvet"
    Fibre = "Fibre"
    Other = "Other"


class UncefactDoseUnitsType(Enum):
    MLT = "MLT"
    LTR = "LTR"
    MGM = "MGM"
    GRM = "GRM"
    XTU = "XTU"
    XVI = "XVI"
    XAR = "XAR"
    XCQ = "XCQ"
    GJ = "GJ"
    GL = "GL"
    GRN = "GRN"
    L19 = "L19"
    NA = "NA"
    SYR = "SYR"
    WW = "WW"
    TU = "TU"
    EA = "EA"


class IcarAnimalHealthStatusType(Enum):
    Healthy = "Healthy"
    Suspicious = "Suspicious"
    Ill = "Ill"
    InTreatment = "InTreatment"
    ToBeCulled = "ToBeCulled"


class IcarAttentionCategoryType(Enum):
    Behaviour = "Behaviour"
    Environment = "Environment"
    Health = "Health"
    Reproduction = "Reproduction"
    DeviceIssue = "DeviceIssue"
    Weight = "Weight"
    Other = "Other"


class IcarAttentionCauseType(Enum):
    Activity = "Activity"
    AnimalTemperature = "AnimalTemperature"
    AnimalTemperatureDecrease = "AnimalTemperatureDecrease"
    AnimalTemperatureIncrease = "AnimalTemperatureIncrease"
    BodyCondition = "BodyCondition"
    EatingLess = "EatingLess"
    EnvironmentTemperature = "EnvironmentTemperature"
    Disturbance = "Disturbance"
    Health = "Health"
    HeartRate = "HeartRate"
    Inactivity = "Inactivity"
    Ketosis = "Ketosis"
    Lameness = "Lameness"
    Location = "Location"
    LowerRumination = "LowerRumination"
    LyingTooLong = "LyingTooLong"
    LyingTooShort = "LyingTooShort"
    Mastitis = "Mastitis"
    MobilityScore = "MobilityScore"
    NoMovement = "NoMovement"
    Parturition = "Parturition"
    PostParturitionRisk = "PostParturitionRisk"
    ProlongedParturition = "ProlongedParturition"
    RespirationRate = "RespirationRate"
    Standing = "Standing"
    StandingUp = "StandingUp"
    Walking = "Walking"
    Heat = "Heat"
    LowBattery = "LowBattery"
    Offline = "Offline"
    UnderWeight = "UnderWeight"
    OverWeight = "OverWeight"
    AtTargetWeight = "AtTargetWeight"
    Other = "Other"
    Undefined = "Undefined"


class IcarAttentionPriorityType(Enum):
    Informational = "Informational"
    Normal = "Normal"
    Urgent = "Urgent"
    Critical = "Critical"


class IcarStatisticsPurposeType(Enum):
    TestDay = "TestDay"
    Feeding = "Feeding"
    Reproduction = "Reproduction"
    BreedingValues = "BreedingValues"
    TypeClassification = "TypeClassification"
    Registration = "Registration"


class IcarGroupType(Enum):
    Herd = "Herd"
    LactationNumber = "LactationNumber"
    DaysInMilk = "DaysInMilk"
    AnimalSet = "AnimalSet"


class IcarAggregationType(Enum):
    Average = "Average"
    Sum = "Sum"
    StDev = "StDev"
    Min = "Min"
    Max = "Max"
    Count = "Count"
    Range = "Range"
    Index = "Index"


class IcarDurationType(Enum):
    P1D = "P1D"
    PT1H = "PT1H"
    PT24H = "PT24H"
    PT96H = "PT96H"
    P1W = "P1W"
    P1M = "P1M"


class IcarMilkingTypeCode(Enum):
    Manual = "Manual"
    Automated = "Automated"


class IcarBottleIdentifierType(Enum):
    BRC = "BRC"
    RFD = "RFD"


class IcarValidSampleFillingIndicatorType(Enum):
    field_0 = "0"
    field_1 = "1"
    field_2 = "2"


class IcarMilkingRemarksType(Enum):
    AnimalSick = "AnimalSick"
    MilkingIncomplete = "MilkingIncomplete"
    TeatSeparated = "TeatSeparated"
    MilkedSeparately = "MilkedSeparately"
    SamplingFailed = "SamplingFailed"


class IcarTestDayCodeType(Enum):
    Dry = "Dry"
    SamplingImpossible = "SamplingImpossible"
    Sick = "Sick"


class IcarLactationType(Enum):
    Normal = "Normal"
    field_100Days = "100Days"
    field_200Days = "200Days"
    field_305Days = "305Days"
    field_365Days = "365Days"


class IcarMilkRecordingProtocolType(Enum):
    A_OfficialMRORepresentative = "A-OfficialMRORepresentative"
    B_HerdOwnerOrNominee = "B-HerdOwnerOrNominee"
    C_Both = "C-Both"


class IcarMilkRecordingSchemeType(Enum):
    AllMilkingsAtTestday = "AllMilkingsAtTestday"
    AllMilkingsInPeriod = "AllMilkingsInPeriod"
    OneMilkingAtTestday = "OneMilkingAtTestday"


class IcarMilkingsPerDayType(Enum):
    field_1 = "1"
    field_2 = "2"
    field_3 = "3"
    field_4 = "4"
    Robot = "Robot"


class IcarMilkSamplingSchemeType(Enum):
    ProportionalSizeSamplingOfAllMilkings = "ProportionalSizeSamplingOfAllMilkings"
    ConstantSizeSamplingOfAllMilkings = "ConstantSizeSamplingOfAllMilkings"
    AlternateSampling = "AlternateSampling"
    CorrectedSampling = "CorrectedSampling"
    OneMilkingSampleInAMS = "OneMilkingSampleInAMS"
    MulitpleMilkingSampleInAMS = "MulitpleMilkingSampleInAMS"


class IcarMilkSamplingMomentType(Enum):
    Composite = "Composite"
    Morning = "Morning"
    Evening = "Evening"


class IcarMilkingType(Enum):
    OfficialMilkResultSuppliedByMRO = "OfficialMilkResultSuppliedByMRO"
    MeasureByICARApprovedEquipment = "MeasureByICARApprovedEquipment"
    MeasureByNotApprovedEquipment = "MeasureByNotApprovedEquipment"


class IcarWeightMethodType(Enum):
    LoadCell = "LoadCell"
    Girth = "Girth"
    Assessed = "Assessed"
    WalkOver = "WalkOver"
    Predicted = "Predicted"
    Imaged = "Imaged"
    FrontEndCorrelated = "FrontEndCorrelated"
    GroupAverage = "GroupAverage"


class IcarBreedingValueCalculationType(Enum):
    BreedingValue = "BreedingValue"
    ParentAverageBreedingValue = "ParentAverageBreedingValue"
    GenomicBreedingValue = "GenomicBreedingValue"
    ConvertedBreedingValue = "ConvertedBreedingValue"
    Other = "Other"


class IcarConformationTraitGroupType(Enum):
    Composite = "Composite"
    Linear = "Linear"


class IcarConformationTraitType(Enum):
    Angularity = "Angularity"
    BackLength = "BackLength"
    BackWidth = "BackWidth"
    BodyConditionScore = "BodyConditionScore"
    BodyDepth = "BodyDepth"
    BodyLength = "BodyLength"
    BoneStructure = "BoneStructure"
    CentralLigament = "CentralLigament"
    ChestDepth = "ChestDepth"
    ChestWidth = "ChestWidth"
    ClawAngle = "ClawAngle"
    DairyStrength = "DairyStrength"
    FeetLegs = "FeetLegs"
    FinalScore = "FinalScore"
    FlankDepth = "FlankDepth"
    FootAngle = "FootAngle"
    ForePasternsSideView = "ForePasternsSideView"
    ForeUdderAttachment = "ForeUdderAttachment"
    ForeUdderLength = "ForeUdderLength"
    Frame = "Frame"
    FrontFeetOrientation = "FrontFeetOrientation"
    FrontLegsFrontView = "FrontLegsFrontView"
    FrontTeatPlacement = "FrontTeatPlacement"
    HeightAtRump = "HeightAtRump"
    HeightAtWithers = "HeightAtWithers"
    HindPasternsSideView = "HindPasternsSideView"
    HockDevelopment = "HockDevelopment"
    LengthOfRump = "LengthOfRump"
    Locomotion = "Locomotion"
    LoinStrength = "LoinStrength"
    Muscularity = "Muscularity"
    MuscularityComposite = "MuscularityComposite"
    MuscularityShoulderSideView = "MuscularityShoulderSideView"
    MuscularityShoulderTopView = "MuscularityShoulderTopView"
    MuzzleWidth = "MuzzleWidth"
    RearLegsRearView = "RearLegsRearView"
    RearLegsSet = "RearLegsSet"
    RearLegsSideView = "RearLegsSideView"
    RearTeatPlacement = "RearTeatPlacement"
    RearUdderHeight = "RearUdderHeight"
    RearUdderWidth = "RearUdderWidth"
    RoundingOfRibs = "RoundingOfRibs"
    RumpAngle = "RumpAngle"
    RumpLength = "RumpLength"
    RumpWidth = "RumpWidth"
    SkinThickness = "SkinThickness"
    Stature = "Stature"
    TailSet = "TailSet"
    TeatDirection = "TeatDirection"
    TeatForm = "TeatForm"
    TeatLength = "TeatLength"
    TeatPlacementRearView = "TeatPlacementRearView"
    TeatPlacementSideView = "TeatPlacementSideView"
    TeatThickness = "TeatThickness"
    ThicknessOfBone = "ThicknessOfBone"
    ThicknessOfTeat = "ThicknessOfTeat"
    ThicknessOfLoin = "ThicknessOfLoin"
    ThighLength = "ThighLength"
    ThighRoundingSideView = "ThighRoundingSideView"
    ThighWidthRearView = "ThighWidthRearView"
    ThurlWidth = "ThurlWidth"
    TopLine = "TopLine"
    Type = "Type"
    Udder = "Udder"
    UdderBalance = "UdderBalance"
    UdderDepth = "UdderDepth"
    WidthAtHips = "WidthAtHips"
    WidthAtPins = "WidthAtPins"


class IcarConformationScoringMethodType(Enum):
    Manual = "Manual"
    Automated = "Automated"


class IcarAnimalStatusType(Enum):
    Alive = "Alive"
    Dead = "Dead"
    OffFarm = "OffFarm"
    Unknown = "Unknown"


class IcarAnimalRelationType(Enum):
    Genetic = "Genetic"
    Recipient = "Recipient"
    Adoptive = "Adoptive"


class IcarRegistrationReasonType(Enum):
    Born = "Born"
    Registered = "Registered"


class IcarDeathReasonType(Enum):
    Missing = "Missing"
    Parturition = "Parturition"
    Disease = "Disease"
    Accident = "Accident"
    Consumption = "Consumption"
    Culled = "Culled"
    Other = "Other"
    Unknown = "Unknown"
    Age = "Age"
    Mastitis = "Mastitis"
    Production = "Production"
    LegOrClaw = "LegOrClaw"
    MilkingAbility = "MilkingAbility"
    Nutrition = "Nutrition"
    Fertility = "Fertility"


class IcarDeathDisposalMethodType(Enum):
    ApprovedService = "ApprovedService"
    Consumption = "Consumption"
    OnPremise = "OnPremise"
    Other = "Other"


class IcarDeathMethodType(Enum):
    Perished = "Perished"
    Slaughter = "Slaughter"
    Culled = "Culled"
    Theft = "Theft"
    Lost = "Lost"
    Accident = "Accident"
    Euthanized = "Euthanized"
    Other = "Other"


class IcarArrivalReasonType(Enum):
    Purchase = "Purchase"
    InternalTransfer = "InternalTransfer"
    Imported = "Imported"
    StudService = "StudService"
    StudServiceReturn = "StudServiceReturn"
    Slaughter = "Slaughter"
    Agistment = "Agistment"
    AgistmentReturn = "AgistmentReturn"
    Show = "Show"
    ShowReturn = "ShowReturn"
    Sale = "Sale"
    SaleReturn = "SaleReturn"
    Other = "Other"


class IcarDepartureKindType(Enum):
    InternalTransfer = "InternalTransfer"
    Export = "Export"
    Slaughter = "Slaughter"
    Newborn = "Newborn"
    StudService = "StudService"
    StudServiceReturn = "StudServiceReturn"
    Agistment = "Agistment"
    AgistmentReturn = "AgistmentReturn"
    Show = "Show"
    ShowReturn = "ShowReturn"
    Sale = "Sale"
    SaleReturn = "SaleReturn"
    Other = "Other"


class IcarDepartureReasonType(Enum):
    Age = "Age"
    Superfluous = "Superfluous"
    Slaughter = "Slaughter"
    Sale = "Sale"
    Newborn = "Newborn"
    LegOrClaw = "LegOrClaw"
    Nutrition = "Nutrition"
    Parturition = "Parturition"
    Mastitis = "Mastitis"
    Fertility = "Fertility"
    Health = "Health"
    Production = "Production"
    MilkingAbility = "MilkingAbility"
    BadType = "BadType"
    Behaviour = "Behaviour"
    Other = "Other"
    Unknown = "Unknown"


class IcarReproPregnancyMethodType(Enum):
    Echography = "Echography"
    Palpation = "Palpation"
    Blood = "Blood"
    Milk = "Milk"
    Visual = "Visual"
    Other = "Other"


class IcarReproPregnancyResultType(Enum):
    Empty = "Empty"
    Pregnant = "Pregnant"
    Multiple = "Multiple"
    Unknown = "Unknown"


class IcarReproHeatDetectionMethodType(Enum):
    Chemical = "Chemical"
    Visual = "Visual"
    Pedometer = "Pedometer"
    Collar = "Collar"
    EarTag = "EarTag"
    Bolus = "Bolus"
    Other = "Other"


class IcarReproHeatCertaintyType(Enum):
    InHeat = "InHeat"
    Suspect = "Suspect"
    Potential = "Potential"


class IcarReproHeatSignType(Enum):
    Slime = "Slime"
    ClearSlime = "ClearSlime"
    InterestedInOtherAnimals = "InterestedInOtherAnimals"
    Bawling = "Bawling"
    Blood = "Blood"
    StandsUnder = "StandsUnder"


class IcarReproHeatIntensityType(Enum):
    VeryWeak = "VeryWeak"
    Weak = "Weak"
    Normal = "Normal"
    Strong = "Strong"
    VeryStrong = "VeryStrong"


class IcarReproInseminationType(Enum):
    NaturalService = "NaturalService"
    RunWithBull = "RunWithBull"
    Insemination = "Insemination"
    Implantation = "Implantation"


class IcarReproSemenPreservationType(Enum):
    Liquid = "Liquid"
    Frozen = "Frozen"


class IcarReproCalvingEaseType(Enum):
    EasyUnassisted = "EasyUnassisted"
    EasyAssisted = "EasyAssisted"
    DifficultExtraAssistance = "DifficultExtraAssistance"
    DifficultVeterinaryCare = "DifficultVeterinaryCare"
    CaesareanOrSurgery = "CaesareanOrSurgery"


class IcarParturitionBirthStatusType(Enum):
    Alive = "Alive"
    Stillborn = "Stillborn"
    Aborted = "Aborted"
    DiedBeforeTaggingDate = "DiedBeforeTaggingDate"
    DiedAfterTaggingDate = "DiedAfterTaggingDate"
    SlaughteredAtBirth = "SlaughteredAtBirth"
    EuthanisedAtBirth = "EuthanisedAtBirth"


class IcarParturitionBirthSizeType(Enum):
    ExtraSmall = "ExtraSmall"
    Small = "Small"
    Average = "Average"
    Large = "Large"
    ExtraLarge = "ExtraLarge"


class IcarRecommendationType(Enum):
    SireRecommended = "SireRecommended"
    RecommendationImpossible = "RecommendationImpossible"
    BeefSire = "BeefSire"
    NoBreedingSire = "NoBreedingSire"


class IcarReproEmbryoFlushingMethodType(Enum):
    OPU_IVF = "OPU-IVF"
    Superovulation = "Superovulation"
