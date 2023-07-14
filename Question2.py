def is_strobogrammatic(num):
  """
  Returns True if num is a strobogrammatic number, False otherwise.

  Args:
    num: A string.

  Returns:
    True if num is a strobogrammatic number, False otherwise.
  """

  strobogrammatic_pairs = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
  if len(num) == 0:
    return True
  if len(num) == 1:
    return num in strobogrammatic_pairs

  for i in range(len(num) // 2):
    if num[i] not in strobogrammatic_pairs or strobogrammatic_pairs[num[i]] != num[-i - 1]:
      return False
  return True


if __name__ == "__main__":
  num = "69"
  print(is_strobogrammatic(num))