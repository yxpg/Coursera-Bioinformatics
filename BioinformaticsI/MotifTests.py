from library.Motif import enumerate_motifs
from library.Motif import median_string
from library.Motif import profile_most_probable_kmer
from library.Motif import greedy_motif_search

def test1():
    dnas = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
    kmerLength = 3
    mismatches = 1
    print(' '.join(str(m) for m in enumerate_motifs(dnas, kmerLength, mismatches)))

def test2():
    dnas = [
        'TGACTTCTGACCCGGTGGAAGCACG',
        'CGAATTGCTTGCTGATAGACGTAAG',
        'CGACTTTTTGACTGACCAGAGAGTA',
        'ACTGACTCTGTAATACACCCTATCC',
        'GCCATCTGCCCAGATACTGAAGTAA',
        'GCTGATTATGCAGAGATGTTCGCCC'
    ]
    kmerLength = 5
    mismatches = 1
    print('\n'.join(str(m) for m in enumerate_motifs(dnas, kmerLength, mismatches)))

def test3():
    kmerLength = 3
    dnas = ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
    print(median_string(kmerLength, dnas))

def test4():
    kmerLength = 6
    dnas = [
        'CTGGACCAATGGGATCCGACTGTATCTAGTTCATCTAAGCCT',
        'CAATCTTCCAACAGACGTCAATGGATGAGCGATGCCGACCCT',
        'CAATAGCTAAATTTAGGCGAGACGACGGAGCGATATAATCGC',
        'AGGTTTCAATCGATTACTGGCCACTTTGCCCGAAAAGCGCGT',
        'TAAATGAAGTTGGCGGCGGACTCTATCACCCTGAATCAATCG',
        'CGAGGCGAGCCTAGGCGACTGGCGCCAAATCAATTGGGCCTG',
        'GTACCGCCACTATGTTAGCTTGCTGGTTCTCAATCGTAATTG',
        'CGGGTTCCAAAGCCTTTTGCATCGCGATGTATGTTCCAATAG',
        'GTTAAGGAGCCTCAATTGTCCGACATCTTCGATTAGCTTAGA',
        'AACCGGTATGCGAGATAGATCAACCATAGGTCATCTCAATTG'
    ]
    print(median_string(kmerLength, dnas))

def test5():
    genome = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    kmerLength = 5
    profile = {
        'A' : [0.2, 0.2, 0.3, 0.2, 0.3],
        'C' : [0.4, 0.3, 0.1, 0.5, 0.1],
        'G' : [0.3, 0.3, 0.5, 0.2, 0.4],
        'T' : [0.1, 0.2, 0.1, 0.1, 0.2]   
    }
    print(profile_most_probable_kmer(genome, kmerLength, profile))

def test6():
    with open('dataset/dataset_159_3.txt') as file:
        content = file.readlines()
    genome = [line.strip() for line in content][0]
    kmerLength = int([line.strip() for line in content][1])
    profile = {
        'A' : string_to_list(content[2]),
        'C' : string_to_list(content[3]),
        'G' : string_to_list(content[4]),
        'T' : string_to_list(content[5])   
    }
    print(profile_most_probable_kmer(genome, kmerLength, profile))

def test7():
    kmerLength = 3
    dnas = [
        'GGCGTTCAGGCA',
        'AAGAATCAGTCA',
        'CAAGGAGTTCGC',
        'CACGTCAATCAC',
        'CAATAATATTCG'      
    ]
    print('\n'.join(m for m in greedy_motif_search(dnas, kmerLength)))

def test8():
    with open('dataset/greedy_motif_input.txt') as file:
        content = file.readlines()
    kmerLength = int((content[0].split())[0])
    dnas = [line.strip() for line in content[1:]]
    result = greedy_motif_search(dnas, kmerLength)

    print('\n'.join(m for m in result))    

def string_to_list(string):
    return [float(e) for e in string.split()]

# test1()
# test2()
# test3()
# test4()
# test5()
# test6()
# test7()
test8()