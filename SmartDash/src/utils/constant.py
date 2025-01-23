from enum import Enum

class WorkStageEnum(str, Enum):
    CITY_ZONING = "City Zoning"
    PRE_HLD = "Pre-HLD"
    HLD_CPP = "HLD-CPP Submission"
    IS_PP = "IS & PP Submission"
    LLD = "LLD Submission"
    AS_BUILT = "As Built LLD"
    GCOMS = "GCOMS"
    BCN = "BCN activity"

class UserRole(str, Enum):
    SME = "SME"
    QA = "QA"

class TeamType(str, Enum):
    TEAM_A = "Team A"
    TEAM_B = "Team B"
    TEAM_C = "Team C"
    TEAM_QUALITY = "Team Quality"