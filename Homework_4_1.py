def la(a=3, b=3, c=0):
    """
    Генерирует и возвращает песню la-la-la. Функция принимает 3 аргумента:
    a - сколько строк будет в песне
    b - сколько «la» будет в строке («la» в строке объединяются дефисом
    c - если 0, то в конце песни (в конце последней строчки) стоит точка, если 1, то в конце стоит «!».
    """
    e = ("la-"*(b-1)+"la\n")*a
    r = e.strip()+("." if c == 0 else "!")
    return r


print(la())
