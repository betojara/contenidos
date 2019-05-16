import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, \
                          QHBoxLayout, QVBoxLayout, QLineEdit

class CampoFormulario(QHBoxLayout):

    def __init__(self, texto, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = QLabel(f"{texto}: ")
        campo = QLineEdit("")
        self.addStretch(1)
        self.addWidget(label)
        self.addWidget(campo)
        self.addStretch(1)

class Ventana(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Ventana")
        self.setGeometry(200, 200, 400, 400)
        contenedor = QVBoxLayout()
        contenedor.addLayout(CampoFormulario("Usuario"))
        contenedor.addLayout(CampoFormulario("Contraseña"))
        self.setLayout(contenedor)
        self.show()

app = QApplication(sys.argv)
ventana = Ventana()
sys.exit(app.exec())
