with open('Input.txt') as f:
    datastream = f.read()

def find_start_of_packet(datastream):

    last_fourteen = []

    for i, c in enumerate(datastream):
        last_fourteen.append(c)
        if len(last_fourteen) > 14:
            last_fourteen.pop(0)

        if len(set(last_fourteen)) == 14:
            return i + 1


print(find_start_of_packet(datastream))
