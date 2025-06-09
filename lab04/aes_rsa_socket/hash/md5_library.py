import hashlib

def calculate_md5(imput_string):
    md5_hash = hashlib.md5()
    md5_hash.update(imput_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Nhập một văn bản cần băm: ")
md5_result = calculate_md5(input_string)

print(f"Mã băm của '{input_string}' là: {md5_result}")