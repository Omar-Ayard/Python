def default_try_value(value):
    def _default_try_value(func):
        def box(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except:
                return value
            return result

        return box

    return _default_try_value


@default_try_value('error')
def divide_entre_2(numero):
    return numero / 2


print
divide_entre_2(16)
print
divide_entre_2('david')