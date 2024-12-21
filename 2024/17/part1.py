            #A  B  C
registers = [0, 0, 0]
program = []
output = []
iptr = 0

def parse(lines):
    for i in range(3):
        s = lines[i]
        j = s.find(": ") + 2
        val = 0
        while j < len(s) and s[j] >= '0' and s[j] <= '9':
            val = val*10 + int(s[j])
            j += 1
        registers[i] = val

    for ch in lines[4]:
        if ch >= '0' and ch <= '9':
            program.append(int(ch))

def get_operand_value(x):
    if x >= 0 and x <= 3:
        return x
    return registers[x-4]

def adv(combo_operand):
    val = get_operand_value(combo_operand)
    registers[0] //= (2**val)
    global iptr
    iptr += 2

def bxl(literal_operand):
    registers[1] ^= literal_operand
    global iptr
    iptr += 2

def bst(combo_operand):
    val = get_operand_value(combo_operand)
    registers[1] = val % 8
    global iptr
    iptr += 2

def jnz(literal_operand):
    global iptr
    if registers[0] == 0:
        iptr += 2
        return
    iptr = literal_operand

def bxc():
    registers[1] ^= registers[2]
    global iptr
    iptr += 2

def out(combo_operand):
    val = get_operand_value(combo_operand)
    output.append(val % 8)
    global iptr
    iptr += 2

def bdv(combo_operand):
    val = get_operand_value(combo_operand)
    ans = registers[0] // (2**val)
    registers[1] = ans
    global iptr
    iptr += 2

def cdv(combo_operand):
    val = get_operand_value(combo_operand)
    ans = registers[0] // (2**val)
    registers[2] = ans
    global iptr
    iptr += 2

def solve():
    global iptr
    while iptr < len(program):
        opcode = program[iptr]
        operand = program[iptr+1]
        if opcode == 0:
            adv(operand)
        if opcode == 1:
            bxl(operand)
        if opcode == 2:
            bst(operand)
        if opcode == 3:
            jnz(operand)
        if opcode == 4:
            bxc()
        if opcode == 5:
            out(operand)
        if opcode == 6:
            bdv(operand)
        if opcode == 7:
            cdv(operand)

    for i in range(len(output)):
        print(output[i], sep='', end='')
        if i < len(output) - 1:
            print(',', sep='', end='')
    print()

with open("input.txt") as file:
    lines = list(map(str.rstrip, file.readlines()))
    parse(lines)
    solve()
