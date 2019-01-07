from library.PatternCount import hamming_distance

NUCLEOTIDES = ['A', 'T', 'C', 'G']

def immediate_neighbours(pattern):
    neighbourhood = {pattern}
    for pos, symbol in enumerate(pattern):
        for nucleotide in NUCLEOTIDES:
            if nucleotide != symbol:
                neighbourhood.add(pattern[:pos] + nucleotide + pattern[pos + 1:])
    return neighbourhood

def neighbours(pattern, distance):
    if distance == 0:
        return set(pattern)
    if len(pattern) == 1:
        return 'A', 'T', 'C', 'G'
    neighbourhood = set()
    suffix = pattern[1:]
    suffixNeighbours = neighbours(suffix, distance)
    for neighbour in suffixNeighbours:
        if hamming_distance(suffix, neighbour) < distance:
            for nucleotide in NUCLEOTIDES:
                neighbourhood.add(nucleotide + neighbour)
        else:
            neighbourhood.add(pattern[0] + neighbour)
    return neighbourhood

def iterative_neighbours(pattern, distance):
    neighbourhood = {pattern}
    for _ in range(distance):
        localNeighbourhood = set()
        for neighbour in neighbourhood:
            localNeighbourhood |= immediate_neighbours(neighbour)
        neighbourhood |= localNeighbourhood
    return neighbourhood