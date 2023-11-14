from typing import Annotated
from pydantic import BaseModel
from typing import List, Optional

class AgriculturalProduction(BaseModel):
    id: Optional[int] = None 
    farmId: int 
    yearId: int 
    productGroupId: int 
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
    productGroupId: int
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
    
class Farm(BaseModel):
    id: Optional[int] = None 
    lat: int
    long: int
    altitude: int
    holderAge: int
    holderGender: int
    holderSuccessors: int
    holderSuccessorsAge: int
    holderFamilyMembers: int
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
    name: str
    productType: int
    originalNameDatasource: str
    productsIncludedInOriginalDataset: str
    
class FADNProductRelation(BaseModel):
    id: Optional[int] = None 
    productGroupId: int
    fadnProductId: int

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
    rentBalance: float
    
class Policy(BaseModel):
    id: Optional[int] = None 
    policyIdentifier: str
    policyDescription: str
    isCoupled: bool
    
class PolicyProductGroupRelation(BaseModel):
    id: Optional[int] = None 
    productGroupId: int
    policyId: int
