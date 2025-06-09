# Helper functions
def left_rotate(x, c):
    return (x << c | x >> (32 - c)) & 0xFFFFFFFF

# Giải thuật md5
def md5(message):
    if isinstance(message, str):
        message = message.encode('utf-8')  # Chuyển đổi chuỗi sang bytes nếu cần

    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    original_length = len(message) # Độ dài ban đầu tính theo bit
    message += b'\x80'  # Append a single '1' bit (0x80 in hex)
    while len(message) % 64 != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, 'little')  # Append the original length in bits

    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]

        words = [int.from_bytes(chunk[j:j + 4], 'little') for j in range(0, 64, 4)]
        a, b, c, d = a0, b0, c0, d0  # Khởi tạo giá trị cho mỗi vòng lặp

        # Vòng lặp chính
        for j in range(64):
            if j < 16:
                f = (b & c) | (~b & d)
                g = j
            elif j < 32:
                f = (d & b) | (~d & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)
            a = temp

        a = (a + a0) & 0xFFFFFFFF
        b = (b + b0) & 0xFFFFFFFF
        c = (c + c0) & 0xFFFFFFFF
        d = (d + d0) & 0xFFFFFFFF
    # Trả về giá trị băm cuối cùng

    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

input_message = input("Nhập một văn bản nào đó: ")
md5_hash = md5(input_message)
print(f"Mã hàm băm md5: {md5_hash}")