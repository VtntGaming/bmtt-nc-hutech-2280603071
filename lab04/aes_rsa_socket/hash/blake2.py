import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    text = input("Nhập văn bản cần băm BLAKE2: ").encode('utf-8')
    hash_result = blake2(text)
    
    print(f"Mã băm BLAKE2 của '{text.decode('utf-8')}' là: {hash_result.hex()}")
    
if __name__ == "__main__":
    main()