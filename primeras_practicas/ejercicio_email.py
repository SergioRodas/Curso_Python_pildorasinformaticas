email = input("Por favor, introduzca una dirección de email: ")
cantidad_arroba = email.count("@")

while cantidad_arroba != 1 or email.index("@") == 0 or email.index("@") == len(email) - 1:
    print("La dirección ingresada es incorrecta.")
    email = input("Por favor, introduzca una dirección de email: ")

print("La dirección de email es correcta.")

    
