from Bio import Entrez, SeqIO

# Set your email address for NCBI to contact you
Entrez.email = "your.email@example.com"

# Set the search term for NCBI to retrieve the sequences
search_term = "protein"

# Use the E-utilities to search for the sequences
handle = Entrez.esearch(db="protein", term=search_term, retmax=100)

# Parse the search results
record = Entrez.read(handle)
id_list = record["IdList"]

# Use the E-utilities to retrieve the sequences using the list of IDs
handle = Entrez.efetch(db="protein", id=id_list,
                       rettype="fasta", retmode="text")

# Parse the sequences using BioPython
records = list(SeqIO.parse(handle, "fasta"))

# Print the first 10 sequences for demonstration purposes
for i in range(10):
    print(f">{records[i].id}\n{records[i].seq}\n")
