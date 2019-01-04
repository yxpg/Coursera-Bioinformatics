# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def reverse_complement(pattern):
    return complement(reverse(pattern))

def reverse(pattern):
    return pattern[::-1]

def complement(pattern):
    reverse = ''
    for char in pattern:
        if char == 'A':
            reverse += 'T'
        elif char == 'T':
            reverse += 'A'
        elif char == 'C':
            reverse += 'G'
        else:
            reverse += 'C'
    return reverse