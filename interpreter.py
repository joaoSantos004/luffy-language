import sys
from functions import resolve, multiply, addition, subtraction, modulo, reverse

filename = sys.argv[1]

f = open(filename, 'r')
lines = f.readlines()
f.close()

printer_ln = 'gomuno '
printer = 'gomu '
var_key = 'free '
mult = 'gatling'
add = 'crew'
sub = 'g3'
user_input = 'meat '
loop = 'gear '
mod = 'nika'
if_key = 'straw '
else_key = 'hat ['
reverse_key = 'ace'
char_key = 'chopper'

def run_lines(lines, variables):
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if line == '':
            i += 1
            continue

        # Assign variables
        if line.startswith(var_key):
            var = line[5:].strip()

            parts = var.split('=', 1)
            name = parts[0].strip()
            value = parts[1].strip()

            # string var
            if (value.startswith('"') and value.endswith('"')) or \
            (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]

            # integer var
            elif value.isdigit():
                value = int(value)

            # multiplication (gatling)
            elif mult in value:
                value = multiply(value, variables, mult)

            # addition (crew)
            elif add in value:
                value = addition(value, variables, add)

            # subtraction (g3)
            elif sub in value:
                value = subtraction(value, variables, sub)

            # mod (nika)
            elif mod in value:
                value = modulo(value, variables, mod)

            # reverse (ace)
            elif reverse_key in value:
                value = reverse(value, variables, reverse_key)

            variables[name] = value

        # User input (meat)
        elif line.startswith(user_input):
            name = line[4:].strip()
            variables[name] = raw_input()

        # loops (gear)
        elif line.startswith(loop) and line.endswith('['):
            count_text = line[len(loop):-1].strip()
            count = resolve(count_text, variables)
            block = []
            i += 1

            while i < len(lines):
                block_line = lines[i].strip()


                if block_line == ']':
                    break

                block.append(lines[i])
                i += 1

            try:
                count = int(count)
                for _ in range(count):
                    run_lines(block, variables)
            except ValueError:
                print('Error')

        # if command
        elif line.startswith(if_key) and line.endswith('['):
            condition = line[len(if_key):-1].strip()

            parts = condition.split('==', 1)
            value_one = resolve(parts[0], variables)
            value_two = resolve(parts[1], variables)

            block = []
            else_block = []

            i += 1

            while i < len(lines):
                block_line = lines[i].strip()


                if block_line == ']':
                    i += 1
                    break

                block.append(lines[i])
                i += 1

            if lines == '':
                i += 1

            if i < len(lines) and lines[i].strip() == else_key:
                i += 1
                while i < len(lines):
                    block_line = lines[i].strip()


                    if block_line == ']':
                        i += 1
                        break

                    else_block.append(lines[i])
                    i += 1


            if value_one == value_two:
                run_lines(block, variables)
            else:
                run_lines(else_block, variables)


        # Print command (gomu)
        elif line.startswith(printer_ln) or line.startswith(printer):

            # new line or not logic
            if line.startswith(printer_ln):
                content = line[len(printer_ln):].strip()
                newline = True
            else:
                content = line[len(printer):].strip()
                newline = False

            # string case
            if content.startswith('"') and content.endswith('"'):
                print_value = content[1:-1]
            elif content.startswith("'") and content.endswith("'"):
                print_value = content[1:-1]

            # print multiplication
            elif mult in content:
                print_value = multiply(content, variables, mult)

            # print addition
            elif add in content:
                print_value = addition(content, variables, add)

            # print subtraction
            elif sub in content:
                print_value = subtraction(content, variables, sub)

            # print mod
            elif mod in content:
                print_value = modulo(content, variables, mod)

            # print reversed word
            elif reverse_key in content:
                print_value = reverse(content, variables, reverse_key)

            # print variable
            elif content in variables:
                print_value = variables[content]

            # input error
            else:
                print('Error')

            if newline:
                print(print_value)
            else:
                sys.stdout.write(str(print_value))

        i += 1


variables = {}
run_lines(lines, variables)
