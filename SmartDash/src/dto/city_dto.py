from pydantic import BaseModel, validator, Field
from typing import List, Optional
from enum import Enum

class WorkStageEnum(str, Enum):
    PRE_HLD = "Pre-HLD"
    HLD_CPP = "HLD-CPP"
    IS_PP = "IS & PP"
    LLD = "LLD"
    AS_BUILT = "As Built LLD"
    GCOMS = "GCOMS"
    BCN = "BCN"

class NBUBase(BaseModel):
    nbu_no: str
    node_name: str
    child_nbu_no: str
    planner_name: str
    qa_name: Optional[str] = None
    technical_reviewer: Optional[str] = None
    total_premise_count: int
    pia_count: int
    ug_count: int
    self_dig_count: int
    l4_cabinets: int
    ug_chambers: int
    pole_dps: int
    policy_d_poles: int
    policy_poles: int
    sd_poles: int
    share_drive_link: Optional[str] = None

    @validator('total_premise_count')
    def validate_total_premise(cls, v, values):
        if 'pia_count' in values and 'ug_count' in values and 'self_dig_count' in values:
            total = values['pia_count'] + values['ug_count'] + values['self_dig_count']
            if total != v:
                raise ValueError(f'Total premise count must equal sum of PIA, UG, and Self-Dig counts (got {v}, expected {total})')
        return v

class CityBase(BaseModel):
    name: str
    stage: WorkStageEnum
    planner_name: Optional[str] = None
    qa_name: Optional[str] = None
    technical_reviewer: Optional[str] = None

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('City name cannot be empty')
        return v.strip()

class CityCreate(CityBase):
    pass

class CityUpdate(CityBase):
    name: Optional[str] = None
    stage: Optional[WorkStageEnum] = None

class NBUResponse(NBUBase):
    id: int
    city_id: int

    class Config:
        from_attributes = True

class WorkStageResponse(BaseModel):
    id: int
    stage: WorkStageEnum
    details: str
    nbus: List[NBUResponse] = []

    class Config:
        from_attributes = True

class CityResponse(CityBase):
    id: int
    work_stages: List[WorkStageResponse] = []
    nbus: List[NBUResponse] = []

    class Config:
        from_attributes = True

class CityDetailResponse(CityResponse):
    total_premises: int = Field(0, description="Total premises across all NBUs")
    total_nbus: int = Field(0, description="Total number of NBUs")
    
    @validator('total_premises', pre=True)
    def calculate_total_premises(cls, v, values):
        if 'nbus' in values:
            return sum(nbu.total_premise_count for nbu in values['nbus'])
        return 0

    @validator('total_nbus', pre=True)
    def calculate_total_nbus(cls, v, values):
        if 'nbus' in values:
            return len(values['nbus'])
        return 0

    class Config:
        from_attributes = True