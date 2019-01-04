SYMBOL_TO_NUMBER = { 'A' : 0, 'C' : 1, 'G' : 2, 'T' : 3 }
NUMBER_TO_SYMBOL = { 0 : 'A', 1 : 'C', 2 : 'G', 3 : 'T' }

def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    return 4 * pattern_to_number(pattern[:-1]) + SYMBOL_TO_NUMBER[pattern[-1]]

def number_to_pattern(number, length):
    if (length == 0):
        return NUMBER_TO_SYMBOL[0]
    pattern = [NUMBER_TO_SYMBOL[0]] * length
    for i in range(length - 1, -1, -1):
        pattern[i] = NUMBER_TO_SYMBOL[number % 4]
        number //= 4
    return ''.join(pattern)

def compute_frequencies(text, patternLength):
    frequencyArray = [0] * (4 ** patternLength)
    for i in range (len(text) - patternLength + 1):
        pattern = text[i : i + patternLength]
        number = pattern_to_number(pattern)
        frequencyArray[number] += 1
    return frequencyArray  

def frequent_words_by_frequency_array(text, patternLength):
        mostFrequentPatterns = []
        frequencyArray = compute_frequencies(text, patternLength)
        maxFrequency = max(frequencyArray)
        for index, frequency in enumerate(frequencyArray):
            if frequency == maxFrequency:
                mostFrequentPatterns.append(number_to_pattern(index, patternLength))
        return mostFrequentPatterns       

def frequent_words_by_sorting(text, patternLength):
        mostFrequentPatterns = []
        numberOfPatterns = len(text) - patternLength + 1
        patternIndeces = [None] * numberOfPatterns
        patternCounts = [None] * numberOfPatterns

        for i in range(numberOfPatterns):
            pattern = text[i : i + patternLength]
            patternIndeces[i] = pattern_to_number(pattern)
            patternCounts[i] = 1

        sortedPatternIndeces = sorted(patternIndeces)
        for i in range(1, numberOfPatterns):
            if sortedPatternIndeces[i] == sortedPatternIndeces[i - 1]:
                patternCounts[i] = patternCounts[i - 1] + 1

        maxCount = max(patternCounts)
        for i in range(numberOfPatterns):
            if patternCounts[i] == maxCount:
                mostFrequentPatterns.append(number_to_pattern(sortedPatternIndeces[i], patternLength))
        return mostFrequentPatterns 