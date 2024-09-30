# Given amino acid sequence
amino_acid_sequence = "KVRMFTSELDIMLSVNG-PADQIKYFCRHWT*"

# Count the number of amino acids (excluding the stop codon)
# Remove the stop codon symbols ('-' and '*')
cleaned_sequence = amino_acid_sequence.replace("-", "").replace("*", "")
num_amino_acids = len(cleaned_sequence)

# Each amino acid is encoded by 3 nucleotides (codons)
# Adding 3 for the stop codon
num_bases_in_ORF = len(cleaned_sequence) * 3 + 3

print("Number of amino acids (excluding stop codon):", num_amino_acids)
print("Number of bases in the open reading frame (including stop codon):", num_bases_in_ORF)
