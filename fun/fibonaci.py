def fib(int):
  fib = []
  if (int > 0):
    fib.append(1)
  if (int > 1):
    fib.append(1)
  if (int > 2):
    int = int - 1
    i = 0
    while i < int:
      newValue = fib[-1] + fib[-2]
      fib.append(newValue)
      i += 1
  return fib

numbers = fib(10)
print(numbers)

