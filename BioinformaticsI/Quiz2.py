from library.Distance import hamming_distance
from library.PatternCount import approximate_pattern_count
from library.Skew import minimum_skew
from library.Neighbourhood import iterative_neighbours

def question2():
    p = 'CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA'
    q = 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'
    print(hamming_distance(p, q))

def question3():
    genome = 'GATACACTTCCCGAGTAGGTACTG'
    print(' '.join(str(p) for p in minimum_skew(genome)))

def question4():
    pattern = 'CCC'
    text = 'CATGCCATTCGCATTGTCCCAGTGA'
    maxMistmatches = 2
    print(str(approximate_pattern_count(pattern, text, maxMistmatches)))

def question5():
    pattern = 'CCAGTCAATG'
    distance = 1
    print(len(iterative_neighbours(pattern, distance)))
   
question2()
question3()
question4()
question5()