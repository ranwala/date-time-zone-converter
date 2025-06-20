import streamlit as st
from datetime import datetime
import pytz

all_time_zones = pytz.all_timezones

st.title("⏱️ TimeZone Converter")

date = st.date_input("Select a date")
print(date)
time = st.time_input("Select a time")
print(time)
from_option = st.selectbox("From time zone", all_time_zones)

to_option = st.selectbox("To time zone", all_time_zones)

convert_button = st.button("Convert Time")

if convert_button:
    dt = datetime.combine(date, time)

    input_tz = pytz.timezone(from_option)
    localize_dt = input_tz.localize(dt)

    output_tz = pytz.timezone(to_option)
    converted_dt = dt.astimezone(output_tz)

    st.success(f"🕓 Original ({from_option}): {localize_dt}")
    st.success(f"🌎 Converted ({to_option}): {converted_dt}")

