# 陣列
a = [[1, 2, 4],[3, 5, 7], [2, 4, 9]]
transposed_a=[]
# Transposing the matrix
for i in range(len(a[0])):
    row = []
    for j in range(len(a)):
        row.append(a[j][i])
    transposed_a.append(row)

#列印出轉換玩的陣列
for row in transposed_a:
    #刪掉括號跟逗號
    print(" ".join(map(str, row)))

#O(9)