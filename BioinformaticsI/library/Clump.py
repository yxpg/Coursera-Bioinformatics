from library.WordFrequency import frequency_map

def find_clumps(genome, patternLength, times, clumpLength):
    frequentPatterns = set()
    frequencies = frequency_map(genome[0 : clumpLength], patternLength)

    for pattern in frequencies:
        if frequencies[pattern] >= times:
            frequentPatterns.add(pattern)   

    for i in range(1, len(genome) - clumpLength + 1):
        firstPattern = genome[i - 1 : i + patternLength - 1]
        frequencies[firstPattern] -= 1

        lastPattern = genome[i + clumpLength - patternLength : i + clumpLength]
        frequencies[lastPattern] += 1

        if frequencies[lastPattern] >= times:
            frequentPatterns.add(lastPattern)

    return frequentPatterns