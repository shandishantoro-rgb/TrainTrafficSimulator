from ttc.core.models import Project, Station
from ttc.core.simulation import SimulationController, SimulationState


def test_project_can_hold_station():
    p = Project()
    p.stations.append(Station("Gambir", "GMR"))
    assert p.stations[0].code == "GMR"


def test_simulation_state_cycle():
    s = SimulationController()
    assert s.state == SimulationState.SIAP
    s.start(); assert s.state == SimulationState.BERJALAN
    s.pause(); assert s.state == SimulationState.JEDA
    s.reset(); assert s.state == SimulationState.SIAP
