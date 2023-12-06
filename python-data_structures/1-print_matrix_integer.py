def print_matrix_integer(matrix=[[]]):
    """This function prints a matrix of integers."""
    for row in matrix:
        for element in row:
            print(f"{element:3}", end=" ")
        print()
