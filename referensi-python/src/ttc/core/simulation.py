from dataclasses import dataclass
from enum import Enum


class SimulationState(str, Enum):
    SIAP = "Siap"
    BERJALAN = "Berjalan"
    JEDA = "Jeda"
    BERHENTI = "Berhenti"


@dataclass
class SimulationController:
    state: SimulationState = SimulationState.SIAP
    speed_factor: float = 1.0
    simulated_seconds: int = 0

    def start(self) -> None:
        self.state = SimulationState.BERJALAN

    def pause(self) -> None:
        if self.state == SimulationState.BERJALAN:
            self.state = SimulationState.JEDA

    def stop(self) -> None:
        self.state = SimulationState.BERHENTI

    def reset(self) -> None:
        self.state = SimulationState.SIAP
        self.simulated_seconds = 0
