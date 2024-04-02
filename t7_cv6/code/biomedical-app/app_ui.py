from shiny import ui

import data_init as data

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.panel_title("Biomedical Data Visualization and Analysis"),
            # TODO 1: create ui.input_text to read a New Patient ID from user input

            # TODO 2: create ui.input_file to read Patient Data from file, let the file accept CSV only
            #  (attribute accept=".csv")

            # TODO 3: create ui.input_action_button Create a New Patient Record

            ui.output_text("txt_status_code"),
            ui.input_text("patient_id", "Select Patient", placeholder="Patient ID", value="Patient 1"),
            ui.input_select("measurement_type", "Select Measurement Type", choices=data.measurements),
            ui.input_slider("value_range", "Value Range", min=100, max=250, value=[100, 250]),
            # TODO 6: create ui.input_action_button with id "update_data" to update Patients' Data, that will generate
            #  new values for each patient and measurement
            ui.input_radio_buttons("view_type", "Choose View",
                                   choices=list(data.views.values()), selected="Visualization"),

            # Dynamic UI element
            ui.output_ui("dynamic_content"),
        ),
        ui.panel_main(
            ui.output_text("statistical_summary"),
            ui.output_table("patient_data"),
            ui.output_plot("data_visualization"),
        )
    )
)