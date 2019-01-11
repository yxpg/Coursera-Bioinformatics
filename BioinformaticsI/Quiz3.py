from library.Motif import calculate_entropy

def question3():
    distributions = {
        'A' : [0.5, 0, 0, 0.5],
        'B' : [0.25, 0.25, 0.25, 0.25],
        'C' : [0, 0, 0, 1],
        'D' : [0.25, 0, 0.5, 0.25]
    }
    
    entropies = [(key, calculate_entropy(distributions[key])) for key in distributions]
    sortedEntropies = sorted(entropies, key = lambda e: e[1])
    print(sortedEntropies)

question3()