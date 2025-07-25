import pytest
import json, sys, os
sys.path.append(os.getcwd())
from backend.simulation.month_loop import simulate
from backend.config.members import initial_members
from backend.domain.bonus import calc_bonus
from backend.simulation.params import SimParams


def test_addition():
    assert 1 + 1 == 2