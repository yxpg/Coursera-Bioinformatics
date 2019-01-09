from library.Motif import enumerate_motifs

def test1():
    dnas = ['ATTTGGC', 'TGCCTTA', 'CGGTATC', 'GAAAATT']
    kmerLength = 3
    mismatches = 1
    print(' '.join(str(m) for m in enumerate_motifs(dnas, kmerLength, mismatches)))

test1()