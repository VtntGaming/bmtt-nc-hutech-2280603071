def demSoLanXuatHien(ds):
    countData = {}
    for item in ds:
        if item in countData:
            countData[item] += 1
        else:
            countData[item] = 1
    return countData

inputStr = input("Nhập d=s các từ, cách nhau bằng dấu cách:")
wordList = inputStr.split()

print("Số lần xuất hiện của các phần tử:",demSoLanXuatHien(wordList))