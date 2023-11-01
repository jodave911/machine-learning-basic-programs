A=[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

B=[[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

result=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,len(A)):
    for j in range(0, len(B[0])):
        for k in range(0, len(B)):
            result[i][j]=A[i][j]*B[j][i]
for r in result:
    print(r)

