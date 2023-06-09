title = "learning new stuff take time , but Learning is enjoying work i love it"

# print encode
print(title.encode('utf-8','replace'))
# print decode
decoded_string = title.encode('utf-8','replace').decode()
print(decoded_string)

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
