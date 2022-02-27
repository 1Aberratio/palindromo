# @author: Jairo Benavides Pasos

palabra = input("Ingrese una palabra, frase u oración: ")
palabraOriginal = palabra.upper()
palabra = palabra.lower()
signos = "¿?¡!,.:;'*´(){}[]-—_@#$%±=></"

for losSignos in palabra:    
    if losSignos in signos:
        palabra = palabra.replace(losSignos,"") 
        
palabra1 = palabra.replace(" ","")

a,b = "áéíóúü","aeiouu"
acento = str.maketrans(a,b)
letras_unidas = palabra1.translate(acento)
print("Todas las letras juntas:",letras_unidas)

if letras_unidas == letras_unidas[::-1]:
    print(f'{palabraOriginal} => sí es un palíndromo.')
else:
    print(f'{palabraOriginal} => no es un palíndromo.')