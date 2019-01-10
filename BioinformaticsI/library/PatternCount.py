from library.Distance import hamming_distance

def pattern_count(pattern, text):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            count += 1
    return count

def pattern_positions_in_genome(pattern, genome):
    positions = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i : i + len(pattern)] == pattern:
            positions.append(i)
    return positions

# Input:  Strings pattern and genome along with an integer distance
# Output: A list containing all starting positions where pattern appears
# as a substring of genome with at most distance mismatches
def approximate_pattern_positions_in_genome(pattern, genome, distance):
    positions = []
    for i in range(len(genome) - len(pattern) + 1):
        if hamming_distance(genome[i : i + len(pattern)], pattern) <= distance:
            positions.append(i)
    return positions

# Input:  Strings pattern and text, and an integer d
# Output: The number of times pattern appears in test with at most maxMistmatches mismatches
def approximate_pattern_count(pattern, text, maxMistmatches):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hamming_distance(text[i : i + len(pattern)], pattern) <= maxMistmatches:
            count += 1
    return count 