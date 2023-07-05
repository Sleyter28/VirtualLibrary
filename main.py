# This is a sample Python script.
from book import Book
from employee import Employee
from user import User

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
employees = []
books = []
users = []


def start():
    is_running = True
    menu = {
        '1': "Cargar empleados",
        '2': "Registrar libros",
        '3': "Ver listado de libros",
        '4': "Buscar por título",
        '5': "Registrar usuario",
        'S': "Salir"
    }
    # Use a breakpoint in the code line below to debug your script.
    while is_running:
        options = sorted(menu.keys())

        for entry in options:
            print(entry, menu[entry])

        selection = input("Seleccione una opción: \n")
        if selection == "1":
            create_employee_from_file("employee.txt")
        elif selection == "2":
            request_book_data()
        elif selection == "3":
            get_all_books()
        elif selection == "4":
            search_book_by_title()
        elif selection == "5":
            register_user()
        elif selection == "S" or selection == "s":
            is_running = False
            break


def create_employee_from_file(path):
    with open(path, "r") as filestream:
        for line in filestream:
            current_line = line.split(",")

            employee = Employee(current_line[0], current_line[1], current_line[2], current_line[3], current_line[4],
                                current_line[5])
            employees.append(employee)


def request_book_data():
    title = input("Ingrese el título del libro:\n")
    author = input("Ingrese el autor del libro:\n")
    publishing_house = input("Ingrese la editorial del libro:\n")
    publication_year = input("Ingrese el año de publicación del libro:\n")
    genre = input("Ingrese el género del libro:\n")
    description = input("Ingrese la descripción del libro:\n")

    register_book(title, author, publishing_house, publication_year, genre, description)


def register_book(title, author, publishing_house, publication_year, genre, description):
    new_book = Book(title, author, publishing_house, publication_year, genre, description)
    books.append(new_book)


def get_all_books():
    for book in books:
        print("The book title is: ", book.title)


def search_book_by_title():
    title = input("Ingrese el título del libro:\n")
    result = next((obj for obj in books if obj.title == title))
    print(f'El título del libro es: {result.title}')


def register_user():
    name = input("Ingrese el nombre del usuario:\n")
    address = input("Ingrese la dirección del usuario:\n")
    phone = input("Ingrese el teléfono del usuario:\n")
    user = User(name, address, phone)
    users.append(user)
    print_user()


def print_user():
    for user in users:
        print("El nombre del usuario es: " + user.name + ", la dirección es: " + user.address + ", el teléfono es: " + user.phone)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
