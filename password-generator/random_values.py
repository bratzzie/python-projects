import random


def populate_with_random_values(values, num_of_values):
    result = ""
    for i in range(num_of_values):
        result += random.choice(values)
    return result


def shuffle_string(string):
    print(string)
    return ''.join(random.sample(string, len(string)))
