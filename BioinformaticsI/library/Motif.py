import itertools

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
