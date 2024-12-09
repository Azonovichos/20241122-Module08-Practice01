# Module 8 Practice 1

def add_everything_up(a, b):
    try:
        result = (a + b)
        if result is int:
            return result
        else:
            return round(result, 3)
    except (TypeError):
        result = str(a) + str(b)
        return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# help('except')
# help('raise')
