import os

def run_script(script_name):
    os.system(f'python {script_name}.py')

def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Charger les données")
        print("2. Visualiser les données")
        print("3. Définir et afficher le modèle")
        print("4. Entraîner le modèle")
        print("5. Tester le modèle")
        print("6. Quitter")

        choice = input("Choisissez une option : ")

        if choice == '1':
            run_script('data_loader')
        elif choice == '2':
            run_script('visualize')
        elif choice == '3':
            run_script('model')
        elif choice == '4':
            run_script('train')
        elif choice == '5':
            run_script('test')
        elif choice == '6':
            print("Fermeture du programme.")
            break
        else:
            print("Choix invalide, essayez encore.")

if __name__ == "__main__":
    menu()
