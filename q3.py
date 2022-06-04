def list_to_set(lst):
    if type(lst) is tuple:
        lst = list(lst)
    for x in lst:
        while lst.count(x) > 1:
            lst.remove(x)
    print(*lst)
