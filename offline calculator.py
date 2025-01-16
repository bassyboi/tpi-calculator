import tkinter as tk
from tkinter import messagebox

def calculate_tpi():
    try:
        cape = int(cape_var.get())
        shear = int(shear_var.get())
        lightning = int(lightning_var.get())
        updraft = int(updraft_var.get())
        precip = int(precip_var.get())

        tpi = cape + shear + lightning + updraft + precip

        if tpi <= 10:
            interpretation = "Weak to Moderate Thunderstorm Potential"
        elif tpi <= 15:
            interpretation = "Strong Storm Potential (could be locally severe)"
        elif tpi <= 20:
            interpretation = "Severe Storm Potential (large hail, damaging winds, maybe tornadoes)"
        else:
            interpretation = "Extreme Storm Potential (significant severe threat)"

        result_message = (
            f"TPI Calculation Result:\n"
            f"  CAPE Factor (C): {cape}\n"
            f"  Shear Factor (S): {shear}\n"
            f"  Lightning Factor (L): {lightning}\n"
            f"  Updraft Strength (U): {updraft}\n"
            f"  Precipitation Core (P): {precip}\n"
            f"  Total TPI: {tpi}\n\n"
            f"Interpretation: {interpretation}"
        )

        messagebox.showinfo("TPI Result", result_message)

    except ValueError:
        messagebox.showerror("Input Error", "Please select a value for all factors.")

# Initialize main window
root = tk.Tk()
root.title("Thunderstorm Power Index (TPI) Calculator")

# Create input variables
cape_var = tk.StringVar(value="1")
shear_var = tk.StringVar(value="1")
lightning_var = tk.StringVar(value="1")
updraft_var = tk.StringVar(value="1")
precip_var = tk.StringVar(value="1")

# Create UI components
instructions = tk.Label(root, text="Select values (1-5) for each factor and click Calculate.")
instructions.pack(pady=10)

factors_frame = tk.Frame(root)
factors_frame.pack(pady=10)

# CAPE Factor
cape_label = tk.Label(factors_frame, text="CAPE Factor (C):")
cape_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
cape_menu = tk.OptionMenu(factors_frame, cape_var, "1", "2", "3", "4", "5")
cape_menu.grid(row=0, column=1, padx=5, pady=5)

# Shear Factor
shear_label = tk.Label(factors_frame, text="Shear Factor (S):")
shear_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
shear_menu = tk.OptionMenu(factors_frame, shear_var, "1", "2", "3", "4", "5")
shear_menu.grid(row=1, column=1, padx=5, pady=5)

# Lightning Factor
lightning_label = tk.Label(factors_frame, text="Lightning Factor (L):")
lightning_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
lightning_menu = tk.OptionMenu(factors_frame, lightning_var, "1", "2", "3", "4", "5")
lightning_menu.grid(row=2, column=1, padx=5, pady=5)

# Updraft Strength Factor
updraft_label = tk.Label(factors_frame, text="Updraft Strength (U):")
updraft_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
updraft_menu = tk.OptionMenu(factors_frame, updraft_var, "1", "2", "3", "4", "5")
updraft_menu.grid(row=3, column=1, padx=5, pady=5)

# Precipitation Core Factor
precip_label = tk.Label(factors_frame, text="Precipitation Core (P):")
precip_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
precip_menu = tk.OptionMenu(factors_frame, precip_var, "1", "2", "3", "4", "5")
precip_menu.grid(row=4, column=1, padx=5, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate TPI", command=calculate_tpi)
calculate_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
