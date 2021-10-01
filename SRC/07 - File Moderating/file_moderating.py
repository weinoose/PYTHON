"""
[TR]
a - Dosyaya bir yazı eklemek için kullanılır. Okuma işlemi gerçekleştirmez.
w - Dosyayının içeriğini siler ve sıfırdan bir yazı ekler. Okuma işlemi gerçekleştirmez.
r - Dosyayı okumak için kullanılır. Yazma işlemi gerçekleştirmez.

"""

"""
[ENG]
a - Used to add a text to the file. It does not perform a reading operation.
w - Deletes the contents of the file and adds a text from scratch. It does not perform a reading operation.
r - Used to read the file. It does not write.

"""

file = open("demo1.txt", "r", encoding="UTF-8")
file.close()