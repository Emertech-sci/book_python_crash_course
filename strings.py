regard = "Hello World!"
print(regard)

name = "Jesus Mateo Rendon Avila"
print(name)

regards = f"{regard} my name is {name}."
print(regards)

#
# Strings
#
string_1 = 'String con milla simple'
string_2 = "String con comilla doble"
print(string_1)
print(string_2)

favorite = 'Python is my "favorite" programming language' # Strings con comilla simple y comillas dobles como caracteres
print(favorite)

favoreite_1 = "Pyhton is my \"favorite\" programming language" # Strings con comillas dobles y comillas dobles como caracteres
print(favoreite_1)

#
# Metodos de Strings
#
new_name = "ada lovelace"
print(new_name.title())
print(new_name.upper())
new_name = "ADA LOVELACE"
print(new_name.lower())

# Variables on Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
hello = f"Hello {full_name.title()}!"
print(hello)

# White spaces
print("Python")
print("\tPython")

print("Languages:\nPyhton\nC\nJava\nRust")
print("Languages:\n\tPyhton\n\tC\n\tJava\n\tRust")

# Strip white spaces
# Derecha
name = "Gonzalo "
last_name = "Menendez"
full_name = f"{name}{last_name}"
print(full_name)

name = name.rstrip()
full_name = f"{name}{last_name}"
print(full_name)

# Izquierda
name_1 = "Mercedes"
name_2 = " Benz"
full_car_name = f"{name_1}{name_2}"
print(full_car_name)

name_2= name_2.lstrip()
full_car_name = f"{name_1}{name_2}"
print(full_car_name)

# Ambos lados
messi_1 = "Lionel"
messi_2 = " Andres "
messi_3 = "Messi"
messi_name = f"{messi_1}{messi_2}{messi_3}" # messi_2 tiene espacios en ambos lados
print(messi_name)
messi_2 = messi_2.strip() # .strip() eliminara los dos espacios en blanco de messi_2
messi_name = f"{messi_1}{messi_2}{messi_3}"
print(messi_name)

# Remove prefixes
jugadores = 'Cristiano Ronaldo, Messi, Mbappe'
#jugadores.removeprefix('Cristiano ronaldo, ')
print(jugadores)
print(jugadores.removeprefix('Cristiano Ronaldo, '))

