from nicegui import app, ui
import datetime
import pytz

time_zones = pytz.all_timezones

def on_button_click():
    date_value = None
    time_value = None

    if not selected_date.value or not selected_time.value:
        original_time_zone_label.text = "Please select a date and time"

    try:
        if isinstance(selected_date.value, str):
            date_value = datetime.date.fromisoformat(selected_date.value)

        if isinstance(selected_time.value, str):
            time_value = datetime.time.fromisoformat(selected_time.value)

        dt = datetime.datetime.combine(date_value, time_value)

        input_tz = pytz.timezone(from_zone.value)
        localize_dt = input_tz.localize(dt)

        output_tz = pytz.timezone(to_zone.value)
        converted_dt = dt.astimezone(output_tz)

        original_time_zone_label.text = f"🕓 {from_zone.value}: {localize_dt}"
        converted_time_zone_label.text = f"🌎 {to_zone.value}: {converted_dt}"
    except Exception as e:
        original_time_zone_label.text = f"Something wrong here {e}"


with ui.header().classes('bg-blue-500 text-white'):
    ui.label('Date Time Converter').classes('text-xl font-bold')

with ui.column().classes('items-center w-auto mx-auto gap-10 mt-20'):
    ui.label("⏱️ Date Time Converter").tailwind('font-bold', 'text-4xl')

    with ui.row().classes('justify-center items-center gap-4'):
        selected_date = ui.date()
        selected_time = ui.time()

    with ui.row().classes('gap-4'):
        with ui.column().classes('gap-0'):
            ui.label("From Time Zone").tailwind('font-bold')
            from_zone = ui.select(time_zones, value="Europe/Berlin")

        with ui.column().classes('gap-0'):
            ui.label("To Time Zone").tailwind('font-bold')
            to_zone = ui.select(time_zones, value="Asia/Colombo")

    original_time_zone_label = ui.label("")
    converted_time_zone_label = ui.label("")

    ui.button("Convert Time", on_click=on_button_click)

    def handle_state():
        now = datetime.datetime.now()
        selected_date.value = now.date().isoformat()
        selected_time.value = now.time().strftime('%H:%M:%S')

    app.on_connect(handle_state)


ui.run()