def xoaPT(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
dir = {'a':1,'b':2,'c':3, 'd':4}
keyDelete = 'b'
result = xoaPT(dir,keyDelete)


print(result and f"DS sau khi xoá: {dir}" or "DS không tìm thấy key để xoá")