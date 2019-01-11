# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    return greedy_motif_search_with_pseudocounts(Dna, k)

def greedy_motif_search_with_pseudocounts(dnas, kmerLength):
    bestMotifs = [first_kmer(dna, kmerLength) for dna in dnas]
    for kmer in all_kmers_in_genome(dnas[0], kmerLength):
        motifs = [kmer]
        for j in range(1, len(dnas)):
            profile = calculate_profile_with_pseudocounts(motifs[0:j])
            motifs.append(profile_most_probable_kmer(dnas[j], kmerLength, profile))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs         
    return bestMotifs 

def calculate_profile_with_pseudocounts(motifs):
    rowCount = len(motifs) + 4
    columnCount = len(motifs[0])
    profile = count_with_pseudocounts(motifs)
    for symbol in profile:
        for column in range(columnCount):
            profile[symbol][column] /= rowCount
    return profile

def count_with_pseudocounts(motifs):
    motifLength = len(motifs[0])
    counts = {symbol : [1] * motifLength for symbol in "ACGT"}
    for row in range(len(motifs)):
        for column in range(motifLength):
            symbol = motifs[row][column]
            counts[symbol][column] += 1             
    return counts

def first_kmer(genome, kmerLength):
    return genome[0 : kmerLength]

def all_kmers_in_genome(genome, kmerLength):
    for i in range(len(genome) - kmerLength + 1):
        yield genome[i : i + kmerLength]
        
def profile_most_probable_kmer(genome, kmerLength, profile):
    maxProbability = -1
    mostProbableKmer = ''
    for kmer in all_kmers_in_genome(genome, kmerLength):
        probability = calculate_probability(kmer, profile)
        if probability > maxProbability:
            mostProbableKmer = kmer
            maxProbability = probability
    return mostProbableKmer
        
def calculate_probability(text, profile):
    probability = 1
    for i, symbol in enumerate(text):
        probability *= profile[symbol][i]
    return probability

def score(motifs):
    consensus = consensus_string(motifs)
    return sum([hamming_distance(consensus, motif) for motif in motifs])

def consensus_string(motifs):
    motifLength = len(motifs[0])
    counts = count_with_pseudocounts(motifs)
    consensus = ""
    for column in range(motifLength):
        maxCount = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if counts[symbol][column] > maxCount:
                maxCount = counts[symbol][column]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def hamming_distance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance