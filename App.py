import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class LanguageTranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Translator")
        
        self.create_widgets()

    def create_widgets(self):
        # Input Text Area
        self.input_text_area = tk.Text(self, height=5, width=50)
        self.input_text_area.grid(row=0, column=0, padx=10, pady=10)

        # Source Language Dropdown
        source_language_label = tk.Label(self, text="Source Language:")
        source_language_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.source_language = ttk.Combobox(self, values=["auto", "en", "fr", "es", "de", "hi", "zh-CN"])
        self.source_language.set("auto")
        self.source_language.grid(row=1, column=1, padx=10, pady=5)

        # Target Language Dropdown
        target_language_label = tk.Label(self, text="Target Language:")
        target_language_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.target_language = ttk.Combobox(self, values=["en", "fr", "es", "de", "hi", "zh-CN"])
        self.target_language.set("en")
        self.target_language.grid(row=2, column=1, padx=10, pady=5)

        # Translate Button
        translate_button = tk.Button(self, text="Translate", command=self.translate_text)
        translate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Translated Text Area
        self.translated_text_area = tk.Text(self, height=5, width=50)
        self.translated_text_area.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def translate_text(self):
        input_text = self.input_text_area.get("1.0", "end-1c")
        source_lang = self.source_language.get()
        target_lang = self.target_language.get()

        translator = Translator()
        translated_text = translator.translate(input_text, src=source_lang, dest=target_lang)

        self.translated_text_area.delete("1.0", "end")
        self.translated_text_area.insert("1.0", translated_text.text)

if __name__ == "__main__":
    app = LanguageTranslatorApp()
    app.mainloop()
