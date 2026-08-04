

print(chr(65))
print(chr(97))  # 輸出：a
print(chr(48))  # 輸出：0

print(chr(21488))  # 輸出：台
print(chr(128522)) # 輸出：😊

alphabet=[chr(i) for i in range(65,91 )] # A-Z
print(alphabet)

char='C'
shift=3
new_char=chr(ord(char)+shift)
print(f'{char}向後推{shift}位是{new_char}')