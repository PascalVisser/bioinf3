#! usr/bin/env python3

""""
Script for validating the command line arguments
"""


__author__ = "Pascal Visser"
__version__ = 1.0

import sys
import pydoc


class ArgCheck:
    """
    class with function for validating arguments
    """

    @staticmethod
    def validate_nucleotide(nucleotide):
        """
        validate a input nucleotide for being a single nucleotide
        """
        # check and valid arguments

        valid_nuc = ['A', 'C', 'G', 'T']
        nucleotide = str(nucleotide.upper())

        if len(nucleotide) >= 2:
            print("Error, nucleotide input must be 1 character")
            print("Please provide a single nucleotide")
            sys.exit()
        elif nucleotide in valid_nuc:
            pass
        elif nucleotide == 'U':
            print("Error, input is a RNA nucleotide.")
            print("Please provide a DNA nucleotide (a,c,g or t)")
            sys.exit()
        else:
            print("Error, input is NOT a nucleotide.")
            print("Please provide a DNA nucleotide (a,c,g or t)")
            sys.exit()
        return True

    @staticmethod
    def validate_position(position):
        """
        validate a position for length and being numeric
        """
        # check position
        try:
            position = int(position)
        except ValueError:
            print("\nError, value is not a (whole)number")
            print("Please input a number in stead of a character.\n")
            sys.exit()

        if position <= 0:
            print('Error, position argument is 0 or negative')
            print("Please provide a positive position argument")
            sys.exit()
        else:
            pass
        return True

    @staticmethod
    def validate_file(fileIn):
        """
        validate input file for file type and content
        """
        seq = ''
        # check valid file extension
        typecheck = str(fileIn)
        if typecheck.endswith('.txt'):
            pass
        else:
            print('Error, wrong file type')
            print('Please provide a .txt file type')
            sys.exit()

        # open file content
        with open(fileIn) as f:
            for line in f:
                line = line.strip()
                seq += line
                seq = seq.upper()

        # validate content is dna
        valid_chars = ['A', 'C', 'G', 'T']
        for char in seq:
            if char in valid_chars:
                pass
            else:
                print("Error, file content is not DNA or not valid DNA")
                print("File content might not be all nucleotides of DNA")
                sys.exit()

        return True

    @staticmethod
    def validate_msa(msa):
        """
       validate msa for being a msa
        """
        msacheck = str(msa)
        if msacheck.endswith('.msf'):
            pass
        else:
            print("Error, msa file is not the correct type (.msf)")
            print("Please provide a valid msa")
            sys.exit()

        return True


def main(argv=None):
    """
    Main Function
    """
    # returns a pydoc documentation if the user runs this module
    if len(argv) < 2:
        print(__author__)
        print(pydoc.help(__name__))
    else:
        print(argv)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
