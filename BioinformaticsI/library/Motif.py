import itertools
import math

from library.Neighbourhood import iterative_neighbours
from library.Distance import hamming_distance
from library.Distance import distance_between_pattern_and_strings

def enumerate_motifs(dnas, kmerLength, mismatches):
    motifs = set()
    for kmer in all_kmers_in_genome(dnas[0], kmerLength):
        for neighbour in iterative_neighbours(kmer, mismatches):
            if is_in_all_dnas(dnas[1:], neighbour, mismatches):
                motifs.add(neighbour)
    return motifs

def is_in_all_dnas(dnas, kmer, mismatches):
    for dna in dnas:
        isFound = False
        for anotherKmer in all_kmers_in_genome(dna, len(kmer)):
            if hamming_distance(kmer, anotherKmer) <= mismatches:
                isFound = True
                break
        if not isFound:
            return False
    return True

def all_kmers_in_genome(genome, kmerLength):
    for i in range(len(genome) - kmerLength + 1):
        yield genome[i : i + kmerLength]

def median_string(kmerLength, dnas):
    median = ''
    minDistance = float("inf") 
    for kmer in generate_all_kmers_with_length(kmerLength):
        distance = distance_between_pattern_and_strings(kmer, dnas)
        if distance < minDistance:
            median = kmer
            minDistance = distance
    return median

def generate_all_kmers_with_length(kmerLength):
    for kmer in itertools.product('ACGT', repeat = kmerLength):
        yield ''.join(kmer)

def greedy_motif_search(dnas, kmerLength):
    bestMotifs = [first_kmer(dna, kmerLength) for dna in dnas]
    for kmer in all_kmers_in_genome(dnas[0], kmerLength):
        motifs = [kmer]
        for j in range(1, len(dnas)):
            profile = calculate_profile(motifs[0:j])
            motifs.append(profile_most_probable_kmer(dnas[j], kmerLength, profile))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs         
    return bestMotifs      

def calculate_profile(motifs):
    rowCount = len(motifs)
    columnCount = len(motifs[0])
    profile = count(motifs)
    for symbol in profile:
        for column in range(columnCount):
            profile[symbol][column] /= rowCount
    return profile

def first_kmer(genome, kmerLength):
    return genome[0 : kmerLength]

def count(motifs):
    motifLength = len(motifs[0])
    counts = {symbol : [0] * motifLength for symbol in "ACGT"}
    for row in range(len(motifs)):
        for column in range(motifLength):
            symbol = motifs[row][column]
            counts[symbol][column] += 1             
    return counts

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
    counts = count(motifs)
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

def calculate_entropy(probabilities):
    return -sum([p * math.log(p, 2) if p != 0 else 0 for p in probabilities])
