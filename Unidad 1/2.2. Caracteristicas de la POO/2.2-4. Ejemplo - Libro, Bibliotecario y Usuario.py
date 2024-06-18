class Book:
    """Representa un libro en la biblioteca."""

    def __init__(self, title, author, isbn):
        """Inicializa un nuevo libro con título, autor e ISBN."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        """Presta el libro si no está actualmente prestado."""
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        """Devuelve el libro a la biblioteca."""
        self.is_borrowed = False

    def __str__(self):
        """Devuelve una representación en cadena del libro."""
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"


class Librarian:
    """Representa un bibliotecario en la biblioteca."""

    def __init__(self, name):
        """Inicializa un nuevo bibliotecario con un nombre."""
        self.name = name

    def manage_book(self, book, action):
        """Gestiona las acciones de prestar o devolver un libro."""
        if action == 'borrow':
            return book.borrow()
        elif action == 'return':
            book.return_book()


class User:
    """Representa un usuario de la biblioteca."""

    def __init__(self, name):
        """Inicializa un nuevo usuario con un nombre."""
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book, librarian):
        """Permite al usuario pedir prestado un libro."""
        if librarian.manage_book(book, 'borrow'):
            self.borrowed_books.append(book)
            print(f"{self.name} ha pedido prestado el libro: {book.title}")
        else:
            print(f"El libro {book.title} no está disponible.")

    def return_book(self, book, librarian):
        """Permite al usuario devolver un libro."""
        if book in self.borrowed_books:
            librarian.manage_book(book, 'return')
            self.borrowed_books.remove(book)
            print(f"{self.name} ha devuelto el libro: {book.title}")
        else:
            print(f"{self.name} no tiene el libro: {book.title}")


# Ejemplo de uso
libro1 = Book("Cien años de soledad", "Gabriel García Márquez", "1234567890")
bibliotecario = Librarian("Juan")
usuario = User("Ana")

usuario.borrow_book(libro1, bibliotecario)  # Ana pide prestado el libro
usuario.return_book(libro1, bibliotecario)  # Ana devuelve el libro
