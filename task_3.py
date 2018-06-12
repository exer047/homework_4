numbers = [2, 4, 6, 8]

def f(numbers):
    for element in range(len(numbers)):
        if element == len(numbers) - 1:
            numbers[element] = numbers[0]
        else:
            numbers[element] = numbers[element + 1]
    return numbers

print(f(numbers))