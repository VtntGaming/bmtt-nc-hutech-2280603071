def tao_tuple_tu_ds(lst):
    return tuple(lst)

input_list = input("Nhập ds các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

print("List:",numbers)
print("Tuple:",  tao_tuple_tu_ds(numbers))
