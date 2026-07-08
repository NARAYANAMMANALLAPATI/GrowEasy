import streamlit as st
import pandas as pd
import random

st.set_page_config(
    page_title="GrowEasy CSV Importer",
    layout="wide"
)

CRM_FIELDS = [

    "created_at",
    "name",
    "email",
    "country_code",
    "mobile_without_country_code",
    "company",
    "city",
    "state",
    "country",
    "lead_owner",
    "crm_status",
    "crm_note",
    "data_source",
    "possession_time",
    "description"
]

COLUMN_MAPPING = {

    "lead name": "name",
    "customer name": "name",
    "full name": "name",

    "email": "email",
    "email address": "email",
    "email id": "email",

    "mobile": "mobile_without_country_code",
    "phone": "mobile_without_country_code",
    "phone number": "mobile_without_country_code",

    "contact number":
        "mobile_without_country_code",

    "company": "company",
    "company name": "company",

    "city": "city",
    "city name": "city",

    "remarks": "crm_note",
    "comments": "crm_note",
    "notes": "crm_note",

    "country": "country",

    "state": "state"
}

STATUSES = [

    "GOOD_LEAD_FOLLOW_UP",
    "DID_NOT_CONNECT",
    "BAD_LEAD",
    "SALE_DONE"
]

st.title("📂 GrowEasy AI CSV Importer")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(
        uploaded_file
    )

    st.subheader(
        "CSV Preview"
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=350
    )

    if st.button(
        "Confirm Import"
    ):

        mapping = {}

        for col in df.columns:

            key = (
                col
                .lower()
                .strip()
            )

            if key in COLUMN_MAPPING:

                mapping[col] = (
                    COLUMN_MAPPING[key]
                )

        parsed_records = []
        skipped_records = []

        for _, row in df.iterrows():

            crm_record = {}

            for field in CRM_FIELDS:
                crm_record[field] = ""

            for src, target in (
                mapping.items()
            ):

                crm_record[target] = str(
                    row[src]
                )

            crm_record[
                "country_code"
            ] = "+91"

            crm_record[
                "crm_status"
            ] = random.choice(
                STATUSES
            )

            email = crm_record[
                "email"
            ]

            mobile = crm_record[
              "mobile_without_country_code"
            ]

            if (
                email == ""
                and
                mobile == ""
            ):
                skipped_records.append(
                    crm_record
                )
                continue

            parsed_records.append(
                crm_record
            )

        result_df = pd.DataFrame(
            parsed_records
        )

        st.success(
            "Import Completed"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Imported",
                len(parsed_records)
            )

        with col2:
            st.metric(
                "Skipped",
                len(skipped_records)
            )

        st.subheader(
            "CRM Records"
        )

        st.dataframe(
            result_df,
            use_container_width=True,
            height=500
        )

        csv = (
            result_df
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            "Download CRM CSV",
            csv,
            "groweasy_output.csv",
            "text/csv"
        )