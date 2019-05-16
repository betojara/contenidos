import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Ventana(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Ventana")
        self.setGeometry(200, 200, 400, 400)
        self.show()

app = QApplication(sys.argv)
ventana = Ventana()
label = QLabel("etiqueta", ventana) # ¿Le falta algo?
label.setGeometry(100, 100, 100, 100)
label.show()
sys.exit(app.exec())
