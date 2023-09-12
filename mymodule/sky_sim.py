#! /usr/bin/env python
# Determine Andromeda location in ra/dec degrees

# from wikipedia


# convert to decimal degrees
from math import cos, sin, pi


def clip_to_radius()
  pass


def generate)sky_pos()
  
  RA = '00:11:44.3'
  DEC = '41:16:09'
  d, m, s = DEC.split(':')
  dec = int(d)+int(m)/60+float(s)/3600
  
  h, m, s = RA.split(':')
  ra = 15*(int(h)+int(m)/60+float(s)/3600)
  ra = ra/cos(dec*pi/180)
  
  NSRC = 1_000_000
  
  # make 1000 stars within 1 degree of Andromeda
  from random import *
  ras = []
  decs = []
  for i in range(NSRC):
      ras.append(ra + uniform(-1,1))
      decs.append(dec + uniform(-1,1))
  
  
  # now write these to a csv file for use by my other program
  with open('catalog.csv','w') as f:
    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}".format(i, ras[i], decs[i]), file=f)
