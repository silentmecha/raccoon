import sys ,getopt
import discord
import pynxm

# how to read arguments from commandline into program.
# will need to do some syntax fixing so as to read "arg=key" where key is unknown


def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print(f'test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print(f'test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print(f'Input file is "', inputfile)
   print(f'Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])