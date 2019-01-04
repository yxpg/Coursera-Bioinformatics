from library.Complement import reverse_complement

def test1():
    print(reverse_complement('AAAACCCGGT'))

def test2():
    text = 'AACATCGCGTGTGACCCTAAGCTAAAGTCTGTCAATGGAACAAAGAAGGTTTCGTTGAGGAATGCGGTCTTTCAAGCGATCGGGAACAAAGCACCTCAATACATAGGGAGTCGCTATGCAACCTGTAACCGCGCTTACCCATGGATACTTCATAGCGGAACATCACTCGGTGCGAGGGGACTTGCCTTTCATGGTGGGAGCAACTCAAGTGTCCTTATAATTCACATAACGTTGATCGACAGGCCCTGAGAGCGCAGGCCAACAGTATATTCGCAACCAGACATGCTCGGCCACTAACATATTCCTTTAGAGTCGCTACCCAACAAGGACCACGTTAGGCCTTGTTGACAGTTGTTAAGATAAATTGCCTTAGTTACTAGACGCCGAACATATGTATGACCGTCATGAAGCGCCGCATTGGTTGGGGCGTATCAGATCCGTAAGTGCGGCTTTCGCGAAGCCAACCCTGGGTGTAAGGCTGTTGCGCGACTCTGTGGCGCCTGTCGTTCAGTTTATCGTGTCGGGAAGATTCTGGTGTGAACGCCGGTCTAGCTGCGCGGGCATCGACATGCTATTTAGATTACCTATACCCGTGAATGGCCCTACACGAAGGCTGGGACGTAAATCTGCATCATCAGGTTAGAGCTCCGAGGCGTTCCCTCATAACGCGTTTCAACAGTGTGCGCCAGGAATTATTGCCACCAAAAGGGGCTCTCAAGCATAGTTCCATTAACAAGCCGGGGGTTTAATACGCTGGTCGCCACGTCGTGCCTTCTATTAACAGAATGAGTCGTCGAAGCCTAAGAGAGTCTAACGCCCCCGCCAATACTAAAGTTGGGAATGCATCGATACCTAGACGAGTCATATGTACGGCATGATTGGACGGCAAGTTACGATTCGCGCTGGGTACCGCTTCGCAGACGGTGAGGAGAGTGACCTCATGTCTCGGAATATATGGCGATCCACGTGCACTCGCATAAGACTGCGGGGGCTCATTGGGCTTACCAATACTAGCCGTATACGGAAGACACTTAAGGGTTAACCGCATACTGTCATGGTCGGCGCTCGGAGTTTTACTATAATGAAACTGGCCTTCTCGGATTTCTTCAGCGCCCTACCCACGATCTTATCAATTACTTTCGAAGTGCAATCAGAAAGATGTTCGACAATTCACTTAACAAACTACAGCATCAAACGTGTCGCGCTGACTTTTGGAGCCGGCCTGCAGTAATCCAGTAGGAAGATGTGTGACCCAACACCAATTACAGACGGCTCTTGTAGACGGCTGGAACCATTGGTCGTCCCTCGGGTCCATGCGGTTATACCGCACTCGGTAACAAAGAATATGGTTCAGCCTGAATGAAGTTAGGGCTAATCGTGGTAGGTATAAACATCAATAAATGTCCGTGATAGGTCCATAAGTACCCCGTTAGTTCTGCAGGATTCGCCACCGACCATCGTACTAGTGTTGCCAGTAGTAGGAAATTTCACATGAGCATGACTTGCGATTCCCCCAGTCGGCCGTGAGTTCCAGTATACAAGCCCGCGCGCCGCGTTGAATGGCGCACGCTCCACGACGTACTCTTTTCCCGCACATGCTGAGTATCACTATTCTCAGGTGGAGTCCACGTTTTCCATGAATTTACAGGTACTGCCTCGCCGTGTCAGTCCACTCGGGTAATGCGATGAGTGTAGTCCAATAGCAACTCGACTAATAAGTGACTCGATACCTTTTTTGTAATGACTCGCAGGATATCGGGGAATCTAAGTAAGCCGTCATATTCTACAGGCTATTTTACCCTCATATTTTGGAGACTAGACCCAAAGAGTCACAACCTACAAGCCCGTGACCCCGTCTTTCACTGGCGCCTCGTTGTACGGGCTATCCCTTTTACGTAGTGAATTATTAGCTACTGGTGGTCCGCTGTGATTGTACCATGGGTCGCTGCGCATTGCTTCCCTACGCCATTGGGGATGGAGATGTCTTAATTTGGTTATGTTCTATGTTCCGTGTTGCAAAAATCATCACAGACTAGGAACCCATGACAGACGACTGGTCATCTGATAACTGTGTGCCGAAATTGCGCGTTGGGTCGCTGATGACGCTTCGGACGAAGGTATGGGGGAAGAGGCCGTCTCATTTGATAGGTTCAGTGCGATTGCGGAGTCTATCTCGCGCGTAAAGAACGAGAAATAGATTGTAGCATGTGTGTGATGTCAGCTGTAACTGCTCAATTGATAATCTGTCCATCGCACTATTATCTCCCCCTCAATTCATACAAATGTAGTGCCGCAGGTACCGGAATAAACGTCCCCTAATTTTCTAGAAAAATGCACGGTCCCTCAGTTGCTAGTGGCAGGAGTTTCCACAGCTGGTACTGCATAGGGAGTAGGTGGAAGCCTTTTACGACTGGGATTCTGTCTTTGTGGAAGTGAGCTCAAGACGACACATGGATATCAGGAGAGCCCTCTCTATAAGATTAACATCGCCTGCCCGTGTGGCGTATCATGAGCGATTAGTATCTAGTTCCTCCGCCCGAGGCGGGAAAGTCCAGTGCAGGTGTTGTTGGTACTCGAGAAGCTCGCTAACGTCATAAATTAGTTACGTAGCTAGCGCGAGCGAATAGCCAGGATGCGCTATGAGCTAAACAAGCTTAGTGGTGATCGATCTCACATGGGTACGGAGGGAACACTCTGGATATTAACTTGTGGAAGAATTTTGGAACGCATTAGGGACCGCGGGGAAAAGCGGCAAGGCACCGCCAAGCCTACGATAGCACTACCAAACGCCATTCACCCATCTGCCCAGTCTGGCGCGCCGGCAGACTCCTCAACGGAGTAACACTAAAGTGCAACAGCGGGCCCTAATTTTGTACTGTCGGAGTACACCCGGATGTATGATAGTATTCCCGAACCATTCTTATGAATCAGAATCGGCTATCGGATGGGAAAGATACCTCAAGGTTCCATGCTTTCCGCTAAGAAGGGTCTAAGTTCAAACGATGTTGTGGATGAACTCGCCTCATCACTCAACAAGTGTCAACGTGCCCTAAGAGAGGCCAGCAGAAGTGCACAAGAGGGTCAGGAACACTAGACGGACTGGATCCTCGTATGTCCGTAAGCTGGGGACGGCCTACACTAGTAACATCACAAAAGTCTCGAGCCTTTCTGTCATTCGTCGACATCAGTTACTGTAGTAAGTGACCCGGGCTTCCCGGTATTTGCATCCTAGTAGGAGAGTGAAATGAGCCTCAACGGTACCATGAATCCGCAAACTTAGACGAGTAGGTAAAGTCATCCAGTCCGGCGCTTACGACCTGTCCCGTATATACGTATTTCCGTATTAGGTGGTTTTCAGATGGCGATCAAAAGGACTGTCGCTCTAGGGGCGGCACCAGCTCCACATAGCATCGAGGCGATAGACCAACTGTCACTGACTAACGCTTGGCACCAACTAGTGCCCTATCATGCTGATTTGCGATTACCTTTTGTCCTAAGAGAGCCTGCACGTTGTTTGTGGCACAAGGGGATCTGGTGGATAGCTACGCGGTACCGGGATGGAATCACCGCAATAACAGGGTTTATCCATCCCGGTGACTGCGTCGCGAATCCTGGGCATGCACAAGAGCCTCGCAGTTCAATTCACTGAGCCAATCATGGTAATTACCCCTCATTCTCGCTCTCCGAAGATGATGCGAGAGTATATACGGGCGAAATTACCCCGGGACATCCCAGCTAGCATCCTTTGTGATCGCAATAACTAGGCTCCTTTTACCTCTATTTTCTCTATGCGGATGGAGATCGAAGTGTGGAGAGACTTTTACACCATTCCCATAAAGCGCGTAAACCGGAACGATGTGACCATATACGGGTGGACGGAGTAGTCAAGATCCGTGTCCAACTTAGGATAACCTTGGGCAGCGAGTAGCTGCGTAACTTCTTGGTGCGCAAGTGGGGTAACGGGCGCTGAGCTGTCGAGTGCGTCTGGGAGGACGCATCGGACGGAATGCAGACCTGGATCTCGTCGCGCTAACCTGCAGGTTCTGTTGGGGATCTGACTTACAACTGCTGTGTCATGACTCGCTATGAGCCTGACTGCCTGTGTCAGGTTAGTTATGTAGATTAGTTGTCAGGGGTTCGTCGCAGTCACCTAGCCAAAAAGCCGTAAGACCATACCTCCCACCCCGTTTCTACAGTCTCGTCTCTGCGGCGGACTTTGGCCGAAGTGACGAATGCCGTGGCCTGTGGGTTCTTTCGCATCATCATGTAACTTTGTCAACGTATCTGAAGGCAGATGAAAGCGGAACTTGACGGCCATAGTCCTACCTTAGTAGCTAAAGTATTAGAATCCGTTTCATTGGACATCATGCGGTATTTGTACATTGGGCTGCCGGGGGCCCGGCATGCCGCTGGGGCGAATTGACTGAAACGTCAATAAACCGAACATGCGCTTAGGGTGCGGTCTGGTAGGGTAAGCGAATCTGGCTTAGGACACTTGAGATTGGATCGCAAGCGATCATAAATGGTTCTGATTTTACGACCCCTCGGGCAAGTTTCACATCAGACCGTGTACCCATCAAACAGACGGCGCGGGGATAATGGCACCCCGGGTTGGGCACAACGAGGGCGGTCGGAGCGACCACAGACAGGTTAGTCGACTATAAACAACATTAAACATTAGTCTCATCGCCGAAGCCGTGGCAAGTGACGTTTGAATTGCAACAAATCCGGACTGAGACTTTACAACGAAATCGAGGGATGATTACCCGACATACTACGCCGTGACCACGCGCCCATGTAGAACCATAATATTCAGCCCAGCAGTACGGCTCTGATTATAACGATACAAGGCGTAATCACAAGTCTGCTAACCGTAACTGTCATCCAGCTGTGCGTATCCATCCGTTAGATGGACCCCTGTAACTCGCCGAGGATGTGCCCCGTATAATCCGCACACAAGAGGATTAAGATGTGATCGGGGATATTCCTATACCCCACAAGACCAGAGCCTCTGCGAACAATTCCTGCACCTCCATCAGATGACAATCCCGTTTGGGTTACTACTTCACTAAATCTGCAGCCGCTTGAGCCGTCAAAATCTGCTTGCATAGCCCTTACCCCAAATAGAGGTGGCTGGCACAACGCTGGGTGGGGGCATCTGGCGAGTTTACCTTAGGCTTCAGAGCCGGCGTGATGGCATACCGGTTACTTTACTCTGGCTACGTCTGTGCCTTGGGAGCTCGCCGAGTCGACCACGATTACCACTCCAAGTGAACGTCGGTCGCACGGGGTCCATCTAAGGGTTGTTAAGATTGCGTCCAAACACACGCACTTTTCGGCACGATATGGTAAAAATATAAAGAGTCGTCTATGGGAAGCTCACCTCCTGTGAATGGATGATGGCCATGCCATCTAAACCAATCAGCGAGCCTTAATAAGGTGGCCTACCTCCCGCCCGAGTGCATTCCTCCCTAGTGTTCTACCGGATTGGTACGAGAAAACGCGACCGAGGACCCGAAGACTGTTCTTATTTTGTAACAGCATCCGCATGACTTCTAATCGGTTGTAACTAGGGCTAACTTTTTAATTGTCCCATCTTTGTGACCCCTACCAGAAGCCTACCATCGCGCCTATTTTGAATGGAGGCGACGATGGTGGGTACAGAAAACGCAGTTTGGATAAAGCGAATGGTAGTGCTCAGGCATGTGGTAGTACTCGCCTACTATCGTTCGCGACGATGGTACGCCCGCATCTCGGCATGGCCCACCAGTTCCGCCATTAAACTGTTAACTCTACTGGATATTACCCAAGCTACCAGGGGAACCATCGTACCAGCTCCAACCCACCAGACCAGACGCCTAGTTCCCTAGCGGGGTGACCGACTCGCGGTCGCGACGTCTCACACACGCTAGCGTGGAAGTAAGATGAATCTTAGAGTCTCGGTGGCTAAAACGCCAGTCTGCTACAAAGTGACAGAGCCCCGAACAACCCCGTTGCCGAATCCAGTAACGCTCTTCATCGATACCACTCGCGCGGAAGTACGACTCGCGAGGGGCCCGTTGACCATTAGCGATTGGACCGCATGGTACATCTCCTGTTTATCAGTTCTGCATATGCATTAAATTGTACCTTTTGACATAGAAACCTAGACGGCGAACTGTATTATCAACGAGAAGCTTAGAGCTCGCGTCGCAATCATTGCGGACGAAATGTAATCCCTCAAGTCTACATACGCTAGGACAATCTATGTATCGGATAGATCATGGTCATGTTAATTGGAGGACCACAGATTATGAAGCGGCAATCGGACAACATTATTGCGAGCATTCGGACCTCAAAACTGATTAACTTAACGACAGGCGACCGTATATATATTTGGTGTTCGGTGCATCTTTGTGAAAACATATGGCGCATCCCCGGACAGTACGTGACCGAGTGATGAACGAGCGATTCTTTCGTCGACTAGGGGGGTGATAAGGAACGTTCCGTGATGGGGTAGATTATGAGCTTAATAACACTAGCGTTTGATAGACTTTCGTAAATGAGGAGATTGTAAGCAAAAGTAGATAAGGGCCATCGTCTATCCTCCTGAGGTCGTAGTTATACAACGGCGTGTACAGTCTACTGATTCTCGTTCATAGCGGACATACCATGCTCGTAGCGATAATGGTTGGCCACACTATATTTGTGTCCAATTCGAAACTGCTTGGTAACAGAGCGCACGCGGAATACGACCCATTATAACAGTACTATCACGCATGTAACGTATGCGAGACCGGTCGATGCCAGTGGCGTTTAGCGGCACCGGGCATAAAGCCTCGCCTGTCGGTTGGCACAGGTTATGCCTGAAGATCCCCCCAGGCAGAAATTGCCCTGTGATTGATGGTGTGACGCAAGTGGCTCGGCATGCGTTTTATTGGAGGTTACCAGTAAGTTGCGACAGACAGTCGCTATTATAAGGAGATATACAGCCAACGGGCGGTGGTACTGGGCGCTAGCAGTACACACGACGGCTGTTCACAAGGCATCTATTCAAAAGTGACTCCTGGGGCAATGTTGGCGTATTGTAGGATTCTGCCCTCTAACCTTCGGTACATATACCGCGGTAGCTAGAGTCACGCAATTTTACGTGGTGGAACCAAATCCGTAATATACGTAGTGGCGAAGTCGAACGTCAGCGATGGTTACAATACGAATCCTTTACCACGGGCGGATATATTGCCTTAGTGCCATGCGGTGTAGGCGGAACATGACTGTCGAACACATCGCGCCTGAACGTTTGGACCATGAGCTGATGCCGGTTGCACGTTGTTGTGCAACATCGAACACCAATTAACGAGCTGTCCCACGCCCGGAAGACCTACAGAGTAGATGTTACTCTGATGAGTAAGACGCTGACCTCCTATAGTAGCTGATCGGGTGACGTCTACCAATAAGAATGTGCCGCGCTTAGGTCGTCGCTATCCTACAACTGGTGCTCTCTTGTGCTCTGACCGTGAAGTGCCTTGAACGGTATGGAGCTATTGATGACCCATGGAGTGGAGGTAAGCGATTCTTTCGGAAAATTGCCCCTTCTTTAGTAGAGTATAGGCTCCCATAGACGACAAGTATGCAACAGTTCTTTGAATAGTCTACACGACAACTGCCCCGCTCTATCTACCCCAATTACTGGGATGGGAGATCCGCTCGTGCAGTAGGAAATCGGCACCAGTCCCGTGTTTCCACCACGTCAGCCGGGAAATGTAAGTGGGGGCTCCTGGAACATCTTATGCCTACTGGCTCACATGGCCCTGCCGATGTCACCACTTACCTGAAGGGCGTGAGCGACGAGCAATCGACTACATTTGGAAAGCGGGTCCGTAAGTAATCTGCCCAGGGGTCAAGGGGGGTGGCAGTCAGCTATCGAATCGCAGTAAAGTTTGCCTATGGTAAGACTAGATACCCGTTGCGCGTGCCGACAAGGTTAAAGCTGTGGGGTAGAGAACATAGGTTTTTCGCTATTCGTCCCCGCTGCGACTGTCGTGAACGGCTTCCCTGCCCATGCCCGGTTCCAAAGGAGTACCGACTGTCTGACTATGTATCAAGGTATACGCGTCTGCTATCAATGGGAAGAACAGCGCGACGCTCGTACTAGTTCTCAGCGTTTGCCTAGTGTTGCCGTGTGTAAGCCGGACTCAAGAAGAGTACCTAACGCGGTCGCCGTTCGGAGAAAATCAGCTCGATGAGGCACGAGGGCATAGAGCCTGTCGTACAGATCCATATTAAAACTTAACTATGCCTCAGGGCTCTTTGTATAGCGAAGTCAAACGAGCGCGAGGCAGTTATAACCCACAGCTTACAATCAGAACGCTACTATTCGACCATCGGTCTTCAAACCAGCGCGATGCGATGTCAGCGTACCTTCTAATGTTACTAACGCGCATAGATGCGAGAGCCGTGCCGTGTCTCAAGGAGCTACTGGCCGATTCACGGTCGCCTAATCACACGTCTTGCTCGAGGAGGCGCAGAACAGACCACTTTGGAACAAGCATACCGCTAGGTGTATGTCTGCGCTGCCTCTCCAGAGTAACGTCCAGTCTTATATCTGTAGCACTAGTATACGTCAGTAACAACTCCTAGGACCTACTTATACATGCTTTCAATCTGCGATAGTCCTAACAACTAGTCCGGGCGTTAGGTATGATAGATCGGAAACAGATGCGTGTGAATCTTACGCCACTCCTCCACTGTACGCTACACCATCGGACTCTCTCCCTTACTCACTACAAGAGTCCACAGCCTGACTAAGCCTGCAAAGTTCAGAGGAGTCTTAGCGAAGCCCCTGGGTACAGACACTCCATACGTCTATGGATCGACAACACCTGTGCACCTAACGGCCAGATGCTCGATGCGGGCCGTGCTCCGGGACTACAGCAGGGTATCCGCATAGATGGAGAATGTCAGCGTAAACATAACGACATTGGCCCATCCTCACAGAACATCCGCCCGCGCTTATCAATTAACACTATGACCGGCATTTTCGTACCAGTTCTTAAGAGCTCGATCCGTTGAT'
    print(reverse_complement(text))    

test1()
test2()