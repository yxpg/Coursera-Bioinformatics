from library.Distance import hamming_distance
from library.Distance import distance_between_pattern_and_strings
from library.Distance import median_string

def test1():
    p = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
    q = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
    print(hamming_distance(p, q)) 

def test2():
    p = 'GGGCCGTTGGT'
    q = 'GGACCGTTGAC'
    print(hamming_distance(p, q)) 

def test3():
    with open('dataset/dataset_9_3.txt') as file:
        content = file.readlines()
    p = [line.strip() for line in content][0]   
    q = [line.strip() for line in content][1] 

    print(hamming_distance(p, q))

def test4():
    pattern = 'AAA'
    strings = ['TTACCTTAAC', 'GATATCTGTC', 'ACGGCGTTCG', 'CCCTAAAGAG', 'CGTCAGAGGT']
    print(distance_between_pattern_and_strings(pattern, strings))

def test5():
    lines = open("dataset/dataset_5164_1-2.txt").readlines()
    pattern = lines[0]
    strings = lines[1].split()
    # print(strings)
    print(distance_between_pattern_and_strings(pattern, strings))

# test4()
test5()


