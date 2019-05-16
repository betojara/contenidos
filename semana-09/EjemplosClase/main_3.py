import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QGridLayout, QPushButton, QVBoxLayout)


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.etiqueta1 = QLabel('Texto a modificar', self)
        self.grilla = QGridLayout()

        valores = ['0', '1']        
        posiciones = [(0,0),(0,1)]
        
        for i in range(2):
            boton = QPushButton(valores[i])
            # Conectamos el evento clicked con la función
            boton.clicked.connect(self.boton_clickeado)
            self.grilla.addWidget(boton, *posiciones[i])
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.etiqueta1)
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)
        self.setWindowTitle('Emit signal')
        self.show()


        
    def boton_clickeado(self):

        # Sender retorna el objeto que fue clickeado.
        boton = self.sender()

        # Obtenemos el identificador del elemento en la grilla
        idx = self.grilla.indexOf(boton)

        # Con el identificador obtenemos la posición del ítem en la grilla
        posicion = self.grilla.getItemPosition(idx)

        # Actualizamos label1
        self.etiqueta1.setText(f'Presionado boton {idx}, en fila/columna: {posicion[:2]}.')

app = QApplication(sys.argv)
ex = Ventana()
sys.exit(app.exec_())