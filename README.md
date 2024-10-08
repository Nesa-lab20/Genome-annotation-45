# Genome-annotation-WEEK 4-5
-Create a README in a Github repository with the answers.

# 1. AMINOACIDS
-If given the amino acid sequence "KVRMFTSELDIMLSVNG-PADQIKYFCRHWT*", what is the number of amino acids in the encoded peptide (not including the stop codon)?    
Additonally, how many bases are contained in the open reading frame of the DNA sequence encoding the amino acids (including the stop codon)?    
Each amino acid is encoded by a codon (3 nucleotides), and the stop codon is also 3 nucleotides long. So, for 30 amino acids plus the stop codon,calculate the total number of bases.  

**FOR THE CODES YOU NEED TO CHANGE THE FILE PATH**

---Create a new python file to formulate the code and then run it to get the outputs    
```
nano HW3.py
python HW3.py
```
The outputs are the following:

```markdown
Number of amino acids (excluding stop codon): 30
Number of bases in the open reading frame (including stop codon): 93
```

# 2. Run prodigal on one of the genomes you have previously downloaded. Using command line tools, count how many genes were annotated (you can use any of the output formats for this but some are easier than others).

Step 2: Run Prodigal on one of your genomes. For example:GCA_000006825.1_ASM682v1_genomic.fna

```
module load prodigal 
prodigal -i GCA_000006825.1_ASM682v1_genomic.fna -d genes_GCA_000006825.1.fna -o GCA_000006825.1.gbk 
```

Step 3: Count the number of genes annotated. You can use grep to count entries:

grep ">" genes_GCA_000006825.1.fna -c > genecounts.txt

OUTPUT from genecounts.txt = 2032


# 3. Run prodigal on all of the genomes you have previously downloaded. Using command line tools, find which genome has the highest number of genes. Put all your code into a shell script, and put your code on the repository on Github where you keep your README with the solutions to this assignment (title:Prodigalrun.sh)

Step 1: Create a shell script to run Prodigal on all genomes in a directory. (Prodigalrun.sh):

Step 2: Use command-line tools to find which genome has the most genes:
```
module load prodigal
nano Prodigalrun.sh
chmod +x Prodigalrun.sh
sbatch Prodigalrun.sh
./Prodigalrun.sh

```
Genome with the highest number of genes:
File: ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna
Number of genes: 3594

# 4. Annotate all genomes you have previously downloaded using prokka instead of prodigal. Using shell commands, count the number of coding sequences (CDS) annotated by Prokka. 
```
module load prokka
nano counts_cds.sh
chmod +x counts_cds.sh
./counts_cds.sh

```
ANSWER: counts_cds.txt
```
GCA_000008525.1_ASM852v1_genomic: 1577 CDS
GCA_000008605.1_ASM860v1_genomic: 1001 CDS
GCA_000008625.1_ASM862v1_genomic: 1771 CDS
GCA_000008745.1_ASM874v1_genomic: 1058 CDS
GCA_000027305.1_ASM2730v1_genomic: 1748 CDS
GCA_000006745.1_ASM674v1_genomic: 3589 CDS
GCA_000008545.1_ASM854v1_genomic: 1861 CDS
GCA_000008565.1_ASM856v1_genomic: 3245 CDS
GCA_000008725.1_ASM872v1_genomic: 892 CDS
GCA_000008785.1_ASM878v1_genomic: 1504 CDS
GCA_000006825.1_ASM682v1_genomic: 2028 CDS
GCA_000006865.1_ASM686v1_genomic: 2383 CDS
GCA_000007125.1_ASM712v1_genomic: 3150 CDS
GCA_000091085.2_ASM9108v2_genomic: 1056 CDS
```

# Are the total number of genes the same as they were with prodigal? What are the differences?
```
PRODIGAL=Number of genes: from 897 to 3594
PROKKA= Number of coding sequences (CDS): from 892 to 3589
Not the same, the differences are that the counts from Prokka are lower, this is because Prodigal can include potential genes. But Prokka focuses on the actual and real sequences, deleting anything else from the count.
```

# 5. Extract and list all unique gene names annotated by Prokka using shell commands. Provide the command you used and the first five gene names from the list.
```
cd prokka_output/
grep -h "gene=" */*.gff | sed 's/.*gene=//; s/;.*//' | sort -u > unique_g_names.txt
head -n 5 unique_g_names.txt


```
OUTPUT
```
aaaT
aaeA
aaeA_1
aaeA_2
aaeB
```
