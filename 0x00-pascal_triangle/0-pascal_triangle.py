def pascal_triangle(n):
    """
    Generate Pascal's triangle with 'n' rows.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if triangle:  # Check if triangle is not empty
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
