import tkinter as tk
from tkinter import ttk, messagebox
import math

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lbs):
    return lbs / 2.20462

def grams_to_pounds(g):
    return g * 0.00220462

def pounds_to_grams(lbs):
    return lbs / 0.00220462

def ounces_to_grams(oz):
    return oz * 28.3495

def grams_to_ounces(g):
    return g / 28.3495

def newtons_to_grams(n):
    return n * 101.971621

def grams_to_newtons(g):
    return g / 101.971621

def pounds_to_newtons(lbs):
    return lbs * 4.4482216

def newtons_to_pounds(n):
    return n / 4.4482216

def inches_to_millimeters(inches):
    return inches * 25.4

def millimeters_to_inches(mm):
    return mm / 25.4

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def degrees_to_radians(deg):
    return deg * (math.pi / 180)

def radians_to_degrees(rad):
    return rad * (180 / math.pi)

def psi_to_bar(psi):
    return psi * 0.0689476

def bar_to_psi(bar):
    return bar / 0.0689476



class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        # self.root.geometry("600x400") # Let it resize automatically

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Headers
        ttk.Label(main_frame, text="English / Imperial", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(main_frame, text="Metric / SI", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=10)

        # Conversion Rows
        self.rows = []
        
        # Format: (Label1, Label2, ConvertFunc1to2, ConvertFunc2to1, Precision1, Precision2)
        self.conversions_setup = [
            ("Feet", "Meters", feet_to_meters, meters_to_feet, 4, 4),
            ("Pounds", "Kilograms", pounds_to_kilograms, kilograms_to_pounds, 4, 4),
            ("Pounds", "Newtons", pounds_to_newtons, newtons_to_pounds, 4, 4),
            ("Pounds", "Grams", pounds_to_grams, grams_to_pounds, 4, 2),
            ("Newtons", "Grams", newtons_to_grams, grams_to_newtons, 4, 4),
            ("Ounces", "Grams", ounces_to_grams, grams_to_ounces, 4, 2),
            ("Inches", "Millimeters", inches_to_millimeters, millimeters_to_inches, 4, 4),
            ("Fahrenheit", "Celsius", fahrenheit_to_celsius, celsius_to_fahrenheit, 2, 2),
            ("Degrees", "Radians", degrees_to_radians, radians_to_degrees, 4, 4),
            ("PSI", "Bar", psi_to_bar, bar_to_psi, 4, 4),
        ]

        for i, (label1, label2, func1, func2, prec1, prec2) in enumerate(self.conversions_setup):
            row_idx = i + 1
            
            # Labels
            ttk.Label(main_frame, text=label1).grid(row=row_idx, column=0, sticky="e", padx=5, pady=5)
            ttk.Label(main_frame, text=label2).grid(row=row_idx, column=3, sticky="w", padx=5, pady=5)

            # Entries
            var1 = tk.StringVar()
            var2 = tk.StringVar()
            
            entry1 = ttk.Entry(main_frame, textvariable=var1, width=15)
            entry2 = ttk.Entry(main_frame, textvariable=var2, width=15)
            
            entry1.grid(row=row_idx, column=1, padx=5, pady=5)
            entry2.grid(row=row_idx, column=2, padx=5, pady=5)

            # Store row data
            row_data = {
                "var1": var1,
                "var2": var2,
                "func1": func1, # 1 -> 2
                "func2": func2, # 2 -> 1
                "prec1": prec1,
                "prec2": prec2,
                "updating": False # Flag to prevent recursive updates
            }
            self.rows.append(row_data)

            # Bind events
            # Use lambda with default argument to capture current row_data
            entry1.bind("<KeyRelease>", lambda event, rd=row_data: self.on_entry1_change(rd))
            entry2.bind("<KeyRelease>", lambda event, rd=row_data: self.on_entry2_change(rd))

    def on_entry1_change(self, row_data):
        if row_data["updating"]: return
        
        val_str = row_data["var1"].get()
        if not val_str:
            row_data["updating"] = True
            row_data["var2"].set("")
            row_data["updating"] = False
            return

        try:
            val = float(val_str)
            result = row_data["func1"](val)
            
            row_data["updating"] = True
            # Special case for Inches (which is var1 in Inches->MM)
            # Wait, user asked for Inches accuracy to 4 decimal places. 
            # If Inches is var1, we are converting TO MM. 
            # If MM is var2, we convert TO Inches.
            # The precision stored is for the OUTPUT.
            
            # Actually, let's just use the stored precision for the target field
            prec = row_data["prec2"]
            row_data["var2"].set(f"{result:.{prec}f}")
            row_data["updating"] = False
        except ValueError:
            pass # Ignore invalid input while typing

    def on_entry2_change(self, row_data):
        if row_data["updating"]: return
        
        val_str = row_data["var2"].get()
        if not val_str:
            row_data["updating"] = True
            row_data["var1"].set("")
            row_data["updating"] = False
            return

        try:
            val = float(val_str)
            result = row_data["func2"](val)
            
            row_data["updating"] = True
            prec = row_data["prec1"]
            row_data["var1"].set(f"{result:.{prec}f}")
            row_data["updating"] = False
        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()
