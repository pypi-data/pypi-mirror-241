def display_state(matrices, title="INITIAL"):
    print(f"================ {title} STATE =================")
    for i in range(len(matrices)):
        print(matrices[i], sep="\n")
    print()


# COMPLEXITE O(n*n)
def game_of_life(matrices):
    n_col = len(matrices[0])
    n_row = len(matrices)
    # on initialize un etat vide
    next_Matrices = [[0 for _ in range(n_col)] for _ in range(n_row)]
    for i in range(n_row):
        for j in range(n_col):
            num_neighbors = 0
            # print("ij: ", i, j, "mat:", matrices[i][j], end="\t")
            # check des 8 voisins
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < len(matrices) and 0 <= y < len(matrices[0]):
                        if matrices[x][y] == 1:
                            num_neighbors += 1

            num_neighbors = num_neighbors - matrices[i][j]
            # print("neighbors: ",num_neighbors, end="\t")
            if num_neighbors in [0, 1] or num_neighbors > 3:
                    # print("die")
                    next_Matrices[i][j] = 0
            else:

                if matrices[i][j] == 0:
                    if num_neighbors == 3:
                        # print("survival")
                        next_Matrices[i][j] = 1
                    else:
                        pass
                        # print("died")
                if matrices[i][j] == 1:
                    next_Matrices[i][j] = 1
                    # print("survival")

    return next_Matrices