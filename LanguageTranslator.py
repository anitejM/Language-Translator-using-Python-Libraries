import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

def translate_text():
    sentence = text_entry.get("1.0", tk.END).strip()
    target_language = language_var.get().lower()

    if not sentence or target_language not in languages:
        messagebox.showerror("Error", "Please provide both sentence and a valid language")
        return

    try:
        translated_text = translator.translate(sentence, dest=languages[target_language]).text
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize translator
translator = Translator()

# Supported languages
languages = {
    'hindi': 'hi',
    'french': 'fr',
    'german': 'de',
    'spanish': 'es',
    'bengali': 'bn',
    'chinese (prc)': 'zh-CN',
    'japanese': 'ja',
    'arabic': 'ar'
}

# Initialize Tkinter 
root = tk.Tk()
root.title("Language Translation System")

# Create the Interface
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter sentence in English:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
text_entry = tk.Text(frame, height=5, width=50, wrap=tk.WORD)
text_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(frame, text="Select target language:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
language_var = tk.StringVar()
language_combobox = ttk.Combobox(frame, textvariable=language_var)
language_combobox['values'] = list(languages.keys())
language_combobox.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

translate_button = ttk.Button(frame, text="Translate", command=translate_text)
translate_button.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

ttk.Label(frame, text="Translated Sentence:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
result_text = tk.Text(frame, height=5, width=50, wrap=tk.WORD, state='normal')
result_text.grid(row=3, column=1, padx=10, pady=10)

# Styling/Designing
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=6)
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TCombobox', font=('Helvetica', 12))
text_entry.configure(font=('Helvetica', 12))
result_text.configure(font=('Helvetica', 12))

# Running the Tkinter event loop
root.mainloop()