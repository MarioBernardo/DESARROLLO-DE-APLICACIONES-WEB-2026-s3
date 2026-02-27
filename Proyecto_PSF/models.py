import sqlite3

DB = "database.db"

def conectar():
    return sqlite3.connect(DB)

# ==================================================
# CLASE PRODUCTO
# ==================================================
class Producto:
    def __init__(self, id, nombre, cantidad, precio, categoria):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
        self._categoria = categoria

    # ===== GETTERS =====
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def get_categoria(self):
        return self._categoria

    # ===== SETTERS =====
    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio


# ==================================================
# CLASE INVENTARIO
# ==================================================
class Inventario:
    def __init__(self):
        # Diccionario {id: Producto}
        self.productos = {}

    # Cargar datos desde SQLite
    def cargar(self):
        self.productos.clear()

        conn = conectar()
        cursor = conn.cursor()

        # IMPORTANTE: ORDEN EXACTO DE COLUMNAS
        cursor.execute("SELECT id, nombre, cantidad, precio, categoria FROM productos")
        filas = cursor.fetchall()

        conn.close()

        for fila in filas:
            id, nombre, cantidad, precio, categoria = fila

            producto = Producto(
                id=id,
                nombre=nombre,
                cantidad=cantidad,
                precio=precio,
                categoria=categoria
            )

            self.productos[id] = producto

    # Añadir producto
    def añadir(self, nombre, cantidad, precio, categoria):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO productos (nombre, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?)
        """, (nombre, cantidad, precio, categoria))

        conn.commit()
        conn.close()

        self.cargar()

    # Eliminar producto
    def eliminar(self, id):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE id=?", (id,))

        conn.commit()
        conn.close()

        self.cargar()

    # Actualizar producto
    def actualizar(self, id, cantidad, precio):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE productos
            SET cantidad=?, precio=?
            WHERE id=?
        """, (cantidad, precio, id))

        conn.commit()
        conn.close()

        self.cargar()

    # Buscar producto por nombre (LISTA)
    def buscar(self, nombre):
        return [
            p for p in self.productos.values()
            if nombre.lower() in p.get_nombre().lower()
        ]

    # Mostrar todos (LISTA)
    def todos(self):
        return list(self.productos.values())

    # Categorías únicas (SET)
    def categorias_unicas(self):
        categorias = {p.get_categoria() for p in self.productos.values()}
        return sorted(categorias)   # ahora salen ordenadas


# ==================================================
# CREAR TABLAS
# ==================================================
def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# ==================================================
# PRECARGAR DATOS LIMPIOS
# ==================================================
def precargar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM productos")
    total = cursor.fetchone()[0]

    if total == 0:
        productos = [
            ("Radio Motorola", 10, 350.0, "Comunicación"),
            ("Chaleco Antibalas", 15, 500.0, "Protección"),
            ("Linterna Táctica", 25, 45.0, "Equipamiento"),
            ("Cámara CCTV", 8, 220.0, "Tecnología")
        ]

        cursor.executemany("""
            INSERT INTO productos (nombre, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?)
        """, productos)

    conn.commit()
    conn.close()