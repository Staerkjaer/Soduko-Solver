from os import listdir
import solver
import time


for puzzle in listdir("Puzzles"):
    startTime = time.time()
    Board = []
    sudokuIn = "Puzzles/" + puzzle
    with open(sudokuIn, "r") as file:
        for line in file:
            addLine = []
            for char in line:
                if char == ".":
                    addLine.append(0)
                elif char != "\n":
                    addLine.append(int(char))
            Board.append(addLine)

    solver.solve(Board)
    endTime = time.time() - startTime
    print("\n" + puzzle)
    solver.print_flag(Board)
    print("\n-- " + puzzle + " --")
    solver.print_board(Board)
    print("\nIt took " + str(endTime) + " seconds")

