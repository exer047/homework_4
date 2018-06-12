numbers = [5, 2, 3, 4]

def f(numbers):
    for element in range(len(numbers)):
        numbers[element] = numbers[element] ** 2
    return numbers

print(f(numbers))