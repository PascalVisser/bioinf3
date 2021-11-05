#! usr/bin/env python3

"""
script for aligning and scoring the MSA
"""

__author__ = "Pascal Visser"
__version__ = 1.0

import sys
import pydoc
from Bio import AlignIO, Align


class AlignScore:
    """
    class with functions for aligning and scoring msa
    """

    @staticmethod
    def read_msa(msa):
        """
        read and align the MSA
        """
        alignment = AlignIO.read(open(msa), 'msf')
        column_len = len(alignment[:, 1])
        return alignment, column_len

    @staticmethod
    def get_align_score(alignment, snp_seq, column_len):
        """
        align the msa against the input mutated sequence and score this
        """
        scores = []

        aligner = Align.PairwiseAligner()
        for i in range(0, len(snp_seq)):
            alignments = aligner.align(alignment[:, i],
                                       snp_seq[i] * column_len)
            scores.append(alignments.score)

        return scores

    @staticmethod
    def write_results(score, column_len, pos):
        """"
        print the results to the screen based on the percentage similarity
        """

        pos = int(pos)

        if score[pos] <= 0.1 * column_len:
            message = "Very bad SNP, it has a lot of consequences!"
        elif 0.1 * column_len < score[pos] <= 0.4 * column_len:
            message = "SNP could have some bad effects, but not terrible."
        elif 0.4 * column_len < score[pos] <= 0.8 * column_len:
            message = "SNP has little or no bad effects."
        elif score[pos] > 0.8 * column_len:
            message = "SNP has no effect, silent mutation!"

        print(F"A SNP at position: {pos}, has a score:"
              F" {score[pos]} / {column_len}.\n{message}")


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


if __name__ == '__main__':
    sys.exit(main(sys.argv))
