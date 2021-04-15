#Multiply two 2x2 matrices
def multiply2x2matrices(a, b): 
    try:
        c = [[0, 0], [0, 0], [0, 0]]
        row1 = len(a)
        col1 = len(a[0])
        row2 = len(b)
        col2 = len(b[0])

        for i in range(0, row1):
            for j in range(0, col2):
                for k in range(0, col1):
                    c[i][j] += a[i][k] * b[k][j]

        return c
    except:
        error = {
            'error': 'Input is invalid'
        }
        return error

#Multiply two 3x3 matrices
def multiply3x3matrices(a, b): 
    try:
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        row1 = len(a)
        col1 = len(a[0])
        row2 = len(b)
        col2 = len(b[0])

        for i in range(0, row1):
            for j in range(0, col2):
                for k in range(0, col1):
                    c[i][j] += a[i][k] * b[k][j]

        return c
    except:
        error = {
            'error': 'Input is invalid'
        }
        return error
        
        
#Add two 2x2 matrices
def add2x2matrices(a, b): 
    try:
        c = [[0, 0], [0, 0]]
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                c[i][j] += a[i][j] + b[i][j]
                print(i, j)
        return c

    except:
        error = {
            'error': 'Invalid input'
        }
        return error

#Add two 3x3 matrices
def add3x3matrices(a, b): 
    try:
        c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(0, len(a)):
            for j in range(0, len(a)):
                c[i][j] += a[i][j] + b[i][j]
                print(i, j)
        return c

    except:
        error = {
            'error': 'Invalid input'
        }
        return error

