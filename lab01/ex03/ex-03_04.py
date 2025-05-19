def truyCapPT(tupleData):
    firstElement = tupleData[0]
    lastElement = tupleData[-1]
    return firstElement, lastElement

inputTuple = eval(input("Nhập tuple [ex: (1,2,3)]:"))
first,last = truyCapPT(inputTuple)

print(f"Phần tử đầu tiên: {first}\nPhần tử cuối cùng: {last}")