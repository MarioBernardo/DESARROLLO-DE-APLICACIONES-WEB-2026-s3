from flask import Flask, render_template, request, redirect, url_for
from models import db, Servicio
from inventario.persistencia import leer_txt, leer_json, leer_csv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Crear base de datos
with app.app_context():
    db.create_all()

# ===============================
# PAGINAS PRINCIPALES
# ===============================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


# ===============================
# SERVICIOS (CRUD CON SQLALCHEMY)
# ===============================

@app.route("/servicios")
def servicios():

    servicios = Servicio.query.all()

    return render_template(
        "servicios.html",
        servicios=servicios
    )


@app.route("/servicio/<int:id>")
def detalle_servicio(id):

    servicio = Servicio.query.get_or_404(id)

    return render_template(
        "detalle_servicio.html",
        servicio=servicio
    )


@app.route("/agregar", methods=["POST"])
def agregar():

    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]

    nuevo = Servicio(
        nombre=nombre,
        descripcion=descripcion
    )

    db.session.add(nuevo)
    db.session.commit()

    return redirect(url_for("servicios"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    servicio = Servicio.query.get_or_404(id)

    if request.method == "POST":

        servicio.nombre = request.form["nombre"]
        servicio.descripcion = request.form["descripcion"]

        db.session.commit()

        return redirect(url_for("servicios"))

    return render_template(
        "editar.html",
        servicio=servicio
    )


@app.route("/eliminar/<int:id>")
def eliminar(id):

    servicio = Servicio.query.get_or_404(id)

    db.session.delete(servicio)
    db.session.commit()

    return redirect(url_for("servicios"))


# ===============================
# CLIENTES
# ===============================

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

    return render_template(
        "clientes.html",
        clientes=lista_clientes
    )


# ===============================
# PERSONAL
# ===============================

@app.route("/personal")
def personal():
    return render_template("personal.html")


# ===============================
# CONTACTO
# ===============================

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


# ===============================
# INVENTARIO (TXT JSON CSV)
# ===============================

@app.route("/inventario")
def inventario():

    txt = leer_txt()
    json_data = leer_json()
    csv_data = leer_csv()

    return render_template(
        "inventario.html",
        txt=txt,
        json=json_data,
        csv=csv_data
    )


# ===============================

if __name__ == "__main__":
    app.run(debug=True)