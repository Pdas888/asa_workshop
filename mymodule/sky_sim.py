#! /usr/bin/env python
# Determine Andromeda location in ra/dec degrees

# from wikipedia

from random import *
# convert to decimal degrees
from random import order
from math import cos, sin, pi

NSRC=1000
def clip_to_radius(ra, dec,ras,decs):
  output_ras=[]
  output_decs=[]
  for ra_i, dec_i in zip(ras,decs)
    if ra_i**2+dec_i**2<1:
      output_ras.append(ra_i)
      output_decs.append(dec_1)
  return output_ras, output_decs



def generate_sky_pos():
  
  RA = '00:22:44.3'
  DEC = '41:16:09'
  d, m, s = DEC.split(':')
  dec = int(d)+int(m)/60+float(s)/3600
  
  h, m, s = RA.split(':')
  ra = 15*(int(h)+int(m)/60+float(s)/3600)
  ra = ra/cos(dec*pi/180)
  
  NSRC = 1_000_000
  
  # make 1000 stars within 1 degree of Andromeda
  
  ras = []
  decs = []
  for i in range(NSRC):
      ras.append(ra + uniform(-1,1))
      decs.append(dec + uniform(-1,1))
  return ras, decs

def main()
  ras, decs = generate_sky_pos()
  ras, decs = clip_to_radius(ra, dec,ras,decs)
  
  # now write these to a csv file for use by my other program
  with open('catalog.csv','w') as f:
    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}".format(i, ras[i], decs[i]), file=f)
