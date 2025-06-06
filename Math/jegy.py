D = [[1,6,3],

    [4 ,5,6],

    [2 ,8,9]]

C = [[1,4,1],

    [3,2,3],

    [1,3,9]]

result = [[0,0,0],

         [0,0,0],

         [0,0,0]]

# iterate through rows

for x in range(len(D)):

   # iterate through columns

   for y in range(len(C[0])):

       result[x][y] = D[x][y] + C[x][y] + 0

for q in result:

   print(q)
