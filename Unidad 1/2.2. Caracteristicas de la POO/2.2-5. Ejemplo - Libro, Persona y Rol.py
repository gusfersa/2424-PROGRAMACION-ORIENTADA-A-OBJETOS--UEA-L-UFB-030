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


class Person:
    """Representa una persona en la biblioteca, ya sea un usuario o un bibliotecario."""

    def __init__(self, name, role):
        """Inicializa una nueva persona con un nombre y un rol."""
        self.name = name
        self.role = role  # 'user' o 'librarian'
        if self.role == 'user':
            self.borrowed_books = []

    def borrow_book(self, book):
        """Permite a la persona pedir prestado un libro (si es un usuario)."""
        if self.role == 'user':
            if not book.is_borrowed:
                book.borrow()
                self.borrowed_books.append(book)
                print(f"{self.name} ha pedido prestado el libro: {book.title}")
            else:
                print(f"El libro {book.title} no está disponible.")

    def return_book(self, book):
        """Permite a la persona devolver un libro (si es un usuario)."""
        if self.role == 'user':
            if book in self.borrowed_books:
                book.return_book()
                self.borrowed_books.remove(book)
                print(f"{self.name} ha devuelto el libro: {book.title}")
            else:
                print(f"{self.name} no tiene el libro: {book.title}")

    def manage_book(self, book, action):
        """Gestiona las acciones de prestar o devolver un libro (si es un bibliotecario)."""
        if self.role == 'librarian':
            if action == 'borrow':
                return book.borrow()
            elif action == 'return':
                book.return_book()


# Ejemplo de uso
libro1 = Book("Cien años de soledad", "Gabriel García Márquez", "1234567890")
bibliotecario = Person("Juan", "librarian")
usuario = Person("Ana", "user")

usuario.borrow_book(libro1)  # Ana pide prestado el libro
usuario.return_book(libro1)  # Ana devuelve el libro

print(libro1)