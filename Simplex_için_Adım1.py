#Serdar Gürler
# İlk 3x3 matrix
X = [[8,7,1],
    [4 ,5,3],
    [7 ,5,2]]
# İkinci 3x4 matrix
Y = [[5,6,1,2],
    [3,-1,3,2],
    [2,0,2,1]]
# Sonuç_Matrisi 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
# iterasyon
for i in range(len(X)):
   # Y sütun iterasyonu
   for j in range(len(Y[0])):
       # Y satır iterasyonu
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)