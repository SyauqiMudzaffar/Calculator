from stegano import lsb
import os
from tkinter import Tk, Label, Button, filedialog, Entry, Text, messagebox
from PIL import Image

# Warna Palet
BACKGROUND_COLOR = "#2b2b2b"  # Hitam
TEXT_COLOR = "#ff0000"  # Merah
BUTTON_COLOR = "#3b3b3b"  # Abu-abu gelap

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganografi Tool")
        self.root.geometry("600x400")
        self.root.configure(bg=BACKGROUND_COLOR)

        # Judul
        self.title_label = Label(root, text="Steganografi Tool", font=("Helvetica", 18, "bold"), fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
        self.title_label.pack(pady=10)

        # Tombol Sembunyikan Pesan
        self.hide_button = Button(root, text="Sembunyikan Pesan", command=self.hide_message_gui, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 14))
        self.hide_button.pack(pady=10)

        # Tombol Tampilkan Pesan
        self.show_button = Button(root, text="Tampilkan Pesan", command=self.show_message_gui, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 14))
        self.show_button.pack(pady=10)

        # Tombol Keluar
        self.exit_button = Button(root, text="Keluar", command=root.quit, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 14))
        self.exit_button.pack(pady=10)

    def get_image_path(self):
        return filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg")])

    def convert_to_png(self, img_path):
        if img_path.endswith('.jpg'):
            img = Image.open(img_path)
            png_path = img_path.rsplit('.', 1)[0] + ".png"
            img.save(png_path)
            return png_path
        return img_path

    def save_image_path(self):
        return filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])

    def hide_message_gui(self):
        img_path = self.get_image_path()
        if not img_path or not os.path.exists(img_path):
            messagebox.showerror("Error", "Path gambar tidak valid.")
            return

        img_path = self.convert_to_png(img_path)
        if not img_path.endswith('.png'):
            messagebox.showerror("Error", "Format file tidak didukung.")
            return

        # Input pesan
        input_window = Tk()
        input_window.title("Masukkan Pesan")
        input_window.configure(bg=BACKGROUND_COLOR)

        Label(input_window, text="Masukkan Pesan:", bg=BACKGROUND_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12)).pack(pady=10)
        message_entry = Text(input_window, height=5, width=40, bg=BUTTON_COLOR, fg=TEXT_COLOR)
        message_entry.pack(pady=10)

        def submit_message():
            message = message_entry.get("1.0", "end").strip()
            input_window.destroy()
            save_path = self.save_image_path()
            if not save_path:
                return
            try:
                secret = lsb.hide(img_path, message)
                secret.save(save_path)
                messagebox.showinfo("Success", f"Pesan berhasil disembunyikan dalam gambar. Gambar disimpan di: {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")

        Button(input_window, text="Simpan", command=submit_message, bg=BUTTON_COLOR, fg=TEXT_COLOR, font=("Helvetica", 12)).pack(pady=10)
        input_window.mainloop()

    def show_message_gui(self):
        img_path = self.get_image_path()
        if not img_path or not os.path.exists(img_path):
            messagebox.showerror("Error", "Path gambar tidak valid.")
            return

        img_path = self.convert_to_png(img_path)
        try:
            clear_message = lsb.reveal(img_path)
            if clear_message:
                messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
            else:
                messagebox.showinfo("Info", "Tidak ada pesan tersembunyi dalam gambar ini.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menampilkan pesan: {e}")

# Main Program
if __name__ == "__main__":
    root = Tk()
    app = SteganographyApp(root)
    root.mainloop()
