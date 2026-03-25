import streamlit as st
import json
import tempfile
from process_juicebox import extract, make_xlsx

st.set_page_config(page_title="JSON to Excel", layout="centered")

st.title("JSON → Excel Converter")

uploaded_file = st.file_uploader("Upload your JSON file", type=["json"])

if uploaded_file:
    data = json.load(uploaded_file)
    rows = extract(data)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        make_xlsx(rows, tmp.name)
        tmp_path = tmp.name

    with open(tmp_path, "rb") as f:
        st.success("File ready ✅")
        st.download_button(
            label="Download Excel",
            data=f,
            file_name="output.xlsx"
        )