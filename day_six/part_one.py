with open('Input.txt') as f:
    datastream = f.read()


def find_start_of_packet(datastream):
    last_four = []

    for i, c in enumerate(datastream):
        last_four.append(c)
        if len(last_four) > 4:
            last_four.pop(0)

        if len(set(last_four)) == 4:
            return i + 1


print(find_start_of_packet(datastream))
