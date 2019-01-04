from library.PatternCount import pattern_count
from library.PatternCount import pattern_positions_in_genome
from library.WordFrequency import frequent_words
from library.Complement import reverse_complement

def question2():
    pattern = 'CGCG'
    text = 'CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC'
    print(pattern_count(pattern, text))

def question3():
    text = 'TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT'
    patternLength = 3
    print(' '.join(str(p) for p in frequent_words(text, patternLength)))

def question4():
    text = 'GATTACA'
    print(reverse_complement(text))

def question5():
    pattern = 'ATA'
    genome = 'GACGATATACGACGATA'
    print(' '.join(str(p) for p in pattern_positions_in_genome(pattern, genome)))

question2()
question3()
question4()
question5()