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
