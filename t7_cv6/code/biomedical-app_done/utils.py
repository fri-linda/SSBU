import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import data_init as data

def update_patient_data(df_reactive, new_patient_id, file_info):
    current_df = df_reactive.get()
    if file_info:
        new_data = pd.read_csv(file_info[0]["datapath"], header=[0, 1])
        data.patient_ids.append(new_data.columns[0][0])
        new_data.set_index(df_reactive.get().index, inplace=True)
        current_df = pd.concat([current_df, new_data], axis=1)
        operation_result = f"Patient Data for {data.patient_ids[-1]} read from CSV successfully"
    else:
        data.patient_ids.append(new_patient_id)
        for measurement in data.measurements:
            current_df[(new_patient_id, measurement)] = np.random.randint(100, 200,
                                                                          size=len(data.dates)) + np.random.randn(
                len(data.dates)) * 15
        operation_result = f"Patient Data for {data.patient_ids[-1]} generated successfully"
    df_reactive.set(current_df)
    return operation_result

def simulate_data_update(df):
    latest_date = df.index.max() + pd.DateOffset(months=1)
    new_data = {
        (patient, measurement): [np.random.randint(100, 200) + np.random.randn()]
        for patient in data.patient_ids for measurement in data.measurements
    }
    new_df_row = pd.DataFrame(new_data, index=[latest_date])
    return pd.concat([df, new_df_row])


def generate_statistical_summary(patient_id, stats, df_reactive):
    summary_str = ""
    for measurement in stats:
        measurement_data = df_reactive.get().loc[:, (patient_id, measurement)]
        desc = measurement_data.describe()
        stats_lines = [
            f"| Count: {desc['count']:>10.0f} |",
            f"Mean: {desc['mean']:>10.2f} |",
            f"Std: {desc['std']:>10.2f} |",
            f"Min: {desc['min']:>10.2f} |",
            f"25%: {desc['25%']:>10.2f} |",
            f"50%: {desc['50%']:>10.2f} |",
            f"75%: {desc['75%']:>10.2f} |",
            f"Max: {desc['max']:>10.2f} |",
        ]
        measurement_summary = f"{measurement} Summary:\n" + "\n".join(stats_lines) + "\n\n"
        summary_str += measurement_summary
    return summary_str


def create_plot(patient_id, measurement_type, filtered_data, graph_type):
    fig, ax = plt.subplots()

    if graph_type == "Line Plot":
        ax.plot(filtered_data.index, filtered_data)
    elif graph_type == "Histogram":
        ax.hist(filtered_data, bins=15)

    ax.grid(True, which='both')
    ax.set_title(f"{measurement_type} for {patient_id}")
    ax.set_xlabel("Date" if graph_type == "Line Plot" else "Value Range")
    ax.set_ylabel(measurement_type)
    plt.tight_layout()
    return fig
