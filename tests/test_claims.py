import sys; sys.path.insert(0, "src")
from si_nexus.claims import CLAIMS
def test_claims_have_verdicts():
    assert len(CLAIMS) >= 12
    for c in CLAIMS:
        assert c["verdict"] and c["evidence"]
def test_power_math():
    us_TWh, gdp = 4536, 29298013000000
    gw = us_TWh*1000/8760
    assert 500 < gw < 540
    assert 280e9 < gdp/100 < 320e9
def test_ratio():
    assert round(10573/4536,2) == 2.33
