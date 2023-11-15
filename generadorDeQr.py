import pyqrcode, png  # Copie "pip install pyqrcode pypng" y pegue en la terminal para instalar las librerias

link = "https://www."  # Ingrese el link que desea convertir en QR "El link tiene que estar dentro de las comillas"
qr_code = pyqrcode.create(link)
qr_code.png(
    "----nombre----.png",  # Ingrese le nombre con el cual desea guardar el QR 
                           # "El nombre tiene que estar dentro de las comillas y al final con .png"
    scale=8,  # Tamaño del del png o resolucion.
)
print("QR generado con éxito")