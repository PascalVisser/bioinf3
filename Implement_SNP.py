#! usr/bin/env python3


"""
Script which implement a given SNP into the input DNA sequence
and translates the DNA to a protein
"""

__author__ = "Pascal Visser"
__version__ = 1.0

import sys
import pydoc

translation_table = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                     "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                     "UAU": "Y", "UAC": "Y", "UAA": "_", "UAG": "_",
                     "UGU": "C", "UGC": "C", "UGA": "_", "UGG": "W",
                     "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                     "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                     "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                     "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                     "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                     "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                     "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                     "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                     "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }


class ImplementSnp:
    """
    class with functions for implementing a SNP in a given DNA sequence,
    also transforming the dNA to protein
    """

    @staticmethod
    def read_inputseq(inputseq):
        """
        Reads the input DNA sequence, checks if it is a triplet of three
        and cast it to upper, returns the sequence in a string
        """
        seq = ''

        with open(inputseq) as f:
            for line in f:
                line = line.strip()
                seq += line

        if len(seq) % 3 == 0:
            pass
        else:
            print("Error. DNA is not triplet of three")
            print("DNA must be a triplet of three")
            sys.exit()

        seq = seq.upper()

        return seq

    @staticmethod
    def implement(seq, pos, snp):
        """
        Method that implements the SNP at a given position in the input seq
        """
        # format variables
        pos = int(pos) - 1
        snp = snp.upper()

        # checks if input position exists in the file otherwise throw error
        if pos > len(seq):
            print("Error, position is out of range")
            print("Please provide a position that is in the DNA sequence (Position < {})".format(len(seq)))
            sys.exit()
        else:
            pass

        # replaces nucleotide in sequence with snp
        imp_seq = seq[:pos] + snp + seq[pos+1:]

        return imp_seq

    @staticmethod
    def translate_dna(seq):
        """
        translates the DNA sequence to a protein sequence
        """
        proteins = ''
        rna_seq = seq.replace("T", "U")
        for i in range(0, len(rna_seq), 3):
            codon = rna_seq[i:i + 3]
            proteins += translation_table[codon]
        return proteins


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
