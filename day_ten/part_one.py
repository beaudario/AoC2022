lines = open('Input.txt').read().splitlines()

program_instructions = []
CYCLES_TO_COMPUTE = [20, 60, 100, 140, 180, 220]
x = 1
cycles = 1
sum = 0

for line in lines:
    if line.startswith('addx'):
        number = line.removeprefix('addx ')
        program_instructions.append(0)
        program_instructions.append(int(number))
    elif line.startswith('noop'):
        program_instructions.append(0)

for number in program_instructions:

    for cycle in CYCLES_TO_COMPUTE:
        if cycles == cycle:
            sum += x * cycles

    if number == 0:
        cycles += 1
    else:
        x += number
        cycles += 1

print(sum)