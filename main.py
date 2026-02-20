def saludar(nombre):
    return f"Hola, {nombre}. Bienvenido a GitHub 🚀"

def despedirse(nombre):
    return f"Hasta luego, {nombre}. Sigue programando 💻"

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    print(saludar(nombre))
    print(despedirse(nombre))