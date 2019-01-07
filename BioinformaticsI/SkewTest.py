from library.Skew import skew_array
from library.Skew import minimum_skew

def test1():
    genome = 'CATGGGCATCGGCCATACGCC'
    print(' '.join(str(s) for s in skew_array(genome)))

def test2():
    genome = 'GAGCCACCGCGATA'
    print(' '.join(str(s) for s in skew_array(genome)))

def test3():
    genome = 'TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'
    print(' '.join(str(p) for p in minimum_skew(genome)))

def test4():
    with open('dataset/dataset_7_6.txt') as file:
        content = file.readlines()
    genome = [line.strip() for line in content][0]   
    print(' '.join(str(p) for p in minimum_skew(genome)))

test1()
test2()
test3()
test4()