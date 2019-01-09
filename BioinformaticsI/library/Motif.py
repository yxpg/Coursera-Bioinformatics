from library.Neighbourhood import iterative_neighbours
from library.PatternCount import hamming_distance

def enumerate_motifs(dnas, kmerLength, mismatches):
    motifs = set()
    for kmer in all_kmers(dnas[0], kmerLength):
        for neighbour in iterative_neighbours(kmer, mismatches):
            if is_in_all_dnas(dnas[1:], neighbour, mismatches):
                motifs.add(neighbour)
    return motifs

def is_in_all_dnas(dnas, kmer, mismatches):
    for dna in dnas:
        isFound = False
        for anotherKmer in all_kmers(dna, len(kmer)):
            if hamming_distance(kmer, anotherKmer) <= mismatches:
                isFound = True
                break
        if not isFound:
            return False
    return True

def all_kmers(genome, kmerLength):
    for i in range(len(genome) - kmerLength + 1):
        yield genome[i : i + kmerLength]