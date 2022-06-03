
from cv2 import line


r = open('test.txt','w')
f = open('hola_mundo.txt','r')


for linea in f:
    linea = linea.rstrip()
    r.writelines(linea)
    r.write("\n")
    if linea.find("\n"):
        print("hola") 
    

print(type(linea))

f.close()
r.close()
