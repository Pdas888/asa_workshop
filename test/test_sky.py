import pytest 
from mymodule.sky_sim import get_radec, make_stars

def test_module_import():
    try:
        import mymodule.sky_sim
    except Exception as e:
        raise AssertionError("Failed to import mymodule")
    return
    
def test_get_radec_values():
  """
  This checks that get_radec gives back the correct values of Andromeda in decimal degrees
  """
  ra, dec = get_radec()
  assert ra==pytest.approx(14.215420962967535) 
  assert dec==pytest.approx(41.26916666666667)
 
 
@pytest.mark.parametrize("ra,dec,nsrc",[(14.215420962967535,41.26916666666667,200),] )
def test_make_stars(ra, dec, nsrc):
  new_ras, new_decs = make_stars(ra,dec,nsrc)
  for i in new_ras:
    assert(i-ra)<(1)
    assert(i-ra)>(-1)
  for i in new_decs: 
    assert(i-dec)<(1)
    assert(i-dec)>(-1)

