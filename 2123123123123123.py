import tkinter as tk
import random

class CountryCapitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Country Capital App")

        self.country_label = tk.Label(root, text="Enter Country:")
        self.country_entry = tk.Entry(root)

        self.capital_label = tk.Label(root, text="Enter Capital:")
        self.capital_entry = tk.Entry(root)

        self.result_label = tk.Label(root, text="Result:")
        self.result_display = tk.Label(root, text="")

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_random_country)

        # Grid layout
        self.country_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.country_entry.grid(row=0, column=1, padx=10, pady=10)

        self.capital_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.capital_entry.grid(row=1, column=1, padx=10, pady=10)

        self.result_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.result_display.grid(row=2, column=1, padx=10, pady=10)

        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_random_country(self):
        countries_capitals = {
            "Country1": "Capital1",
            "Country2": "Capital2",
            # Add more countries and capitals as needed
        }

        random_country = random.choice(list(countries_capitals.keys()))
        random_capital = countries_capitals[random_country]

        self.result_display.config(text=f"Random Country: {random_country}\nRandom Capital: {random_capital}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CountryCapitalApp(root)
    root.mainloop()
