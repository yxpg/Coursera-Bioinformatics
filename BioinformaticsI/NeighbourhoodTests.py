import time
from library.Neighbourhood import *

def test1():
    pattern = 'ACG'
    print(' '.join(str(n) for n in immediate_neighbours(pattern)))

def test2():
    pattern = 'ACG'
    print(' '.join(str(n) for n in immediate_neighbours(pattern)))

def test3():
    pattern = 'GGACATGGCTG'
    distance = 2
    print('\n'.join(str(n) for n in neighbours(pattern, distance)))

def test4():
    pattern = 'GGACATGGCTG'
    distance = 2
    print('\n'.join(str(n) for n in iterative_neighbours(pattern, distance)))

def test5():
    pattern = 'GGACATGGCTG'
    distance = 2
    print(neighbours(pattern, distance) == iterative_neighbours(pattern, distance))

def test6():
    pattern = 'GGACATGGCTG'
    distance = 4    
    t0 = time.time()
    recursive = neighbours(pattern, distance)
    t1 = time.time()
    iterative = iterative_neighbours(pattern, distance)
    t2 = time.time()
    print(recursive == iterative)
    print('Recursive: ' + str(t1 - t0))
    print('Iterative: ' + str(t2 - t1))

def test7():
    pattern = 'ACG'
    print(' '.join(str(n) for n in iterative_neighbours(pattern, 1)))

test1()
#test2()
#test3()
#test4()
#test5()
#test6()
test7()
