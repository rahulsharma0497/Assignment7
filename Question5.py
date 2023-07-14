def reverse_k_chars(s, k):
  """
  Reverses the first k characters for every 2k characters counting from the start of the string.

  Args:
    s: A string.
    k: An integer.

  Returns:
    A string with the reversed characters.
  """

  result = ""
  i = 0
  while i < len(s):
    j = min(i + k, len(s))
    result += s[j - 1:i - 1:-1] + s[i:j]
    i = j + k
  return result


if __name__ == "__main__":
  s = "abcdefg"
  k = 2
  print(reverse_k_chars(s, k))