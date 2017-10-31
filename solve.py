#Python Imaging Library (PIL):
#The Python Imaging Library (PIL) adds image processing capabilities to your Python interpreter.
#This library supports many file formats, and provides powerful image processing and graphics capabilities.

from PIL import Image
#The Image module provides a class with the same name which is used to represent a PIL image. 
#The module also provides a number of factory functions, 
#including functions to load images from files, and to create new images.

import time
from mazes import Maze
from factory import SolverFactory

#Read command line arguments - the python argparse class is convenient here.
#The argparse module makes it easy to write user-friendly command-line interfaces.
#The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. 
#The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid args.
import argparse

def solve(factory, method, input_file, output_file):
    # Load Image
    print ("Loading Image")
    im = Image.open(input_file)

    # Create the maze (and time it) - for many mazes this is more time consuming than solving the maze
    print ("Creating Maze")
    t0 = time.time() # time starts
    maze = Maze(im)
    t1 = time.time() # time ends
    print ("Node Count:", maze.count)
    total = t1-t0
    print ("Time elapsed:", total, "\n")

    # Create and run solver
    [title, solver] = factory.createsolver(method)
    print ("Starting Solve:", title)

    t0 = time.time()
    [result, stats] = solver(maze)
    t1 = time.time()

    total = t1-t0

    # Print solve stats
    print ("Nodes explored: ", stats[0])
    if (stats[2]):
        print ("Path found, length", stats[1])
    else:
        print ("No Path Found")
    print ("Time elapsed: ", total, "\n")

    """
    Create and save the output image.
    This is simple drawing code that travels between each node in turn, drawing either
    a horizontal or vertical line as required. Line colour is roughly interpolated between
    blue and red depending on how far down the path this section is.
    """

    print ("Saving Image")
    im = im.convert('RGB')
    impixels = im.load()

    resultpath = [n.Position for n in result]

    length = len(resultpath)

    for i in range(0, length - 1):
        a = resultpath[i]
        b = resultpath[i+1]

        # Blue - red
        r = int((i / length) * 255)
        px = (r, 0, 255 - r)

        if a[0] == b[0]:
            # Ys equal - horizontal line
            for x in range(min(a[1],b[1]), max(a[1],b[1])):
                impixels[x,a[0]] = px
        elif a[1] == b[1]:
            # Xs equal - vertical line
            for y in range(min(a[0],b[0]), max(a[0],b[0]) + 1):
                impixels[a[1],y] = px

    im.save(output_file)


def main():
    sf = SolverFactory()
    
    #The first step in using the argparse is creating an ArgumentParser object:
    parser = argparse.ArgumentParser()
    
    #Filling an ArgumentParser with information about program arguments is done by making calls to the add_argument() method.
    #Generally, these calls tell the ArgumentParser how to take the strings on the command line and turn them into objects. 
    #This information is stored and used when parse_args() is called
    
    parser.add_argument("-m", "--method", nargs='?', const=sf.Default, default=sf.Default,
                        choices=sf.Choices)
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    
    #ArgumentParser parses arguments through the parse_args() method.
    #This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action. 
    #In most cases, this means a simple Namespace object will be built up from attributes parsed out of the command line:
    
    args = parser.parse_args()

    solve(sf, args.method, args.input_file, args.output_file)

if __name__ == "__main__":
    main()

