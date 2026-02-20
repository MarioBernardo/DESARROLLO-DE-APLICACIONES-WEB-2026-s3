from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenido al sistema web de Pacific Security Force"

# Institucional
@app.route('/nosotros')
def nosotros():
    return 'Pacific Security Force es una empresa especializada en seguridad privada en Ecuador.'

@app.route('/mision')
def mision():
    return 'Nuestra misión es brindar protección y confianza a nuestros clientes.'

@app.route('/vision')
def vision():
    return 'Ser la empresa líder en seguridad privada a nivel nacional.'

# Servicios
@app.route('/servicios')
def servicios():
    return 'Servicios: Vigilancia fija, Custodia armada, Seguridad electrónica.'

@app.route('/servicios/<tipo>')
def tipo_servicio(tipo):
    return f'Detalles del servicio de {tipo}.'

# Personal
@app.route('/personal')
def personal():
    return 'Listado general del personal de seguridad.'

@app.route('/personal/<int:id>')
def detalle_personal(id):
    return f'Detalles del guardia con ID {id}'

# Clientes
@app.route('/clientes')
def clientes():
    return 'Listado de clientes corporativos.'

@app.route('/clientes/<empresa>')
def cliente_empresa(empresa):
    return f'Información del cliente {empresa}'

# Contacto
@app.route('/contacto')
def contacto():
    return 'Contacto: info@pacificsecurity.com'

@app.route('/contacto/<ciudad>')
def contacto_ciudad(ciudad):
    return f'Oficina de Pacific Security Force en {ciudad}'

# Asignaciones
@app.route('/asignacion/<guardia>/<puesto>')
def asignacion(guardia, puesto):
    return f'El guardia {guardia} está asignado al puesto {puesto}.'

if __name__ == "__main__":
    app.run(debug=True)