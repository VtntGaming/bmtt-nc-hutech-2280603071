import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()


data_to_hash = input("Bạn hãy nhập dữ liệu để hash bằng SHA-256: ")
sha256_result = calculate_sha256_hash(data_to_hash)
print(f"Mã băm SHA-256 của '{data_to_hash}' là: {sha256_result}")