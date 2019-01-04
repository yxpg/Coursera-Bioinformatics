def pattern_count(pattern, text):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i : i + len(pattern)] == pattern:
            count += 1
    return count

pattern = 'CGCG'
text = 'CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC'

print(pattern_count(pattern, text))

def frequent_words(text, patternLength):
    words = []
    frequencies = frequency_map(text, patternLength)
    maxFrequency = max(frequencies.values())
    for key in frequencies:
        if frequencies[key] == maxFrequency:
            words.append(key)
    return words

def frequency_map(text, patternLength):
    frequencies = {}
    length = len(text)
    for i in range(length - patternLength + 1):
        pattern = text[i : i + patternLength]
        if pattern in frequencies:
            frequencies[pattern] += 1
        else:
            frequencies[pattern] = 1
    return frequencies

text = 'TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
patternLength = 3

print(' '.join(str(p) for p in frequent_words(text, patternLength)))

def reverse_complement(pattern):
    return complement(reverse(pattern))

def reverse(pattern):
    return pattern[::-1]

def complement(pattern):
    reverse = ''
    for char in pattern:
        if char == 'A':
            reverse += 'T'
        elif char == 'T':
            reverse += 'A'
        elif char == 'C':
            reverse += 'G'
        else:
            reverse += 'C'
    return reverse

text = 'GATTACA'
print(reverse_complement(text))


def pattern_positions_in_genome(pattern, genome):
    positions = []
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i : i + len(pattern)] == pattern:
            positions.append(i)
    return positions

pattern = 'ATA'
genome = 'GACGATATACGACGATA'
print(' '.join(str(p) for p in pattern_positions_in_genome(pattern, genome)))