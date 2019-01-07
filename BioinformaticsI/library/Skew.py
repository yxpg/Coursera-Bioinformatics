# Input:  A String Genome
# Output: The skew array of Genome as a list.
def skew_array(genome):
    Skew = [0]
    for i in range(0, len(genome)):
        if genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        elif genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        else:
            Skew.append(Skew[i])
    return Skew


# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def minimum_skew(genome):
    positions = []
    skew = skew_array(genome)
    minval = min(skew)
    for i in range(len(skew)):
        if skew[i] == minval:
            positions.append(i)
    return positions