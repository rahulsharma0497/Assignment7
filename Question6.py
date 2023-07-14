def can_be_shifted(s, goal):
  """
  Returns True if s can become goal after some number of shifts on s, False otherwise.

  Args:
    s: A string.
    goal: A string.

  Returns:
    True if s can become goal after some number of shifts on s, False otherwise.
  """

  if len(s) != len(goal):
    return False

  count = 0
  for i in range(len(s)):
    if s[i] != goal[len(goal) - 1 - i]:
      count += 1
    if count > len(goal) - 1:
      return False
  return True


if __name__ == "__main__":
  s = "abcde"
  goal = "cdeab"
  print(can_be_shifted(s, goal))