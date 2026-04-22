def resolve(token, variables):
    token = token.strip()

    if token in variables:
        return variables[token]
    elif token.isdigit():
        return int(token)
    else:
        return token

def multiply(value, variables, mult):
    sides = value.split(mult, 1)

    first_factor = resolve(sides[0], variables)
    sec_factor = resolve(sides[1], variables)

    try:
        return int(first_factor) * int(sec_factor)
    except ValueError:
        print('Error')

def addition(value, variables, add):
    sides = value.split(add, 1)

    first_factor = resolve(sides[0], variables)
    sec_factor = resolve(sides[1], variables)

    try:
        return int(first_factor) + int(sec_factor)
    except ValueError:
        print('Error')

def subtraction(value, variables, sub):
    sides = value.split(sub, 1)

    first_factor = resolve(sides[0], variables)
    sec_factor = resolve(sides[1], variables)

    try:
        return int(first_factor) - int(sec_factor)
    except ValueError:
        print('Error')

def modulo(value, variables, mod):
    sides = value.split(mod, 1)

    first_factor = resolve(sides[0], variables)
    sec_factor = resolve(sides[1], variables)

    try:
        return int(first_factor) % int(sec_factor)
    except ValueError:
        print('Error')

def reverse(value, variables, reverse_key):
    input = value.split(reverse_key, 1)[0].strip()
    word = resolve(input, variables)
    return str(word)[::-1]