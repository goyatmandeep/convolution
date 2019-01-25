import math
def flip(fil, f):
    i = 0
    while i<f//2:
        fil[i], fil[f-i-1] = fil[f-i-1], fil[i]
        i += 1
    i = 0
    j = 0
    while i < f:
        j = 0
        while j<f//2:
            fil[i][j], fil[i][f-j-1] = fil[i][f-j-1], fil[i][j]
            j += 1
        i += 1
    return fil

def convolute(inp, fil, n, f, s):
    m = int(math.floor((n-f)/s+1))
    if m<1:
        print('Ouput matrix is less than 1X1')
        exit(1)
    output = []
    for i in range(m):
        l = [0 for j in range(m)]
        output.append(l)
    row = 0
    col = 0
    for i in range(m):
        for j in range(m):
            tcol = col
            trow = row
            for k in range(f):
                for l in range(f):
                    output[i][j] += inp[trow][tcol]*fil[k][l]
                    tcol += 1
                trow += 1
                tcol = col
            if col + 1*s <= n-f:
                col += 1*s
            else:
                col = 0
                row += 1*s
    return output, m

def printmatrix(output, m):
    for i in range(m):
        for j in range(len(output[i])):
            print('%4d'%output[i][j], end=' ')
        print()

print("%60s"%'Convolution Operation')
f = int(input('Enter the filter size(odd) and elements(row by row)\n'))
if f<1:
    print('Error in input')
    exit(1)
fil = [0]*f                     # f is the filer size, fil is the filter matrix.
for i in range(f):
    fil[i] = list(input().split())
    fil[i] = [int(x) for x in fil[i]]
extend = False
p = int(input('Enter the number of layers of padding (enter 0 for no padding)\n'))
if p < 0:
    print('Error in input')
    exit(1)
elif p > 0:
    temp = int(input('Enter 1 for extended padding\nEnter 0 for weighted padding\n'))
    if temp == 0:
        w = int(input('Enter the weight of the padding\n'))
    elif temp == 1:
        extend = True
        w = 0
    else:
        print('Error in input')
        exit(1)
else:
    w = 0

s = int(input('Enter the stride(1 for default)\n'))
if s < 1:
    print('Error in input')
    exit(1)

n = int(input('Enter the input matrix size and elements(row by row)\n'))
if f > n:
    print('Invalid input')
    exit(1)
inp = []
for i in range(n+2*p):
    inp.append([w])                    # inp matrix is for the input.
for i in range(p):
    inp[i] = [w]*(n+2*p)
for i in range(n):
    l = [w]*p
    l += list(input().split())
    l += [w]*p
    inp[i+p] = [int(x) for x in l]
for i in range(n+p, n+2*p):
    inp[i] = [w]*(n+2*p)
if extend:
    for i in range(p):
        for j in range(p):
            inp[i][j] = inp[p][p]
    for i in range(p+n, 2*p+n):
        for j in range(p):
            inp[i][j] = inp[p+n-1][p]
    for i in range(p):
        for j in range(p+n-1, n+2*p):
            inp[i][j] = inp[p][p+n-1]
    for i in range(p+n-1, 2*p+n):
        for j in range(p+n-1, 2*p+n):
            inp[i][j] = inp[p+n-1][p+n-1]
    for i in range(0, p):
        for j in range(p, p+n):
            inp[i][j] = inp[p][j]
    for i in range(p, p+n):
        for j in range(p):
            inp[i][j] = inp[i][p]
    for i in range(n+p, 2*p+n):
        for j in range(p, p+n):
            inp[i][j] = inp[p+n-1][j]
    for i in range(p, p+n):
        for j in range(p+n, 2*p+n):
            inp[i][j] = inp[i][p+n-1]

print('\nInput matrix with padding (if applicable)\n')
printmatrix(inp, n+2*p)
n += 2*p                            # updating the value of n to n+2*p
fil = flip(fil, f)
output, m = convolute(inp, fil, n, f, s)
print('\nFilter matrix after flipping\n')
printmatrix(fil, f)
print('\nOutput of convolution\n')
printmatrix(output, m)
input('\nPress enter to exit\n')
