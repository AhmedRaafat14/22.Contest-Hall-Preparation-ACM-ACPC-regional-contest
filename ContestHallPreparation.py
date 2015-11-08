# Read T Input
# T ==> the number of test cases (1 ≤ T ≤ 100)
T = raw_input()
T = int(T)
# Loop by # of test cases
for unusedTestCases in range(0, T):
    # N and M (1 ≤ N, M ≤ 100) representing the dimensions of the hall
    N, M = raw_input().split()
    N = int(N)
    M = int(M)
    # table matrix to hold 2d array
    table = []
    # using it to store visted indices in matrix
    adjacents_checked = []
    # the number of different universities having at least two of
    #          their teams adjacent to each other. 
    differ_uni_adjacents = 0
    # N lines each line contains M integers separated by a single space,
    #      representing the tables assignment in this row.
    #      Each integer represents the university ID of the team assigned to
    #      this table or -1 if it is empty. All universities IDs are positive
    #      integers not greater than 100. 
    for i in range(0, N): 
        line = raw_input().split()
        table += [line]
    # loop throw matrix and build the probablity rules
    for i in range(0, N):
        for j in range(0, M):
            if table[i][j] == '-1':
                continue
            else:
                # if matrix is 3*3 so this condition for index (0, 0) 
                if ( i == 0 and j == 0 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j+1] or
                    table[i][j] == table[i+1][j+1] or
                    table[i][j] == table[i+1][j] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                # if matrix is 3*3 so this condition for index (0, 1) 
                if ( i == 0 and j != 0 and i != N-1 and
                     j != M-1 and table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j-1] or
                    table[i][j] == table[i][j+1] or
                    table[i][j] == table[i+1][j-1] or
                    table[i][j] == table[i+1][j] or
                    table[i][j] == table[i+1][j+1] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                # if matrix is 3*3 so this condition for index (0, 2) 
                if ( i == 0 and j == M-1 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j-1] or
                    table[i][j] == table[i+1][j-1] or
                    table[i][j] == table[i+1][j] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                
                # if matrix is 3*3 so this condition for index (1, 0)
                if ( i != 0 and j == 0 and i != N-1 and j != M-1 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i-1][j] or
                    table[i][j] == table[i+1][j] or
                    table[i][j] == table[i][j+1] or
                    table[i][j] == table[i-1][j+1] or
                    table[i][j] == table[i+1][j+1] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                # if matrix is 3*3 so this condition for index (1, 1)
                if ( i != 0 and j != 0 and i != N-1 and j != M-1 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j-1] or
                    table[i][j] == table[i][j+1] or
                    table[i][j] == table[i-1][j-1] or
                    table[i][j] == table[i-1][j] or
                    table[i][j] == table[i-1][j+1] or
                    table[i][j] == table[i+1][j-1] or
                    table[i][j] == table[i+1][j] or
                    table[i][j] == table[i+1][j+1] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                # if matrix is 3*3 so this condition for index (1, 2)
                if ( i != 0 and j != 0 and i != N-1 and j == M-1 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j-1] or
                    table[i][j] == table[i-1][j] or
                    table[i][j] == table[i+1][j-1] or
                    table[i][j] == table[i+1][j] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                
                # if matrix is 3*3 so this condition for index (2, 0) 
                if ( j == 0 and i == N-1 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j+1] or
                    table[i][j] == table[i-1][j] or
                    table[i][j] == table[i-1][j+1] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                # if matrix is 3*3 so this condition for index (2, 1) 
                if ( i != 0 and j != 0 and i == N-1 and j != M-1 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j-1] or
                    table[i][j] == table[i][j+1] or
                    table[i][j] == table[i-1][j-1] or
                    table[i][j] == table[i-1][j] or
                    table[i][j] == table[i-1][j+1] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
                # if matrix is 3*3 so this condition for index (2, 2) 
                if ( i == N-1 and j == M-1 and
                     table[i][j] not in adjacents_checked ):
                    if ( table[i][j] == table[i][j-1] or
                    table[i][j] == table[i-1][j] or
                    table[i][j] == table[i-1][j-1] ):
                        differ_uni_adjacents += 1
                        adjacents_checked.append(table[i][j])
                        continue
    # print on a single line integer, the number of different universities
    #     having at least two of their teams adjacent to each other.
    print(differ_uni_adjacents)
