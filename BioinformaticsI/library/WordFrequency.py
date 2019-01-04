from collections import defaultdict

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