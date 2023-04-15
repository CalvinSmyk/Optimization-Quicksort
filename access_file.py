

def read_list_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        numbers = [int(line.strip()) for line in lines]
    return numbers