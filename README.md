# Genome-annotation-WEEK 4-5
-Create a README in a Github repository with the answers.

# 1. 
-If given the amino acid sequence "KVRMFTSELDIMLSVNG-PADQIKYFCRHWT*", what is the number of amino acids in the encoded peptide (not including the stop codon)?
Create a new python file to formulate the code and then run it to get the outputs
```
nano HW3.py
python HW3.py

```
The outputs are the following:
```markdown
Answer: The peptide sequence has 30 amino acids (excluding the stop codon).
```
Additonally, how many bases are contained in the open reading frame of the DNA sequence encoding the amino acids (including the stop codon)?

Each amino acid is encoded by a codon (3 nucleotides), and the stop codon is also 3 nucleotides long. So, for 30 amino acids plus the stop codon,calculate the total number of bases.
```
Answer: 30 amino acids * 3 bases per codon + 3 bases for the stop codon = 93 bases.
```

# 2. Run prodigal on one of the genomes you have previously downloaded. Using command line tools, count how many genes were annotated (you can use any of the output formats for this but some are easier than others).

Step 2: Run Prodigal on one of your genomes. For example:

./prodigal -i genome.fasta -a proteins.faa -d nucleotides.fna -o prodigal_output.gbk

Step 3: Count the number of genes annotated. You can use grep to count entries:

grep -c '>' prodigal_output.gbk

# 3. Run prodigal on all of the genomes you have previously downloaded. Using command line tools, find which genome has the highest number of genes. Put all your code into a shell script, and put your code on the repository on Github where you keep your README with the solutions to this assignment (title:3-prodigal 14)

Step 1: Create a shell script to run Prodigal on all genomes in a directory. (run_prodigal14.sh):

#!/bin/bash
for genome in /path/to/genomes/*.fasta; do
    ./prodigal -i $genome -o $(basename $genome .fasta)_prodigal_output.gbk
done

Step 2: Use command-line tools to find which genome has the most genes:

bash

for file in *_prodigal_output.gbk; do
    count=$(grep -c '>' $file)
    echo "$file: $count genes"
done | sort -k2,2nr | head -1

# 4. Annotate all genomes you have previously downloaded using prokka instead of prodigal. Using shell commands, count the number of coding sequences (CDS) annotated by Prokka. Are the total number of genes the same as they were with prodigal? What are the differences?


# 5. Extract and list all unique gene names annotated by Prokka using shell commands. Provide the command you used and the first five gene names from the list.


# BONUS 6. Your task is to identify CRISPR arrays in the bacterial genomes you downloaded. Your first task is to find a tool that can be used for this task — search on Github for the right tool (hint: a name of a popular tool is CRISPRCasFinder but there are others, such as CasFinder or CRISPRFinder). Once you have found a tool, install it in your home directory. Then run the tool on your genomes. How many CRISPR arrays did you find?
Output the number of CRISPR arrays for each species and write the results into a 2 column file where a tab separates columns.


