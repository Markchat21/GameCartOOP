# Los juegos disponibles con su precio en peronios
games = {
    "FIFA 23": 10000.00,
    "CALL OF DUTY: WARZONE": 8000.00,
    "ASSASSIN'S CREED VALHALLA": 7000.00,
    "MINECRAFT": 2000.00,
    "RESIDENT EVIL 4": 8999.99,
    "THE WITCHER 3": 2500.00,
    "AMONGUS": 400.00,                      # SUS
    "HITMAN 3": 4000.00
}


# Clase library, la biblioteca de juegos y padre de la clase cart
class Library:
    def __init__(self):
        self.my_library = {}

    def show_library(self):
        print("BIBLIOTECA")
        for game in self.my_library.keys():
            print(f'{game}')
        print("\n")


# La clase del carrito de compras con sus metodos
class Cart(Library):
    def __init__(self):
        Library.__init__(self)
        self.my_cart = {}
        self.total_price = 0

    def add_game(self, my_game):
        self.my_cart.update({my_game: games[my_game]})
        print("Juego agregado correctamente al carrito\n")

    def remove_game(self, my_game):
        self.my_cart.pop(my_game)
        print("Juego eliminado correctamente del carrito\n")

    def show_cart(self):
        print("CARRITO DE COMPRAS")
        for game, value in self.my_cart.items():
            print(f'{game}: {value}')
            self.total_price += value
        print(f'Precio total: {self.total_price}')
        print('\n')

    def buy_cart(self):
        self.total_price = sum(self.my_cart.values())
        self.my_library = dict(self.my_cart)
        self.my_cart.clear()
        print(f'Se ha pagado un total de {self.total_price} peronios\n'
              f'Los elementos del carrito han sido agregados a su biblioteca con exito\n')


# Funcion para manejar las excepciones
def error_handling():
    my_choice = input("Ingrese la opcion: \n")
    try:
        my_choice = int(my_choice)
    except TypeError as type_err:
        print(f'Error: {type_err}')
        return 1
    except ValueError as value_err:
        print(f'Error: {value_err}')
        return 1
    else:
        if choice_handling(my_choice) == 6:     # Se llama a la funcion con las decisiones al mismo
            return 0                            # tiempo que se verifica si se detiene el programa
        else:
            return 1


# Funcion para manejar las decisiones del usuario
def choice_handling(choice):
    if 0 < choice < 3:
        while True:
            new_game = input("Ingrese el juego: \n").upper()
            if new_game in games:
                if choice == 1:
                    if new_game in user_cart.my_cart:
                        print("El juego ya esta en el carrito\n")
                        continue
                    elif new_game in user_cart.my_library:
                        print("El juego ya esta en la biblioteca\n")
                        continue
                    else:
                        user_cart.add_game(new_game)
                else:
                    if new_game in user_cart.my_cart:
                        user_cart.remove_game(new_game)
                    else:
                        print("El juego no se encuentra en el carrito\n")
                        continue
                break
            else:
                print("El juego no esta disponible\n")
                continue
    elif choice == 3:
        user_cart.show_cart()
    elif choice == 4:
        user_cart.buy_cart()
    elif choice == 5:
        user_cart.show_library()
    elif choice == 6:
        print("Hasta la proximaaaaaaa")
        return 6
    else:
        print("Opción invalida\n")
        return


# Instanciamos la clase Cart como un usuario
user_cart = Cart()

while True:
    print("CATALOGO DE VIDEOJUEGOS")
    for name, price in games.items():
        print(f'{name}: {price}')
    print("\n"
          "Opciones: \n"
          "1- Agregar juego al carrito\n"
          "2- Eliminar juego del carrito\n"
          "3- Mostrar carrito\n"
          "4- Comprar todos los juegos del carrito\n"
          "5- Mostrar biblioteca de juegos\n"
          "6- Salir del programa")
    if error_handling() == 1:
        continue
    else:
        break
