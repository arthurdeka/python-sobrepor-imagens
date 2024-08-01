import os
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image, ImageTk
import customtkinter

class ImageOverlayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicador de Imagem Sobreposta")
        self.root.configure(bg="#1c1c1c")
        self.folder_path = ""
        self.overlay_image_path = ""
        
        # Label de Status
        self.status_label = customtkinter.CTkLabel(
            root,
            text="        Selecione uma pasta de fotos e uma imagem a ser sobreposta.        ",
            bg_color="#1c1c1c",
            fg_color="#1c1c1c",
            )
        self.status_label.pack(pady=10)
        
        # Botão para selecionar a pasta
        self.select_folder_btn = customtkinter.CTkButton(
            root,
            command=self.select_folder,
            text="Selecionar Pasta de Fotos",
            font=("Arial", 14),
            text_color="#ffc905",
            hover=True,
            hover_color="#363636",
            height=30,
            border_width=2,
            corner_radius=9,
            border_color="#ffc905",
            bg_color="#1c1c1c",
            fg_color="#1c1c1c",
            )
        self.select_folder_btn.pack(pady=5)
        
        # Botão para selecionar a imagem sobreposta
        self.select_overlay_btn = customtkinter.CTkButton(
            root,
            text="Selecionar Imagem Sobreposta",
            command=self.select_overlay_image,
            font=("Arial", 14),
            text_color="#ffc905",
            hover=True,
            hover_color="#363636",
            height=30,
            border_width=2,
            corner_radius=9,
            border_color="#ffc905",
            bg_color="#1c1c1c",
            fg_color="#1c1c1c",
            )
        self.select_overlay_btn.pack(pady=5)
        
        # Botão para aplicar a imagem sobreposta
        self.apply_overlay_btn = customtkinter.CTkButton(
            root,
            text="Aplicar Sobreposição",
            command=self.apply_overlay,
            state='disabled',
            font=("Arial", 14),
            text_color="#947400",
            hover=True,
            hover_color="#363636",
            height=30,
            width=95,
            border_width=2,
            corner_radius=9,
            border_color="#947400",
            bg_color="#1c1c1c",
            fg_color="#1c1c1c",
            
            )
        self.apply_overlay_btn.pack(pady=5)
    
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.status_label.configure(text=f"Pasta selecionada: {self.folder_path}")
            self.check_ready_state()
    
    def select_overlay_image(self):
        self.overlay_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.overlay_image_path:
            self.status_label.configure(text=f"Imagem sobreposta selecionada: {self.overlay_image_path}")
            self.check_ready_state()
    
    def check_ready_state(self):
        if self.folder_path and self.overlay_image_path:
            self.apply_overlay_btn.configure(state='normal')
    
    def apply_overlay(self):
        try:
            overlay_image = Image.open(self.overlay_image_path).convert("RGBA")
            for file_name in os.listdir(self.folder_path):
                file_path = os.path.join(self.folder_path, file_name)
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                    base_image = Image.open(file_path).convert("RGBA")
                    base_image.paste(overlay_image, (0, 0), overlay_image)
                    base_image = base_image.convert("RGB") # Converte de volta para RGB
                    save_path = os.path.join(self.folder_path, f"overlaid_{file_name}")
                    base_image.save(save_path)
            messagebox.showinfo("Sucesso", "A imagem sobreposta foi aplicada em todas as fotos.")
            self.status_label.configure(text="Sobreposição aplicada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
            self.status_label.configure(text="Erro ao aplicar a sobreposição.")

if __name__ == "__main__":
    root = Tk()
    app = ImageOverlayApp(root)
    root.mainloop()
