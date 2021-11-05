Author = Pascal Visser 
studnum = 410729


Main:

A program that scores a manual implemented SNP into a given DNA file. the score is based off a msa.   




This directory contains the following files:

- SNP_main.py
- ArguentCheck.py
- Implement_SNP.py
- MsaAlignScore.py

- gene.txt
- msa2.msf


SNP_main.py:

Main python script. this script is the excecuteble for the whole program.

ArgumentCheck.py:

This script validate all the command line inputs and throws errors if a faulty argument is used.

Implement_SNP.py:

This script puts a given SPN into the input seq and translates this to a protein sequence.

MsaAlignScore.py:

Aligns and scores the MSA agianst the mutated protein seq

gene.txt:

file with a dna sequence

msa2.msf:

The multiple sequence alignment file


Useage:

The program requires 4 arguments (nucleotide, position, input dna sequence and msa file).

Nucleotide -n: a input DNA nucleotide as SNP (A,C,T or G)
Position   -p: a numeric value of where the SNP is implemented
Sequence   -s: a input .txt file with DNA nucleotides
msa        -m: a multiple sequence alignment file

help       -h: help function


Outcome:

If the program runs without errors, the outcome is how conservated a aminoacid is in a given protein family.
the score shows how the SNP affects the input sequence. 


Contact:

for more info: p.visser@st.hanze.nl    

