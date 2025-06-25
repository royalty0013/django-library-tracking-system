import random


# rand_list =
def random_numbers():
    random_numbers = []
    for _ in range(1, 20):
        number = random.randint(1, 20)
        random_numbers.append(number)
    return random_numbers


# list_comprehension_below_10 =
nums = random_numbers()
numbers_below_10 = [num for num in nums if num <= 10]

# list_comprehension_below_10 =
filter_nums = filter(lambda x: x <= 10, nums)
