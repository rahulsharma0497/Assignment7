def check_straight_line(coordinates):
  """
  Checks if the points in coordinates make a straight line in the XY plane.

  Args:
    coordinates: An array of points.

  Returns:
    True if the points make a straight line, False otherwise.
  """

  if len(coordinates) < 2:
    return False

  x_diff = coordinates[1][0] - coordinates[0][0]
  y_diff = coordinates[1][1] - coordinates[0][1]
  for i in range(2, len(coordinates)):
    if coordinates[i][0] - coordinates[0][0] != x_diff or coordinates[i][1] - coordinates[0][1] != y_diff:
      return False
  return True


if __name__ == "__main__":
  coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
  print(check_straight_line(coordinates))