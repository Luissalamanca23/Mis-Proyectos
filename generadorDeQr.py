import qrcode  # Copie "pip install pyqrcode" y pegue en la terminal para instalar las librerias
import flet as ft

#link = "https://www.senadis.gob.cl/"  # Ingrese el link que desea convertir en QR "El link tiene que estar dentro de las comillas"
#qr_code = pyqrcode.create(link)
#qr_code.png(
    #"QR senadis.png",  # Ingrese le nombre con el cual desea guardar el QR 
                           # "El nombre tiene que estar dentro de las comillas y al final con .png"
    #scale=20,  # Tamaño del del png o resolucion.
#)
#print("QR generado con éxito")

def main(page: ft.Page):
    

    def btn_click(e):
        # Generate QR code
        codigo_qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        codigo_qr.add_data(texto.value)
        imagen_qr = codigo_qr.make_image(fill_color="black",
                                        back_color="white")

        # Save QR code image
        imagen_qr.save("codigo_qr.png")

        # Display QR code image
        imagen_col.controls.append(ft.Image(
                                            src=f"codigo_qr.png",
                                            width=400,
                                            height=400,
                                            fit=ft.ImageFit.CONTAIN,
                                            ))
        page.update()
        
    # Create input field for text
    texto = ft.TextField(label="Input Text")

    # Create button to generate QR code
    boton = ft.ElevatedButton("Generate QR Code")
    boton.on_click = btn_click

    # Create column to display generated QR code image
    imagen_col = ft.Column(expand=1,wrap=False, scroll='AUTO')

    # Add elements to page
    page.add(texto,
            boton,
            imagen_col)

ft.app(target=main)