import random


def positionIsValid(grid, line, column, number):
    # verifica se o número existe na linha
    for i in range(len(grid)):
        if grid[line][i] == number:
            return False

    # verifica se o número existe na coluna
    for i in range(len(grid)):
        if grid[i][column] == number:
            return False

    # verifica se o número existe no subgrupo
    SIZE_SUBGROUP = 3
    positionXsubGroup = line - line % 3
    positionYsubGroup = column - column % 3
    for posX in range(SIZE_SUBGROUP):
        for posY in range(SIZE_SUBGROUP):
            if grid[posX + positionXsubGroup][posY + positionYsubGroup] == number:
                return False
    return True


def formatGride(grid):
    for linha in range(len(grid)):
        if linha % 3 == 0:
            print("+-------+-------+-------+")

        for coluna in range(len(grid[0])):
            if coluna % 3 == 0:
                print('|', end=' ')

            if coluna == 8:
                print(grid[linha][coluna], '|')
            else:
                print(str(grid[linha][coluna]), end=" ")
    print("+-------+-------+-------+")


def searchSolution(grid, line, column):
    # final da matriz
    if line == len(grid) - 1 and column == len(grid[0]):
        return True

    # verifica se atingiu o limite da coluna e sigo para a próxima linha
    if column == len(grid):
        line += 1
        column = 0

    # verifica se a posição atual da malha contém valores maiores que zero
    if grid[line][column] > 0:
        return searchSolution(grid, line, column + 1)

    for numero in range(1, len(grid) + 1, 1):
        if positionIsValid(grid, line, column, numero):
            grid[line][column] = numero
            if searchSolution(grid, line, column + 1):
                return True

        grid[line][column] = 0
    return False


def generateGrid():
    grid = [[0 for x in range(9)] for y in range(9)]  # Matriz inicial preenchida com 0
    grid[0][1] = random.randint(1, 9)
    grid[1][5] = random.randint(1, 9)                 # Adiciona um número randômico para cada posição desejada
    grid[3][7] = random.randint(1, 9)                                                     #(posições estáticas)
    grid[5][1] = random.randint(1, 9)
    grid[6][5] = random.randint(1, 9)
    filledGrid = grid                                 # Guarda a nova matriz preenchida (randômicos e 0)
    searchSolution(filledGrid, 0, 0)                  # Verifica a solução utilizando a matriz
    formatGride(filledGrid)                           # Imprime a matriz prenchida e com a formatação correta


generateGrid()
