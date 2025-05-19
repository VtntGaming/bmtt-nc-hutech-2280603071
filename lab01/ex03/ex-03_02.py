def dao_nguoc_ds(lst):
    return lst[::-1]

input_list = input("Nhập ds các số, cách nhau bằng dấu phẩy: ");
numbers = list(map(int, input_list.split(',')))

ds_dao_nguoc = dao_nguoc_ds(numbers)
print("Ds sau khi dao nguoc:", ds_dao_nguoc)