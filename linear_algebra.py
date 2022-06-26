import random 
import math 
import numpy as np


# creer la matrice encrypte en s'assurant qu'elle est une matrice carre et que son inverse existe
# avec le module numpy on peut verifier si le determinant est different de 0 avec la linalg.det

X = np.random.randint(1, 26, size=(2, 2))

def determinant(matrixA): 
    if ((np.linalg.det(matrixA))%2 != 0) or ((np.linalg.det(matrixA))%13 != 0): 
        return matrixA
    else:
        matrixA = np.random.randint(1, 26, size=(2, 4))
        determinant(matrixA) 
        
        
        
#  on va travailler le message que l'utilisateur va rentrer pour pouvoir creer une matrice B avec en faisant correspondre chaque lettre a sa valeur numerique
#  

N = 2
texte  = str(input("Enter the message you would like to encrypt: "))

if len(texte )%2 != 0: 
    texte  = texte  + ' '

num_list = [ord(char) - 96 for char in texte ] # Assigner chaque lettre a son chiffre respectif grace a ASSCI code

matrixB = [num_list[i:i+N] for i in range(0, len(num_list), N)]


# Encrypter le message 

matrixC = []
encod_matrix = determinant(X)
inverse_matrix = np.linalg.inv(encod_matrix)
for j in range(len(matrixB)): 
     matrixC.append(np.matmul(encod_matrix, matrixB[j])) # multipliant la matrice A par la matrice pour obtenir une matrice C qui est encrypter
     
     
# Remettre la matrice C en format texte pour pouvoir envoyer le message crypter 

encrypted_modlist = [] 
for k in range(len(matrixB)): 
    encrypted_modlist.append(matrixC[k]%26)
    

    
total_list = [] 
for a in encrypted_modlist: 
    for b in a: 
        total_list.append(b)


final = [] 
for num in total_list: 
    final.append(chr(num + 96))

final_encrypt = "".join(final) #convertir une liste en string 

print('le texte code est : ', final_encrypt)


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

#decryption

# on va decrypter le texte grace a l'inverse de la matrice A si A x B = C B etant le texte tranforme en matrice pour retrouver ce texte 
# on peut dire que inverse de A x C = B qui est le texte original


decrypt = []
decrypt_list = []

for h in range(len(matrixC)):
    decrypt.append(np.matmul(inverse_matrix, matrixC[h]))
    
for arr in decrypt:
    for values in arr:
        decrypt_list.append(round(values))

decode_message = []

for y in decrypt_list:
    decode_message.append(chr(y + 96))
    
final_decode = " ".join(decode_message)

print(f'le texte decode est : {final_decode}')

