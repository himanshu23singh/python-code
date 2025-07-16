# import sys


# name=sys.argv[1]
# print(name)



import argparse
parser=argparse.ArgumentParser(description="this is print my favorite color")
parser.add_argument('-c','--color',metavar='color',choices={"red","yellow"},
                   required = True, help='the color search for')
args=parser.parse_args()
print(args.color)


#A command line argument is a value or input passed to a program when it is run from the command line (terminal or command prompt).
#These arguments allow you to control the behavior of a program without changing its code.


