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