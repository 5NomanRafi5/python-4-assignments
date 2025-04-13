import streamlit as st

st.set_page_config(page_title="Smart Unit Converter", page_icon="🔄")

st.title("🔄 Smart Unit Converter")

# Supported units and their base conversion to meters
units = {
    "Kilometers": 1000,
    "Meters": 1,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Feet": 0.3048,
    "Inches": 0.0254
}

# Dropdowns for unit selection
from_unit = st.selectbox("Select the unit you want to convert from:", list(units.keys()))
to_unit = st.selectbox("Select the unit you want to convert to:", list(units.keys()))

# Value input
value = st.number_input(f"Enter value in {from_unit}:", min_value=0.0, step=0.1)

# Conversion logic
if st.button("Convert"):
    value_in_meters = value * units[from_unit]  # convert from source to meters
    result = value_in_meters / units[to_unit]   # convert from meters to target

    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
