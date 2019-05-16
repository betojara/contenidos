import sys
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QLineEdit, \
                            QPushButton
from PyQt5.QtGui import QFont

class Perfil(QWidget):
    def __init__(self, *args):
        super().__init__(*args)
        self.setWindowTitle("Perfil")
        self.setFixedSize(300, 250)

        self.nombre = ""
        self.ocupacion = ""
        self.nacionalidad = ""

        self.crear_ventana_principal()
        self.crear_ventana_edicion()

        self.boton_editar = QPushButton("Editar", self)
        self.boton_editar.move(50, 200)
        self.boton_editar.clicked.connect(self.editar)

        self.boton_actualizar = QPushButton("Actualizar", self)
        self.boton_actualizar.move(150, 200)
        self.boton_actualizar.clicked.connect(self.actualizar)
        # self.boton_actualizar.setEnabled(False)
        self.boton_actualizar.hide() # alternativa


    def crear_ventana_principal(self):

        self.label_perfil = QLabel("Perfil:", self)
        self.label_perfil.move(50, 50)
        self.label_nombre = QLabel("", self)
        self.label_nombre.move(50, 80)
        self.label_descripcion = QLabel("-", self)
        self.label_descripcion.move(50, 110)

        self.label_perfil.setFont(QFont("Helvetica", 16))
        self.label_nombre.setFont(QFont("Helvetica", 20))
        self.label_descripcion.setFont(QFont("Helvetica", 16))


    def crear_ventana_edicion(self):

        self.label_input_1 = QLabel("Nombre:", self)
        self.label_input_2 = QLabel("Nacionalidad:", self)
        self.label_input_3 = QLabel("Ocupación:", self)
        self.label_input_1.move(50, 50)
        self.label_input_2.move(50, 70)
        self.label_input_3.move(50, 90)

        self.input_1 = QLineEdit("", self)
        self.input_2 = QLineEdit("", self)
        self.input_3 = QLineEdit("", self)
        self.input_1.move(150, 50)
        self.input_2.move(150, 70)
        self.input_3.move(150, 90)

        self.label_input_1.hide()
        self.label_input_2.hide()
        self.label_input_3.hide()
        self.input_1.hide()
        self.input_2.hide()
        self.input_3.hide()


    def editar(self):
        self.label_input_1.show()
        self.label_input_2.show()
        self.label_input_3.show()
        self.input_1.show()
        self.input_2.show()
        self.input_3.show()

        self.label_perfil.hide()
        self.label_nombre.hide()
        self.label_descripcion.hide()

        # self.boton_editar.setEnabled(False)
        self.boton_editar.hide() # alternativa
        # self.boton_actualizar.setEnabled(True)
        self.boton_actualizar.show() # alternativa

    def actualizar(self):

        self.nombre = self.input_1.text()
        self.nacionalidad = self.input_2.text()
        self.ocupacion = self.input_3.text()

        self.label_nombre.setText(self.nombre)
        self.label_descripcion.setText(
            f"{self.ocupacion} - {self.nacionalidad}")

        self.label_input_1.hide()
        self.label_input_2.hide()
        self.label_input_3.hide()
        self.input_1.hide()
        self.input_2.hide()
        self.input_3.hide()

        self.label_perfil.show()
        self.label_nombre.show()
        self.label_descripcion.show()

        # self.boton_editar.setEnabled(True)
        self.boton_editar.show() # alternativa
        # self.boton_actualizar.setEnabled(False)
        self.boton_actualizar.hide() # alternativa

if __name__ == "__main__":
    app = QApplication(sys.argv)
    perfil = Perfil()
    perfil.show()
    sys.exit(app.exec())
