def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        raise ValueError("Division par zéro impossible")
    return x / y

while True:
    try:
        print("Options:")
        print("Tapez 'add' pour additionner deux nombres")
        print("Tapez 'sub' pour soustraire deux nombres")
        print("Tapez 'mul' pour multiplier deux nombres")
        print("Tapez 'div' pour diviser deux nombres")
        print("Tapez 'quit' pour quitter le programme")

        choix = input(": ")

        if choix == "quit":
            break

        if choix not in ("add", "sub", "mul", "div"):
            raise ValueError("Option invalide")

        num1 = float(input("Entrez le premier nombre: "))
        num2 = float(input("Entrez le deuxième nombre: "))

        if choix == "add":
            print("Résultat:", addition(num1, num2))
        elif choix == "sub":
            print("Résultat:", soustraction(num1, num2))
        elif choix == "mul":
            print("Résultat:", multiplication(num1, num2))
        elif choix == "div":
            print("Résultat:", division(num1, num2))

    except ValueError as e:
        print(f"Erreur: {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite: {e}")

