class ServicioForm:

    def __init__(self, form):

        self.nombre = form.get("nombre")
        self.descripcion = form.get("descripcion")

    def validar(self):

        if not self.nombre:
            return False

        if not self.descripcion:
            return False

        return True