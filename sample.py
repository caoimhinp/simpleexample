#!/usr/bin/env python

"""
Example of basic python application format
"""

import os
import sys

def say_hello():
    print "Hello, now read the rest of the code"

def main():
    print "Now we're in the main function."
    print "We don't have to be in a main function though."
    print "People just do this to organize their code."
    
if __name__ == "__main__":
    main()
    print "We're now out of the main function"
    print "This works just as well."
    
    # Oh, yeah... say hello
    say_hello()
    
    sys.exit()
