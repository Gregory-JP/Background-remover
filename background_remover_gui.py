import tkinter as tk
from tkinter import filedialog
import cv2 as cv
from rembg import remove

def select_input_image():
    global input_path
    input_path = filedialog.askopenfilename(title = "Select input image")
    input_label.config(text = input_path)

def select_output_image():
    global output_path
    output_path = filedialog.asksaveasfilename(defaultextension = ".jpg", title = "Select output location")
    output_label.config(text = output_path)

def process_image():
    input_image = cv.imread(input_path)
    output = remove(input_image)
    cv.imwrite(output_path, output)
    result_label.config(text = "Image processed successfully!")



app = tk.Tk()
app.config(background="#90EE90", padx=50.0, pady=50.0)

app.title("Remove Background")
app.minsize(width=400, height=200)

input_label = tk.Label(text = "No input image selected.", foreground='black', background='#FFFACD')
input_label.pack()

input_button = tk.Button(text = "Select Input Image", command = select_input_image)
input_button.pack(pady=10)

output_label = tk.Label(text = "No output location selected.", foreground='black', background='#FFFACD')
output_label.pack()

output_button = tk.Button(text = "Select Output Location", command = select_output_image)
output_button.pack(pady=10)

process_button = tk.Button(text = "Process Image", command = process_image)
process_button.pack()

result_label = tk.Label(text = "", background="#90EE90", foreground='black')
result_label.pack()

app.mainloop()