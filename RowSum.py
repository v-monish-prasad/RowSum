def findRowSum(matrix):
    # if not elements:
    #     return "Empty Array."

    rowSums = []

    for i in range(len(matrix)):
        rowSum = 0
        for j in range(len(matrix[0])):
            rowSum += matrix[i][j]
        rowSums.append(rowSum)

    return rowSums


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().strip('[').strip(']').split(','))))

    print(findRowSum(matrix))
