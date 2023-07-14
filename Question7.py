def is_backspace_equivalent(s, t):
  """
  Returns True if s and t are equal when both are typed into empty text editors, False otherwise.

  Args:
    s: A string.
    t: A string.

  Returns:
    True if s and t are equal when both are typed into empty text editors, False otherwise.
  """

  i, j = 0, 0
  while i < len(s) and j < len(t):
    while i < len(s) and s[i] == "#":
      i += 1
    while j < len(t) and t[j] == "#":
      j += 1
    if i == len(s) or j == len(t) or s[i] != t[j]:
      return False
    i, j = i + 1, j + 1
  return i == len(s) and j == len(t)


if __name__ == "__main__":
  s = "ab#c"
  t = "ad#c"
  print(is_backspace_equivalent(s, t))