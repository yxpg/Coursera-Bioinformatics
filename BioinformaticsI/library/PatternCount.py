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