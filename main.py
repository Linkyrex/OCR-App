'''
This is the main file of the OCR Mac app.
It handles the user interface and coordinates the functionality of other modules.
'''
import tkinter as tk
from tkinter import filedialog
from ocr import OCR
class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Mac App")
        self.file_path = tk.StringVar()
        self.text_output = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        # File selection button
        file_button = tk.Button(self.root, text="Select Image", command=self.select_image)
        file_button.pack(pady=10)
        # Text output label
        text_label = tk.Label(self.root, textvariable=self.text_output)
        text_label.pack(pady=10)
        # OCR button
        ocr_button = tk.Button(self.root, text="OCR", command=self.perform_ocr)
        ocr_button.pack(pady=10)
    def select_image(self):
        self.file_path.set(filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")]))
    def perform_ocr(self):
        ocr = OCR()
        text = ocr.process_image(self.file_path.get())
        self.text_output.set(text)
if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()