from flask import Flask, render_template, request, redirect, url_for
from models import *

app = Flask(__name__)

crear_tablas()
precargar()

inventario = Inventario()
inventario.cargar()

# ===============================
# PAGINAS PRINCIPALES
# ===============================

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/servicios")
def servicios():
    servicios_lista = [
        {"id": 1, "nombre": "Seguridad Física"},
        {"id": 2, "nombre": "Monitoreo CCTV"},
        {"id": 3, "nombre": "Consultoría en Seguridad"}
    ]
    return render_template("servicios.html", servicios=servicios_lista)

@app.route("/servicio/<int:id>")
def detalle_servicio(id):
    descripciones = {
        1: "Protección empresarial y residencial.",
        2: "Monitoreo 24/7 con tecnología avanzada.",
        3: "Análisis y planificación estratégica."
    }

    servicio = descripciones.get(id)

    if not servicio:
        return "Servicio no encontrado", 404

    return render_template("detalle_servicio.html",
                           descripcion=servicio)

@app.route("/clientes")
def clientes():

    lista_clientes = [
        "Edificio Vertice",
        "Edificio Grand Victoria",
        "Edificio Baviera",
        "Edificio Aurus",
        "Edificio Century Plaza 1",
        "Edificio Avinthia",
        "Condominios Montreal",
        "CPN",
        "CR Constructora",
        "Edificio Austria",
        "Piazzara"
    ]

    return render_template("clientes.html", clientes=lista_clientes)

@app.route("/personal")
def personal():
    return render_template("personal.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# ===============================
# INVENTARIO
# ===============================

@app.route("/inventario")
def inventario_view():
    inventario.cargar()
    return render_template(
        "inventario.html",
        productos=inventario.todos(),
        categorias=inventario.categorias_unicas()
    )

@app.route("/agregar", methods=["POST"])
def agregar():
    inventario.añadir(
        request.form["nombre"],
        int(request.form["cantidad"]),
        float(request.form["precio"]),
        request.form["categoria"]
    )
    return redirect(url_for("inventario_view"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    inventario.eliminar(id)
    return redirect(url_for("inventario_view"))

@app.route("/editar/<int:id>")
def editar(id):
    inventario.cargar()
    producto = inventario.productos.get(id)
    if not producto:
        return "Producto no encontrado", 404
    return render_template("editar.html", producto=producto)

@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    inventario.actualizar(
        id,
        int(request.form["cantidad"]),
        float(request.form["precio"])
    )
    return redirect(url_for("inventario_view"))

@app.route("/buscar", methods=["POST"])
def buscar():
    inventario.cargar()
    resultados = inventario.buscar(request.form["nombre"])
    return render_template(
        "inventario.html",
        productos=resultados,
        categorias=inventario.categorias_unicas()
    )

if __name__ == "__main__":
    app.run(debug=True)