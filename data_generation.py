import random

def generate_and_save_random_list(x, filename):
    numbers = list(range(1, x+1))  # create a list of numbers from 1 to x
    numbers = sorted(numbers,reverse=True)
    #random.shuffle(numbers)  # shuffle the list randomly
    with open(filename, 'w') as f:
        for number in numbers:
            f.write(str(number) + '\n')  # write each number to a new line in the file
    return numbers

def shuffle_and_save(length, num_indices, save_path):
    arr = list(range(length))
    indices_to_shuffle = random.sample(range(length), num_indices)
    for i in indices_to_shuffle:
        random_index = random.randint(0, length - 1)
        arr[i], arr[random_index] = arr[random_index], arr[i]
    with open(save_path, 'w') as f:
        for num in arr:
            f.write(f"{num}\n")



if __name__ == '__main__':
    #[10, 500, 2500, 10000, 50000, 100000, 250000, 500000, 1000000, 10000000]
    generate_and_save_random_list(10000000,'datalists/3_9_datalist')
    #shuffle_and_save(500000,250000,'datalists/last_0')