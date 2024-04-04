import numpy as np
import pandas as pd
from shiny import ui

np.random.seed(42)
patient_ids = [f"Patient {i}" for i in range(1, 11)]
dates = pd.date_range(start="2023-01-01", periods=12, freq="M")
measurements = ["Cholesterol", "Blood Pressure", "Glucose"]
views = {"graph": "Visualization","summary":  "Statistical Summary", "table": "Patient Data Table"}

data = {
    (patient, measurement): np.random.randint(100, 200, size=len(dates)) + np.random.randn(len(dates))
    for patient in patient_ids for measurement in measurements
}

df = pd.DataFrame(data, index=dates)

dynamic_ui_elements = {
    'graph_type': ui.input_radio_buttons("graph_type", "Select Graph Type", choices=["Line Plot", "Histogram"],
                                       selected="Line Plot"),
    'stats': ui.input_checkbox_group("stats", "Summary Stats", choices=measurements, selected=measurements)
}


