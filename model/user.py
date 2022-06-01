from pydantic import BaseModel

class AirQuality(BaseModel):
    id:str
    Name:str
    Time:str
    CO2: float
    CO: float
    VOC:float
    RH:float
    PM10:float
    PM25:float
    Temp:float
    Press:float