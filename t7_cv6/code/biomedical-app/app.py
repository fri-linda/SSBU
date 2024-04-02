from shiny import App, render, reactive
import pandas as pd

import app_ui as shiny_ui
import data_init as data
import utils


def server(input, output, session):
    df_reactive = reactive.Value(data.df)
    conditional_ui = reactive.Value(None)
    txt_status = reactive.Value("")

    # INPUTS

    # TODO 4: create a @reactive.Effect to add the New Patient Record
    #   use @reactive.event(input.input_name) in order to react on the button press
    #   Create a method that will react to the change of text from the input field (if input.input_name() is called)
    #   In the method save the patient_id and file_info from the inputs to variables and send them into a method
    #   in the 'utils' module, that will update the patient data with the new patiennt.
    #   Since the dataframe with the data is defined here in the server (df_reactive), send it as a parameter as well.
    #   The update method should return a string about which method was used when inserting the patient
    #   (Generate new data if only the patient_id input is present or load the data from csv file, if file is present).
    #   Assign the result to the txt_status variable here in server using a method '.set()' on a reactive Value variable

    @reactive.Effect
    @reactive.event(input.update_data)
    def _():
        df_1 = utils.simulate_data_update(df_reactive.get())
        df_reactive.set(df_1)

    @reactive.Effect
    @reactive.event(input.view_type)
    def _():
        view_type = input.view_type()
        if view_type == data.views['graph']:
            conditional_ui.set(data.dynamic_ui_elements['graph_type'])
        elif view_type in [data.views['summary'], data.views['table']]:
            conditional_ui.set(data.dynamic_ui_elements['stats'])
        else:
            conditional_ui.set(None)  # Clear the dynamic UI

    # OUTPUTS

    @output
    @render.plot
    def data_visualization():
        if input.view_type() == data.views['graph']:
            patient_id = input.patient_id()
            measurement_type = input.measurement_type()
            value_range = input.value_range()
            patient_data_df = df_reactive.get().loc[:, (patient_id, measurement_type)]
            filtered_data = patient_data_df[(patient_data_df >= value_range[0]) & (patient_data_df <= value_range[1])]

            return utils.create_plot(patient_id, measurement_type, filtered_data, input.graph_type())

    @output
    @render.text
    def statistical_summary():
        if input.view_type() == data.views['summary']:
            patient_id = input.patient_id()
            stats = input.stats()
            return utils.generate_statistical_summary(patient_id, stats, df_reactive)

    @output
    @render.table
    def patient_data():
        if input.view_type() == data.views['table']:
            patient_id = input.patient_id()
            measurement_type = input.stats()
            patient_data_df = df_reactive.get().loc[:, (patient_id, measurement_type)]
            return pd.DataFrame(patient_data_df).reset_index()

    @output
    @render.ui
    def dynamic_content():
        return conditional_ui.get()

    @output
    @render.text
    def txt_status_code():
        return txt_status.get()


app = App(shiny_ui.app_ui, server)
