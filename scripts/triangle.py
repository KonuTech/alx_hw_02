import textwrap


def generate_pascal_row(row):
    """
    Generates the 'row' of Pascal's triangle.
    """
    if row == 0:
        return [1]
    prev_row = generate_pascal_row(row - 1)
    new_row = [1]
    for i in range(len(prev_row) - 1):
        new_row.append(prev_row[i] + prev_row[i + 1])
    new_row.append(1)
    return new_row


def pascal_triangle(n, to_str=False):
    """
    Generates Pascal's triangle up to the 'n' rows.
    If 'to_str' is True, returns the triangle as a string.
    """
    triangle = []
    for i in range(n):
        row = generate_pascal_row(i)
        triangle.append(row)

    if to_str:
        max_width = len(" ".join(map(str, triangle[-1])))
        return "\n".join(
            [" ".join(map(str, row)).center(max_width) for row in triangle]
        )
    else:
        return triangle


# Testing the functions
def test_pascal_triangle():
    actual = pascal_triangle(6)
    assert actual == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
    ]


def test_pascal_triangle_to_str():
    actual = pascal_triangle(7, to_str=True)
    expected = textwrap.dedent("""
       1       
      1 1      
     1 2 1     
    1 3 3 1    
   1 4 6 4 1   
  1 5 10 10 5 1
 1 6 15 20 15 6 1
""").strip()

     # Flatten both actual and expected strings
    actual_flat = ' '.join(actual.split())
    expected_flat = ' '.join(expected.split())

    assert actual_flat  == expected_flat

# Running the tests
test_pascal_triangle()
test_pascal_triangle_to_str()
