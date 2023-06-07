def some_gen(begin: int, n: int, func) -> int:
    el = begin
    yield el

    for i in range(n-1):
        el = func(el)
        yield el
