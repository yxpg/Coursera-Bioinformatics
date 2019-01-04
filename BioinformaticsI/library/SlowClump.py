from library.SlowWordFrequency import compute_frequencies
from library.SlowWordFrequency import pattern_to_number
from library.SlowWordFrequency import number_to_pattern

def slow_find_clumps(genome, patternLength, times, clumpLength):
    frequentPatterns = []
    clumps = [0] * (4 ** patternLength)
    
    text = genome[0 : clumpLength]
    frequencyArray = compute_frequencies(text, patternLength)

    for i in range(4 ** patternLength):
        if frequencyArray[i] >= times:
            clumps[i] = 1

    for i in range(1, len(genome) - clumpLength + 1):
        firstPattern = genome[i - 1 : i + patternLength - 1]
        index = pattern_to_number(firstPattern)
        frequencyArray[index] = frequencyArray[index] - 1

        lastPattern = genome[i + clumpLength - patternLength : i + clumpLength]
        index = pattern_to_number(lastPattern)
        frequencyArray[index] = frequencyArray[index] + 1

        if frequencyArray[index] >= times:
            clumps[index] = 1

    for i in range(4 ** patternLength):
        if clumps[i] == 1:
            frequentPatterns.append(number_to_pattern(i, patternLength))
    return frequentPatterns