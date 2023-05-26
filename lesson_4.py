from time import time


def gen_filename():
    '''
    function for generation unique filename
    t is time from 01.01.1970 in milliseconds
    '''
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))


# g = gen_filename()


def gen_1(s):
    '''
    get every element from input string in every iteration
    '''
    for i in s:
        yield i


def gen_2(n):
    '''
    get every num in range from input int
    '''
    for i in range(n):
        yield i


# object of generator one
g1 = gen_1('sergey')

# object of generator two
g2 = gen_2(4)

# list for objects of generators
tasks = [g1, g2]

# if list is not empty
while tasks:
    # get the first element from list and delete it
    task = tasks.pop(0)

    try:
        # get a result from generator
        i = next(task)
        print(i)
        # append the element in end of quiue
        tasks.append(task)
    except StopIteration:
        pass
