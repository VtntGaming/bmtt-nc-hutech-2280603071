input_str = input("Nhập x, y: ")
dimension = [int(x) for x in input_str.split(',')]
rowNum=dimension[0]
colNum=dimension[1]
multiList = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multiList[row][col]= row*col
print(multiList)