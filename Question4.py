def reverse_words(s):
  """
  Reverses the order of characters in each word within a sentence while still preserving whitespace and initial word order.

  Args:
    s: A string.

  Returns:
    A string with the reversed words.
  """

  words = s.split(" ")
  reversed_words = []
  for word in words:
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
      reversed_word += word[i]
    reversed_words.append(reversed_word)
  return " ".join(reversed_words)


if __name__ == "__main__":
  s = "Let's take LeetCode contest"
  print(reverse_words(s))