# Genome-annotation-45
Create a README in a Github repository with the answers.

1. (2 points) If given the amino acid sequence "KVRMFTSELDIMLSVNG-PADQIKYFCRHWT*", what is the number of amino acids in the encoded peptide (not including the stop codon)?

Answer: The peptide sequence has 30 amino acids (excluding the stop codon).

Additonally, how many bases are contained in the open reading frame of the DNA sequence encoding the amino acids (including the stop codon)?

    Each amino acid is encoded by a codon (3 nucleotides), and the stop codon is also 3 nucleotides long.
    So, for 30 amino acids plus the stop codon,calculate the total number of bases.

Answer: 30 amino acids * 3 bases per codon + 3 bases for the stop codon = 93 bases.

2. (2 points) Run prodigal on one of the genomes you have previously downloaded. Using command line tools, count how many genes were annotated (you can use any of the output formats for this but some are easier than others).



3. (2 points) Run prodigal on all of the genomes you have previously downloaded. Using command line tools, find which genome has the highest number of genes. Put all your code into a shell script, and put your code on the repository on Github where you keep your README with the solutions to this assignment (title:3-prodigal 14)


4. (2 points) Annotate all genomes you have previously downloaded using prokka instead of prodigal. Using shell commands, count the number of coding sequences (CDS) annotated by Prokka. Are the total number of genes the same as they were with prodigal? What are the differences?


5. (2 points) Extract and list all unique gene names annotated by Prokka using shell commands. Provide the command you used and the first five gene names from the list.


6. (Bonus: 5 points) Your task is to identify CRISPR arrays in the bacterial genomes you downloaded. Your first task is to find a tool that can be used for this task — search on Github for the right tool (hint: a name of a popular tool is CRISPRCasFinder but there are others, such as CasFinder or CRISPRFinder). Once you have found a tool, install it in your home directory. Then run the tool on your 
genomes. How many CRISPR arrays did you find?

Output the number of CRISPR arrays for each species and write the results into a 2 column file where a tab separates columns.
