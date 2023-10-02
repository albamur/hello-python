"""
El doctor de cabecera del hospital de tu cuidad te 
ha pedido ayuda para crear un programa que registre
los datos principales de las recetas de sus pacientes.
Debes crear un programa que recoja los siguientes datos:
- Nombre y apellidos del doctor
- Nombre y apellidos del paciente
- Edad
- Sexo
- Nombre del medicamento
- Cantidad
- Nº de veces a dia
"""

print("\n------------ REGISTRO DE RECETAS ------------\n")
docName = input('¿Cuál es su nombre, doctor/a? ')
print("\nBienvenido/a, doctor/a", docName)
print("\nResponda la siguientes preguntas:")
patientName = input('¿Nombre de el/la paciente?: ')
patientAge = input('¿Edad de el/la paciente?: ')
patientSex = input('¿Sexo de el/la paciente?: ')
medicineName = input('¿Nombre del medicamento?: ')
medicineCant = input('¿Dosis del medicamento?: ')
medicineTimes = input('¿Nº de veces que debe tomar el medicamento al día?: ')
print("\n\n")

print("------------ VOLANTE RECETA ------------\n")
print("Nombre y apellidos del doctor:",docName)
print("Nombre y apellidos del paciente:",patientName)
print("Edad:",patientAge)
print("Sexo:",patientSex)
print("Nombre del medicamento:",medicineName)
print("Cantidad:",medicineCant)
print("Nº de veces a dia:",medicineTimes)
print("----------------------------------------\n")