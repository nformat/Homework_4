import string

def issym(a):
    """
    Удаляет все небуквенные символы внутри строки(Только латиница)
    """
    s = "".join([str(i) for i in a if i in string.ascii_letters])
    return s


a = "5454asdasdfaf123fssafa324324vdsvssd,.fAAAAFFFF     gfghsЯЯЯЯЯ"

assert issym("111aaa  !!!") == "aaa", "Фукция issym не работает"

print("Строка без небуквеных и нелатинских символов:\n",issym(a))
