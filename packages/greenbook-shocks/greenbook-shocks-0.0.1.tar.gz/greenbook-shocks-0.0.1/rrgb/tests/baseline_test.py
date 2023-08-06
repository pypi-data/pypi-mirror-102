import pytest
from rrgb import RRGB
from datetime import datetime
from pytest import approx


def test_base():
    rrgb = RRGB(rr_override=True)
    shocks = rrgb.estimate_shocks()
    assert (shocks.loc[datetime(1969, 3, 4), 'rrshock'] == approx(-0.24526549, abs=1e-3)
            ) and shocks.loc[datetime(1990, 7, 3), 'rrshock'] == approx(-0.06561027210829318, abs=1e-3)
