from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
    print("Creando Controlador Mesa")

    def index(self):
    print("Listar todas las Mesas")

    def create(self,elMesa):
    print("Crear una Mesa")

    def show(self,id):
    print("Mostrando una Mesa con id ", id)

    def update(self, id, elMesa):
    print("Actualizando Mesa con id ", id)

    def delete(self, id):
    print("Elimiando Mesa con id ", id)