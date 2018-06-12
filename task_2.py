numbers = [1, 2, -3, 5, -6, 7, -9]

def f(numbers):
    for element in range(len(numbers)):
        if element == len(numbers) - 1:
            break
        elif numbers[element] < 0:
            numbers[element] = numbers[element + 1]
    return numbers

print(f(numbers))