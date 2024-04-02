import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import data_init as data


# TODO 5: create a method that will update the patient data
#  1.  Get the current dataframe (patients) from the df_reactive (to get the value of the reactive Value use .get()
#           method).
#  2.  If a file_info is present (csv_file was uploaded), read the csv file using the method read_csv from
#           the pandas library (pd.). The file path is stored in the file_info on the index 0, mapped to a "datapath"
#           key (use file_info[0]["datapath"]). When reading the file, set the header to rows 0 and 1.
#   3.  In the data module, there is a list of patient ids (data.patient_ids), append to this list the patient id
#           (method .append), that is stored in the first row and the first column of the header (.columns) of the new
#           dataframe, that was read from the csv file.
#   4.  Set the index of the new dataframe to the same as the current_df (get the index using df.index). Use "inplace"
#           attribute set to True.
#   5.  Concatenate the current_df with the new_data. In order to do this, you first need to create a list containing
#           these 2 dataframes. Use attribute axis=1 as the Patients' data is stored as columns, not rows.
#   6.  Set operation result string to inform the user that the Data were read from the CSV file
#  7.  Else (if file_info is not present) append the patient_id from the input to the patient_ids
#   8.  For each measurement from the data.measurements list create a random values and assign them to a patient
#           and his measurement (for the value generation us the code below).
#   9.  Set operation result string to inform the user that the Data were generated.
#  10.  Set the df_reactive to current_df (.set())
#  11.  Return the operation result String

# Code for 8. step
# current_df[(new_patient_id, measurement)] = np.random.randint(100, 200, size=len(data.dates)) + np.random.randn(
#                 len(data.dates)) * 15

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
