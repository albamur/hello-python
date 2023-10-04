'''
Escribir un programa que pregunte nombre y apellidos del usuario en 
la consola y muestre por pantalla otro correo electrónico con el mismo 
nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''

print("\n------------ LOGIN INTRANET ------------\n")
name = input('Introduce tu nombre y apellido: ')

user_name = name[:name.find(" ")].lower().capitalize()
user_last_name = name[name.find(" ")+1:].lower().capitalize()
user = user_name + " " + user_last_name

email = name.lower().replace(" ",".")

print(f"Bienvedino/a a la intranet, tu usuario será: {user} tu email será: {email}@gmail.com")