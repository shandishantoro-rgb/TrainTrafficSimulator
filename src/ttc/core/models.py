from dataclasses import dataclass, field
from enum import Enum


class TrainStatus(str, Enum):
    BERJALAN = "Berjalan"
    BERHENTI = "Berhenti"
    SELESAI = "Selesai"


@dataclass(slots=True)
class Station:
    name: str
    code: str
    platform_length_m: int = 0
    track_count: int = 0
    elevation_m: float = 0.0
    region: str = ""
    description: str = ""


@dataclass(slots=True)
class Train:
    train_id: str
    name: str
    train_type: str
    status: TrainStatus
    position: str
    destination: str
    speed_kmh: float = 0.0
    delay_min: int = 0


@dataclass(slots=True)
class Project:
    name: str = "Proyek TTC"
    stations: list[Station] = field(default_factory=list)
    trains: list[Train] = field(default_factory=list)
