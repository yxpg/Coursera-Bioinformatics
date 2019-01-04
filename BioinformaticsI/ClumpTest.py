import time
from library.Clump import find_clumps
from library.SlowClump import slow_find_clumps

def test1():
    genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
    patternLength = 5
    clumpLength = 50 
    times = 4

    t0 = time.time()
    result = find_clumps(genome, patternLength, times, clumpLength)
    t1 = time.time()
    print(t1 - t0)
    print(' '.join(str(p) for p in result))

def test2():
    genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
    patternLength = 5
    clumpLength = 50 
    times = 4

    t0 = time.time()
    result = slow_find_clumps(genome, patternLength, times, clumpLength)
    t1 = time.time()
    print(t1 - t0)
    print(' '.join(str(p) for p in result))    

def test3():
    with open('dataset/EColi.txt') as file:
        content = file.readlines()
    genome = [line.strip() for line in content][0]
    patternLength = 9
    clumpLength = 500
    times = 3

    t0 = time.time()
    result = find_clumps(genome, patternLength, times, clumpLength)
    t1 = time.time()
    print(t1 - t0)
    print(len(result))

def test4():
    with open('dataset/dataset_4_5.txt') as file:
        content = file.readlines()
    genome = [line.strip() for line in content][0]
    patternLength = int([line.strip() for line in content][1])
    clumpLength = int([line.strip() for line in content][2])
    times = int([line.strip() for line in content][3])

    t0 = time.time()
    result = find_clumps(genome, patternLength, times, clumpLength)
    t1 = time.time()
    print(t1 - t0)
    print(' '.join(str(p) for p in result))

test1()
test2()
test3()
test4()