from library.PatternCount import *

def test1():
    text = 'TAATACCGAGAGACTTTCTTAATACCTCATCGGTCGAGATAATACCCGGCCGCACCTAATACCGGTGATTAATACCCCATAATACCGATAATACCTGATCGCATTAGGTAATACCTAATACCTAATACCCGCTAATACCCGGTAATACCATAATACCATAATACCCATAATACCTTAATACCGTAATACCAGTAATACCTAATACCGCTAATACCGTAATACCGGTAATACCGTAATACCAGTAATACCCTAATACCGTAATACCGACTGGCATAATACCTTAATACCGCCGGATCAATCGATTAATACCCGTTATGACTAATACCTACATAATACCACGCAGTAATACCTGGTTAATACCCTAATACCTTAATACCGTAATACCATTAATACCCTGTAATACCTTGTTAATACCTAATACCGGAGTTATAATACCTAACCGGCATAATACCTTTCGGTGATCTAGAATTAATTAATACCCTACTAATACCTAAACCTATTAATACCGGCTGTGTTAATACCAATAATACCGCTAATACCATAATACCTAATACCTAATACCGTAATACCGCGACTCGTAATACCCGTAATACCTAATACCTAATACCTAATACCTAATACCGTTTCTCATAATACCTAATACCATAATACCTAATACCGCATAATACCTAATACCATTGTTAATACCTAATACCTTAATACCATAATACCAACTAATACCGAAGCTAATACCTCCATGTAATACCGCTAATACCTAGCGCAAAGGTCCCTAATACCACTAATACCAATATAATACCTTGTAACTAATACCCGAAGCATAATACCTTCGCCTAATACCTAATACCCCCGTAATACCGTTAATACCCACAATAATACCCTAATACCAGTAATACCTACGCTGCCCATAATACCGCTAATACCGGTTAATACCACTTTAATACCGTAATACCAGTAATACCTAATACCGGATAATACCGATAATACCGTAATACCAACAGGGATAATACCGTGAA'
    pattern = 'TAATACCTA'
    print(pattern_count(pattern, text))

def test2():
    print(pattern_positions_in_genome('ATAT', 'GATATATGCATATACTT'))    

def test3():
    pattern = 'CTTGATCAT'
    with open('dataset/VibrioCholerae.txt') as file:
        content = file.readlines()
    genome = [line.strip() for line in content][0]

    print(' '.join(str(p) for p in pattern_positions_in_genome(pattern, genome)))    

def test4():
    p = 'TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC'
    q = 'GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA'
    print(hamming_distance(p, q)) 

def test5():
    p = 'GGGCCGTTGGT'
    q = 'GGACCGTTGAC'
    print(hamming_distance(p, q)) 

def test6():
    with open('dataset/dataset_9_3.txt') as file:
        content = file.readlines()
    p = [line.strip() for line in content][0]   
    q = [line.strip() for line in content][1] 

    print(hamming_distance(p, q))

def test7():
    pattern = 'ATTCTGGA'
    genome = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
    distance = 3
    print(' '.join(str(p) for p in approximate_pattern_positions_in_genome(pattern, genome, distance)))    

def test8():
    with open('dataset/dataset_9_4.txt') as file:
        content = file.readlines()
    pattern = [line.strip() for line in content][0]   
    genome = [line.strip() for line in content][1] 
    distance = int([line.strip() for line in content][2])
    print(' '.join(str(p) for p in approximate_pattern_positions_in_genome(pattern, genome, distance)))    

def test9():
    pattern = 'AAAAA'
    text = 'AACAAGCTGATAAACATTTAAAGAG'
    mismatches = 2
    print(approximate_pattern_count(pattern, text, mismatches))

def test10():
    pattern = 'GAGG'
    text = 'TTTAGAGCCTTCAGAGG'
    mismatches = 2
    print(approximate_pattern_count(pattern, text, mismatches))

def test11():
    with open('dataset/dataset_9_6.txt') as file:
        content = file.readlines()
    pattern = [line.strip() for line in content][0]   
    text = [line.strip() for line in content][1] 
    maxMistmatches = int([line.strip() for line in content][2])
    print(approximate_pattern_count(pattern, text, maxMistmatches))

#test1()
#test2()
#test3()
#test4()
#test5()
#test6()
#test7()
#test8()
#test9()
#test10()
test11()