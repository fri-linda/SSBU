from shiny import ui

import data_init as data

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.panel_title("Biomedical Data Visualization and Analysis"),
            ui.input_text("new_patient_id", "Enter New Patient ID:"),
            ui.input_file("file1", "Choose CSV File", accept=".csv"),
            ui.input_action_button("add_patient", "Add Patient"),
            ui.output_text("txt_status_code"),
            ui.input_text("patient_id", "Select Patient", placeholder="Patient ID", value="Patient 1"),
            ui.input_select("measurement_type", "Select Measurement Type", choices=data.measurements),
            ui.input_slider("value_range", "Value Range", min=100, max=250, value=[100, 250]),
            ui.input_action_button("update_data", "Update Data"),
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