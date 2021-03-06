#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tempfile   
import os
from scipy.misc import imsave,imread
import ipol.tools as tools
import subprocess
import numpy as np

string="""TV-L1 Optical Flow Estimation
Javier Sánchez Pérez, Enric Meinhardt-Llopis, Gabriele Facciolo"""

path=os.path.dirname(__file__)

exec_folder=tools.extraction_directory+'/tvl1flow_3'
source_directory=exec_folder


def tvl1flow(image1,image2,NPROCS=0,TAU=0.25,LAMBDA=0.15,THETA=0.3,NSCALES=5,ZOOM= 0.5,NWARPS=5,EPSILON=0.01,VERBOSE=1):
   """
   NPROCS is the number of processors to use (NPROCS=0, all processors available)
   TAU is the time step (e.g., 0.25)
   LAMBDA is the data attachment weight (e.g., 0.15)
   THETA is the tightness of the relaxed functional (e.g., 0.3)
   NSCALES is the requested number of scales (e.g., 5)
   ZOOM is the zoom factor between each scale (e.g., 0.5)
   NWARPS is the number of warps per iteration (e.g., 5)
   EPSILON is the stopping criterion threshold (e.g., 0.01)
   VERBOSE is for verbose mode (e.g., 1 for verbose)
   """

   #saving input image to a temporary file
  
   
   temp_image1_file =tempfile.mkstemp('.PNG')[1]
   temp_image2_file =tempfile.mkstemp('.PNG')[1]
   output_file=tempfile.mkstemp('.flo')[1]
   imsave(temp_image1_file,image1)
   imsave(temp_image2_file,image2)
   
   command=exec_folder+'/tvl1flow %s %s %s %d %f %f %f %d %f %d %f %d'%(temp_image1_file,temp_image2_file,output_file,NPROCS,TAU,LAMBDA,THETA,NSCALES,ZOOM,NWARPS,EPSILON,VERBOSE)
      
   # calling the executable
   os.system( command)   
   #reading the output from the temporary file
   flow=np.fromfile(output_file,dtype=np.float32)[3:].reshape(image1.shape[0],image1.shape[1],2)
   
  
   os.remove(output_file)
   
   os.remove(temp_image1_file)
   os.remove(temp_image2_file)
   return flow


if __name__ == '__main__':
   import sys 
   if 'install' in sys.argv:
      _install()





