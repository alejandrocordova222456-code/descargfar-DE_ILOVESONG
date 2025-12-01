import tkinter as tk
from tkinter import ttk, messagebox
import requests
import random

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def saludar():
    link_bruto = entry_nombre.get().strip()

    if link_bruto == "":
        messagebox.showwarning("Advertencia", "Ingresa un link primero.")
        return

    if "ilovesong.ai/work/" not in link_bruto:
        messagebox.showerror("Error", "El link no es válido.")
        return

    try:
        messagebox.showinfo("Descarga", "Descarga iniciada...")
        id_audio = link_bruto.split("work/")[1]
        print(id_audio[8:-1])
        link_descarga = f"https://cdn9.ilovesong.ai/audios/{id_audio[8:]}.mp3"
        print(link_descarga)
        response = requests.get(link_descarga, stream=True)
        nombre_archivo = f"musica_{random.randint(1,9999999)}.mp3"

        with open(nombre_archivo, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        messagebox.showinfo("Completado", f"Archivo descargado como:\n{nombre_archivo}")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error:\n{e}")

root = tk.Tk()
root.title("Descargar Música")
centrar_ventana(root, 400, 230)

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="DESCARGAR LA MUSIQUITA", font=("Arial", 16)).pack(pady=10)
ttk.Label(frame, text="INGRESA EL LINK A DESCARGAR:").pack(pady=(5, 2))

entry_nombre = ttk.Entry(frame, width=35)
entry_nombre.pack(pady=5)

ttk.Button(frame, text="Descargar", command=saludar).pack(pady=15)

root.mainloop()
