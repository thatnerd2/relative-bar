mat = [[0, 0, 0, 100],
       [0, 1, 0, 50],
       [0, 1, 1, 50]];

#Algo:
# Get 1 in the ith row of the jth col, then
# subtract multiples of that from the ith + 1 ... len(mat) rows.
# if no exist 1 in the ith row and jth col, then swap with somebody who does.

pivotRow = 0;
pivotCol = 0;
numRows = len(mat);
numCols = len(mat[0]);

for i in range(0, numCols - 1):
    if mat[pivotRow][pivotCol] == 0:
        # Enact swap with some row that does.
        
        for j in range(pivotRow + 1, numRows):
            # If some row contains a 1 in that column, interchange.
            if mat[j][pivotCol] != 0:
                temp = mat[j];
                mat[j] = mat[i];
                mat[i] = temp;
                break;
        else:
            # No row exists, so continue on. Assume a free variable.
            # For the relative bar program, possibly throw an error.
            pivotCol += 1;
            pivotRow += 1;
            continue;
                
    # Divide to get pivot row/col to be 1.
    for j in range (0, numCols):
        mat[pivotRow][j] /= float(mat[pivotRow][pivotCol]);

    # Subtract scaled pivot row from other non-zero leading rows.
    for j in range(0, numRows):
        if j == pivotRow: continue;

        scaledRow = [k * -1 * mat[j][pivotCol] for k in mat[pivotRow]];

        # Add the scaled row to the row in question, making at least the
        # same column entries in the row 0, leaving the pivot row intact.
        for k in range(0, numCols):
            mat[j][k] += scaledRow[k];
    pivotRow += 1;
    pivotCol += 1;
    
for row in mat:
    print row;
