def lucas_nums_less_than_n(n):  # answer for q1
    # n = int(input('Enter the lucas sequence max value: ')) can take n as input during the function instead
    a = 2
    b = 1
    if n > 0:
        print(2)
        while b <= n:
            temp = b
            b = a + b
            a = temp
            print(a)


def lucas_nums_list_with_loop(n):  # answer for q2 section a
    # n = int(input('Enter the lucas sequence term number: ')) can take n as input during the function instead
    a = 2
    b = 1
    if n > 0:
        lucas_list = [2]
        for i in range(n - 1):
            temp = b
            b = a + b
            a = temp
            lucas_list.append(a)
        print(*lucas_list)


def lucas_gen(n):  # generator for q2 section b
    a = 2
    b = 1
    yield 2
    for x in range(n - 1):
        temp = b
        b = a + b
        a = temp
        yield a


def lucas_nums_list_with_gen(n):  # answer for q2 section b
    # n = int(input('Enter the lucas sequence term number: ')) can take n as input during the function instead
    if n > 0:
        lucas_list = list(lucas_gen(n))
        print(*lucas_list)


# lucas_nums_less_than_n(5)
# lucas_nums_list_with_loop(5)
# lucas_nums_list_with_gen(5)
