from Crypto.Hash import SHA3_256

def sha3(msg):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(msg)
    return sha3_hash.digest()

def main():
    text = input("Nhập văn bản cần băm SHA-3: ").encode('utf-8')
    hash_result = sha3(text)
    
    print(f"Mã băm SHA-3 của '{text.decode('utf-8')}' là: {hash_result.hex()}")
    
if __name__ == "__main__":
    main()