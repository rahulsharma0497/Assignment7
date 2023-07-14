def is_isomorphic(s, t):
  """
  Returns True if s and t are isomorphic, False otherwise.

  Args:
    s: A string.
    t: A string.

  Returns:
    True if s and t are isomorphic, False otherwise.
  """

  if len(s) != len(t):
    return False

  char_map = {}
  seen = set()
  for i in range(len(s)):
    if s[i] not in char_map:
      if t[i] in seen:
        return False
      char_map[s[i]] = t[i]
      seen.add(t[i])
    elif char_map[s[i]] != t[i]:
      return False
  return True


if __name__ == "__main__":
  s = "egg"
  t = "add"