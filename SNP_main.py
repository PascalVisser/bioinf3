#!usr/bin/env python3

"""
Main script with argument parser
"""

__author__ = "Pascal Visser"
__version__ = 1.0

import sys
import argparse
from Implement_SNP import ImplementSnp
from ArgumentCheck import ArgCheck
from MsaAlignScore import AlignScore


def main(argv=None):
    """
    Executable part
    """
    # create command line arguments
    parser = argparse.ArgumentParser(description='Predicting the effect of a '
                                                 'given Single Nucleotide Polymorphism (SNP) in a input DNA sequence '
                                                 'based of a MSA')

    parser.add_argument('-m', '--msa', metavar='', required=True, help="The file containing the multiple sequence "
                                                                       "alignment (.msf)")
    parser.add_argument('-s', '--sequence', metavar='', required=True, help="File containing a DNA sequence to "
                                                                            "implement the SNP in (.txt)")
    parser.add_argument('-n', '--nucleotide', metavar='', required=True,
                        help="The Single Nucleotide Polymorphism (SNP) used to "
                             "predict the effect, input = (A, C, G or T)")
    parser.add_argument('-p', '--position', metavar='', required=True, help="Position where the SNP is implemented")
    argument = parser.parse_args()

    # validate arguments from the ArgumentCheck script
    x = ArgCheck.validate_nucleotide(argument.nucleotide)
    y = ArgCheck.validate_position(argument.position)
    z = ArgCheck.validate_file(argument.sequence)
    q = ArgCheck.validate_msa(argument.msa)

    # if all input arguments are valid (True), then they will be used
    if x and y and z and q == True:
        msa = argument.msa
        snp = argument.nucleotide
        position = argument.position
        input_sequence = argument.sequence

    # Arguments are used for the SPN implementation
    dna_seq = ImplementSnp.read_inputseq(input_sequence)
    snp_seq = ImplementSnp.implement(dna_seq, position, snp)
    mutated_protein = ImplementSnp.translate_dna(snp_seq)

    # msa align and score
    align, col_len = AlignScore.read_msa(msa)
    score = AlignScore.get_align_score(align, mutated_protein, col_len)
    AlignScore.write_results(score, col_len, position)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
