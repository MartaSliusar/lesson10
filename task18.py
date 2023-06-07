def lchain(*iterables) -> list:
    result = []
    for iterable in iterables:
        for el in iterable:
            result.append(el)
    return result
