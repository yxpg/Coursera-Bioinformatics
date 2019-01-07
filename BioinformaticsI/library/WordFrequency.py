from collections import defaultdict
from library.Neighbourhood import iterative_neighbours
from library.Complement import reverse_complement

# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def frequent_words(text, patternLength):
    words = []
    frequencies = frequency_map(text, patternLength)
    maxFrequency = max(frequencies.values())
    for key in frequencies:
        if frequencies[key] == maxFrequency:
            words.append(key)
    return words

def frequency_map(text, patternLength):
    frequencies = defaultdict(int)
    length = len(text)
    for i in range(length - patternLength + 1):
        pattern = text[i : i + patternLength]
        frequencies[pattern] += 1
    return frequencies

def frequent_words_with_mistmatches(text, patternLength, mismatches):
    frequencies = frequency_map_with_mistmatches(text, patternLength, mismatches)
    maxFrequency = max(frequencies.values())
    return [word for word in frequencies if frequencies[word] == maxFrequency]  

def frequency_map_with_mistmatches(text, patternLength, mismatches):
    frequencies = defaultdict(int)
    for i in range(len(text) - patternLength + 1):
        pattern = text[i : i + patternLength]
        for neighbour in iterative_neighbours(pattern, mismatches):
            frequencies[neighbour] += 1
    return frequencies

def frequent_words_with_mistmatches_and_reverse_complements(text, patternLength, mismatches):
    frequencies = frequency_map_with_mistmatches_and_reverse_complements(text, patternLength, mismatches)
    maxFrequency = max(frequencies.values())
    return [word for word in frequencies if frequencies[word] == maxFrequency]

def frequency_map_with_mistmatches_and_reverse_complements(text, patternLength, mismatches):
    frequencies = defaultdict(int)
    for i in range(len(text) - patternLength + 1):
        pattern = text[i : i + patternLength]
        for neighbour in iterative_neighbours(pattern, mismatches):
            frequencies[neighbour] += 1
        for neighbour in iterative_neighbours(reverse_complement(pattern), mismatches):
            frequencies[neighbour] += 1             
    return frequencies

def frequent_words_with_count_with_mistmatches_and_reverse_complements(text, patternLength, mismatches):
    frequencies = frequency_map_with_mistmatches_and_reverse_complements(text, patternLength, mismatches)
    maxFrequency = max(frequencies.values())
    return [(word, frequency) for word, frequency in frequencies.items() if frequency == maxFrequency]
