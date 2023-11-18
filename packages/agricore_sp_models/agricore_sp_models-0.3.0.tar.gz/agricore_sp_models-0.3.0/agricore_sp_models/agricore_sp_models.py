from pydantic import BaseModel
from typing import Optional


class AgriculturalProduction(BaseModel):
    id: Optional[int] = None
    farmId: int
    yearId: int
    productGroupId: Optional[int] = None
    valueSales: float
    quantitySold: float
    cropProduction: float
    irrigatedArea: float
    cultivatedArea: float
    organicProductionType: int
    variableCosts: float
    landValue: float
    
class LivestockProduction(BaseModel):
    id: Optional[int] = None
    farmId: int
    yearId: int
    productGroupId: Optional[int] = None
    numberOfAnimals: float
    numberOfAnimalsSold: int
    valueSoldAnimals: float
    numberAnimalsForSlaughtering: int
    valueSlaughteredAnimals: float
    numberAnimalsRearingBreading: float
    valueAnimalsRearingBreading: float
    milkTotalProduction: float
    milkProductionSold: float
    milkTotalSales: float
    milkVariableCosts: float
    woolTotalProduction: float
    woolProductionSold: float
    eggsTotalSales: float
    eggsTotalProduction: float
    eggsProductionSold: float
    manureTotalSales: float
    dairyCows: int
    variableCosts: float

class Population(BaseModel):
    id: Optional[int] = None
    description: str
    
class Farm(BaseModel):
    id: Optional[int] = None
    populationId: Optional[int] = None
    lat: int
    long: int
    altitude: int
    regionLevel1: int
    regionLevel1Name: str
    regionLevel2: int
    regionLevel2Name: str
    regionLevel3: int
    regionLevel3Name: str
    farmCode: str
    technicalEconomicOrientation: int
    weight_ra: float
    weight_reg: float
        
class ProductGroup(BaseModel):
    id: Optional[int] = None
    populationId: Optional[int] = None
    name: str
    productType: int
    originalNameDatasource: str
    productsIncludedInOriginalDataset: str
    
class FADNProductRelation(BaseModel):
    id: Optional[int] = None
    productGroupId: Optional[int] = None
    fadnProductId: Optional[int] = None
    populationId: Optional[int] = None

class ClosingValue(BaseModel):
    id: Optional[int] = None
    agriculturalLand: float
    landImprovements: float
    forestLand: float
    farmBuildings: float
    machineryAndEquipment: float
    intangibleAssetsTradable: float
    intangibleAssetsNonTradable: float
    otherNonCurrentAssets: float
    longAndMediumTermLoans: float
    totalCurrentAssets: float
    farmNetIncome: float
    grossFarmIncome: float
    subsidiesOnInvestments: float
    vatBalanceOnInvestments: float
    totalOutputCropsAndCropProduction: float
    totalOutputLivestockAndLivestockProduction: float
    otherOutputs: float
    totalIntermediateConsumption: float
    taxes: float
    vatBalanceExcludingInvestments: float
    fixedAssets: float
    depreciation: float
    totalExternalFactors: float
    machinery: float
    farmId: int
    yearId: int
    averageHaPrice: float
    
class Policy(BaseModel):
    id: Optional[int] = None
    policyIdentifier: str
    policyDescription: str
    isCoupled: bool
    
class PolicyProductGroupRelation(BaseModel):
    id: Optional[int] = None
    productGroupId: int
    policyId: int
    populationId: Optional[int] = None

class HolderFarmYearData(BaseModel):
    id: Optional[int] = None
    farmId: Optional[int] = None
    yearId: Optional[int] = None
    holderAge: int
    holderGender: int
    holderSuccessors: int
    holderSuccessorsAge: int
    holderFamilyMembers: int
