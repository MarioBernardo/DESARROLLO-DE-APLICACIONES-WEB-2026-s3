from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

# Acerca de
@app.route("/about")
def about():
    return render_template("about.html")

# Servicios
@app.route("/servicios")
def servicios():
    lista_servicios = [
        "Vigilancia",
        "Custodia",
        "Seguridad Electronica"
    ]
    return render_template("servicios.html", servicios=lista_servicios)

# Ruta dinámica de servicios
@app.route("/servicio/<tipo>")
def detalle_servicio(tipo):
    tipo = tipo.lower()
    return render_template("detalle_servicio.html", tipo=tipo)

# Clientes
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
        "CPN"
    ]
    return render_template("clientes.html", clientes=lista_clientes)

# Personal
@app.route("/personal")
def personal():
    guardias = [
        {"nombre": "Olmedo Bernardo Maldonado", "cargo": "Gerente General"},
        {"nombre": "Dayanara Quishpe", "cargo": "Jefa de Talento Humano"},
        {"nombre": "David Bernardo", "cargo": "Jefe de Operaciones"},
        {"nombre": "Franklin Parra", "cargo": "Supervisor"},
        {"nombre": "Rafael Quishpe", "cargo": "Supervisor"},
        {"nombre": "Diego Tipantuña", "cargo": "Guardia"},
        {"nombre": "Damian Velez", "cargo": "Guardia"},
        {"nombre": "David Velez", "cargo": "Guardia"},
        {"nombre": "Vinicio Caizapanta", "cargo": "Guardia"},
        {"nombre": "Humberto Cachihuango", "cargo": "Guardia"},
        {"nombre": "Anderson Delgado", "cargo": "Guardia"},
        {"nombre": "Carmen Unda", "cargo": "Guardia"},
        {"nombre": "Stalin Pangay", "cargo": "Guardia"},
        {"nombre": "Franklin Mendez", "cargo": "Guardia"},
        {"nombre": "Lenin Cevallos", "cargo": "Guardia"},
        {"nombre": "Erick Fernandez", "cargo": "Guardia"}
    ]
    return render_template("personal.html", guardias=guardias)

# Contacto con formulario
@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    mensaje_confirmacion = None

    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["correo"]
        mensaje_confirmacion = f"Gracias {nombre}, hemos recibido tu mensaje. Te contactaremos pronto."

    return render_template("contacto.html", mensaje=mensaje_confirmacion)


if __name__ == "__main__":
    app.run(debug=True)