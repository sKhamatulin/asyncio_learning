def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass

# def subgen():
#     x = 'ready to accept message'
#     message = yield
#     print('Subgen recived: ', message)


# @coroutine
# def average():  # \n g.send(4) ... \n g.throw(StopIteration)
#     count = 0
#     summ = 0
#     average = None

#     while True:

#         try:
#             x = yield average
#         except StopAsyncIteration:
#             print('Done')
#             break
#         else:
#             count += 1
#             summ += x
#             average = round(summ / count, 2)

#     return average

# @coroutine
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('ku-ku')
            break
        else:
            print('...........', message)
    return 'Returned from sugen()'


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)
