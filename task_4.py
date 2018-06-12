numbers = [1, 1, 1, 1, 1]
def f(numbers):
       for element in range(len(numbers)):
           if element % 2 == 0:
                numbers[element] = 0
           else:
                pass
       return numbers

print(f(numbers))