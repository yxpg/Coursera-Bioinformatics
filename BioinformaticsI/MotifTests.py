from library.Motif import enumerate_motifs
from library.Motif import median_string

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

#test1()
#test2()
test4()