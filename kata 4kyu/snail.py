def snail(array):
    expected = []
    start_row = 0
    start_column = 0
    end_row = len(array) - 1
    end_column = len(array) - 1
    if array == [[]]:
        return expected
    while start_row < len(array) - 1 and start_row != end_column:
        column = start_column
        while column <= end_column:
            expected.append(array[start_row][column])
            column = column + 1
        row = start_row
        while row < end_row:
            row = row + 1
            expected.append(array[row][end_column])
        column =end_column - 1
        while column >= start_column:
            expected.append(array[row][column])
            column = column - 1
        if column < start_column:
            column = start_column
        end_row -= 1
        row = end_row
        while row > start_row:
            expected.append(array[row][column])
            row = row - 1
        start_column += 1
        start_row += 1
        end_column -= 1
    if expected.count(array[start_row][end_column]) == 0:
        expected.append(array[start_row][end_column])

    return expected