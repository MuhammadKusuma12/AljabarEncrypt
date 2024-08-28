# JUDUL: Penggunaan matriks dalam pembuatan enkripsi dalam pemrograman python

import numpy as np

inputan = input("input text:")

# mengubah string ke kode ascii dan memasukkan ke list
def textToAscii(text):
    return [ord(char) for char in text]
    
# mengubah kode ascii char dan menggabungkan menjadi string
def asciiToText(asciiCode):
    return ''.join(chr(code) for code in asciiCode)
    
# membuat matrix dari input dan mengalikannya dengan matrix dan memasukkan ke list
def encript(asciiCode, matrix):
    while len(asciiCode) % len(matrix) != 0:
        asciiCode.append(0)

    asciiMatrix = np.array(asciiCode).reshape(len(matrix), -1)
    kaliMatrix = np.dot(matrix, asciiMatrix)
    return kaliMatrix.flatten().astype(int).tolist()
    
# rumus matrix
matrix = np.array([[1,4,6],
                [2,3,4],
                [1,2,5]])
                
asciiCode = textToAscii(inputan)
encryptMatrix = encript(asciiCode, matrix)
textEncrypt = asciiToText(encryptMatrix)

print(textEncrypt)
    
    
    
    