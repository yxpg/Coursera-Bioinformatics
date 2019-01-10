def hamming_distance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

def distance_between_pattern_and_strings(pattern, strings):
    totalDistance = 0
    substringLength = len(pattern)
    for string in strings:
        distance = substringLength
        for substring in all_substrings(string, substringLength):
            hammingDistance = hamming_distance(pattern, substring)
            if hammingDistance < distance:
                distance = hammingDistance
        totalDistance += distance
    return totalDistance

def all_substrings(string, substringLength):
    for i in range(len(string) - substringLength + 1):
        yield string[i : i + substringLength]
