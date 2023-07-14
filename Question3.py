def add_strings(num1, num2):
  """
  Returns the sum of num1 and num2 as a string.

  Args:
    num1: A string representing a non-negative integer.
    num2: A string representing a non-negative integer.

  Returns:
    A string representing the sum of num1 and num2.
  """

  carry = 0
  result = []
  i, j = len(num1) - 1, len(num2) - 1
  while i >= 0 or j >= 0:
    digit1 = int(num1[i]) if i >= 0 else 0
    digit2 = int(num2[j]) if j >= 0 else 0
    sum_digit = digit1 + digit2 + carry
    result.append(str(sum_digit % 10))
    carry = sum_digit // 10
    i, j = i - 1, j - 1
  if carry:
    result.append(str(carry))
  return ''.join(reversed(result))


if __name__ == "__main__":
  num1 = "11"
  num2 = "123"
  print(add_strings(num1, num2))