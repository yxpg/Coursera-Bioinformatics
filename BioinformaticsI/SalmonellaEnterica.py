import time
from library.Skew import minimum_skew
from library.WordFrequency import frequent_words_with_count_with_mistmatches_and_reverse_complements

lines = open("dataset/SalmonellaEnterica.txt").readlines()

#remove the header
lines = lines[1 : -1]

# remove whitespaces in lines and merge to one line
genome = "".join(map(str.strip, lines))

t0 = time.time()
positions = minimum_skew(genome)
t1 = time.time()
print('Ori locations: ' + ' '.join(str(p) for p in positions))
print('Skew time: ' + str(t1 - t0))

patternLength = 9
mismatches = 1

ori = positions[0] # 3764856
window = 500

t2 = time.time()
mostFrequent = frequent_words_with_count_with_mistmatches_and_reverse_complements(genome[ori - window : ori + window], patternLength, mismatches)
t3 = time.time()
print(t3 - t2)
print('\n'.join(w + ' ' + str(f) for w, f in mostFrequent))