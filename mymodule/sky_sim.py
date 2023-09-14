#! /usr/bin/env python
# Determine Andromeda location in ra/dec degrees
# changing
# from wikipedia

from random import *
import argparse
import logging
import mymodule
# convert to decimal degrees

from math import cos, sin, pi
NSRC=1000

def skysim_parser():
    """
    Configure the argparse for skysim

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-', description ="Simulate a sky")
    parser.add_argument('--ra', dest = 'ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--version', action='version', version=f'%(prog)s {mymodule.__version__}')
    
    parser.add_argument('--dec', dest = 'dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='destination for the output catalog')
    parser.add_argument('--logging', type=str, default='INFO',
                        help='Logging level from (DEBUG, INFO, WARNING, ERROR, CRITICAL)')
    
    return parser

def get_radec():
    """
    Generate the ra/dec coordinates of Andromeda
    in decimal degrees.
    Inputs
    ------
    andromeda_ra : RA of Andromeda galaxy in hh:mm:ss
    andromeda_dec: DEC of Andromeda in dd:mm:ss
    
    Returns
    -------
    ra : float
        The RA, in degrees, for Andromeda
    dec : float
        The DEC, in degrees for Andromeda
    """
    # from wikipedia
    andromeda_ra = '00:42:44.3'
    andromeda_dec = '41:16:09'

    d, m, s = andromeda_dec.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = andromeda_ra.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/cos(dec*pi/180)
    return ra,dec


def clip_to_radius(ra, dec,ras,decs, log = logging.getLogger("sky_sim")):
  output_ras=[]
  output_decs=[]
  for ra_i, dec_i in zip(ras,decs):
    if ra_i**2+dec_i**2<1:
      log.debug("within a degree")
      output_ras.append(ra_i)
      output_decs.append(dec_1)
  return output_ras, output_decs

def make_stars(ra, dec, nsrc=NSRC):
    """
    Generate NSRC stars within 1 degree of the given ra/dec

    Parameters
    ----------
    ra,dec : float
        The ra and dec in degrees for the central location.
    nsrc : int
        The number of star locations to generate
    
    Returns
    -------
    ras, decs : list
        A list of ra and dec coordinates.
    """
    ras = []
    decs = []
    for _ in range(nsrc):
        ras.append(ra + uniform(-1,1))
        decs.append(dec + uniform(-1,1))
    return ras, decs


def generate_sky_pos():
  
  RA = '00:22:44.3'
  DEC = '41:16:09'
  d, m, s = DEC.split(':')
  dec = int(d)+int(m)/60+float(s)/3600
  
  h, m, s = RA.split(':')
  ra = 15*(int(h)+int(m)/60+float(s)/3600)
  ra = ra/cos(dec*pi/180)
  

  
  # make 1000 stars within 1 degree of Andromeda
  
  ras = []
  decs = []
  for i in range(NSRC):
      ras.append(ra + uniform(-1,1))
      decs.append(dec + uniform(-1,1))
  return ras, decs
  
  

def main():
  parser = skysim_parser()
  options = parser.parse_args()
  loglevels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL
  }
  logging.basicConfig(
    format="%(name)s:%(levelname)s %(message)s",
    level=loglevels[options.logging]
  )
  log = logging.getLogger("sky_sim")

  if None in [options.ra, options.dec]:
    ra, dec = get_radec()
    log.error("No ra and dec")
  else:
    ra = options.ra
    dec = options.dec
    log.INFO("correct")
        
  ras, decs = generate_sky_pos()
  ras, decs = clip_to_radius(ra, dec,ras,decs, log=log)
  log.warning("This is warning")
  # now write these to a csv file for use by my other program
  with open(options.out,'w') as f:
      print("id,ra,dec", file=f)
      for i in range(len(ras)):
          print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
  print(f"Wrote {options.out}")
  
if __name__ == "__main__":
    main()