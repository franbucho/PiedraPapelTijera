import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def jugar_piedra_papel_tijera(jugador, computadora):
    if jugador == computadora:
        return "Empate", computadora

    if (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):
        return "Ganaste", computadora
    else:
        return "Perdiste", computadora

class JuegoPiedraPapelTijera:
    def __init__(self, master):
        self.master = master
        self.master.title("Piedra, Papel o Tijera")

        self.opciones = ["piedra", "papel", "tijera"]

        self.label_resultado = tk.Label(master, text="", font=("Helvetica", 16))
        self.label_resultado.pack(pady=20)

        self.frame_opciones = tk.Frame(master)
        self.frame_opciones.pack()

        self.imagenes = {
            "piedra": self.cargar_imagen('piedra.png'),
            "papel": self.cargar_imagen('papel.png'),
            "tijera": self.cargar_imagen('tijera.png'),
        }

        for opcion in self.opciones:
            button = tk.Button(self.frame_opciones, image=self.imagenes[opcion], command=lambda o=opcion: self.jugar(o))
            button.image = self.imagenes[opcion]
            button.pack(side=tk.LEFT, padx=10)

        self.boton_nuevo_juego = tk.Button(master, text="Nuevo Juego", command=self.nuevo_juego)
        self.boton_nuevo_juego.pack(pady=10)

        self.contador_victorias = {"piedra": 0, "papel": 0, "tijera": 0}

    def cargar_imagen(self, nombre_archivo):
        ruta_completa = f'C:/Users/Admin/Desktop/sure lock & key/Piedra Papel Tijera/{nombre_archivo}'
        imagen = Image.open(ruta_completa)
        return ImageTk.PhotoImage(imagen)

    def jugar(self, opcion_usuario):
        opcion_computadora = random.choice(self.opciones)
        resultado, opcion_computadora = jugar_piedra_papel_tijera(opcion_usuario, opcion_computadora)

        mensaje = f"Tú elegiste: {opcion_usuario}\nLa computadora eligió: {opcion_computadora}\nResultado: {resultado}"
        self.label_resultado.config(text=mensaje)

        if resultado == "Perdiste":
            self.contador_victorias[opcion_computadora] += 1

        if messagebox.askyesno("Juego Terminado", f"{mensaje}\n¿Quieres jugar de nuevo?"):
            self.label_resultado.config(text="")
        else:
            self.master.destroy()

    def nuevo_juego(self):
        self.contador_victorias = {"piedra": 0, "papel": 0, "tijera": 0}
        messagebox.showinfo("Nuevo Juego", "Se ha reiniciado el contador de victorias.")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoPiedraPapelTijera(root)
    root.mainloop()
