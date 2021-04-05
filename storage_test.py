import os
import sys, getopt
import time
import datetime
from time import sleep


def main(argv):
   # read arguments
   seconds = 0
   iterations = 0
   outputfile = ''

   try:
      opts, args = getopt.getopt(argv,"hi:s:o:",["iterations=","seconds=","output="])
   except getopt.GetoptError:
      print ("storage_test.py -i <iterations> -s <seconds> -o <output>")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("storage_test.py -i <iterations> -s <seconds> -o <output>")
         sys.exit()
      elif opt in ("-i", "--iterations"):
         iterations = int(arg)
      elif opt in ("-s", "--seconds"):
         seconds = int(arg)
      elif opt in ("-o", "--output"):
         outputfile = arg

   ts = time.time()
   starttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S')

   #summary of the input parameters
   print("********************************\n")
   print("Starting test for storage file %s writing\n" % outputfile)
   print("Number of iterations: %d\n" % iterations)
   print("Waiting seconds: %d\n" % seconds)
   totseconds = int(iterations*seconds)
   totminutes = int(totseconds/60)

   print("Total expected execution time: %d seconds\n" % totseconds)
   print("Total expected execution time: %d minutes\n" % totminutes)

   f=open(outputfile,"a+")


   #start of the iterations
   for i in range(iterations):
      ts = time.time()
      sttime = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H:%M:%S - ')
      print(sttime + "iteration number: %d\n" % (i+1))
      f.write(sttime + "iteration number: %d\n" % (i+1))
      sleep(seconds)
   f.close()


if __name__== "__main__":
  main(sys.argv[1:])
