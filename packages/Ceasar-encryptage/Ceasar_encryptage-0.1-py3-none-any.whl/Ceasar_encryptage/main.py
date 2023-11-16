get_text = input("Veuillez entrer un message: ")
key = 3
clef = int(input("veuillez entrer une cle de codage:"))
text = []
text_decrypt =[]
for i in get_text:
    if clef != key:
        print("veuillez entrer une autre clef:")
        clef
        break
    text.append(ord(i)+key)

for i in text:
    text_decrypt.append(chr(i))
txt = "".join(text_decrypt)
print(txt)
while True:
    cleff = int(input("entrer la clef de decodage:"))
    if cleff == key:
 #le decryptage:
      text = [(ord(i)-key) for i in txt ]
      text_decrypt = [chr(i) for i in text]
      tex = "".join(text_decrypt)
      print(tex)
      break
    else:
        print("vous avez pas l'autorisation requise pour voir ce message")
        break

