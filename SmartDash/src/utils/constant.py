from enum import Enum

class WorkStageEnum(str, Enum):
    CITY_ZONING = "CITY_ZONING"
    PRE_HLD = "PRE_HLD"
    HLD_CPP = "HLD_CPP"
    IS_PP = "IS_PP"
    LLD = "LLD"
    AS_BUILT = "AS_BUILT"
    GCOMS = "GCOMS"
    BCN = "BCN"

class UserRole(str, Enum):
    SME = "SME"
    QA = "QA"

class TeamType(str, Enum):
    TEAM_A = "Team A"
    TEAM_B = "Team B"
    TEAM_C = "Team C"
    TEAM_QUALITY = "Team Quality"