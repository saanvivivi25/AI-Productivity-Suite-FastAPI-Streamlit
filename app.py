import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# -------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="AI Productivity Suite",
    page_icon="🤖",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# -------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------

def get_dashboard():

    response = requests.get(
        f"{API_URL}/dashboard/stats"
    )

    return response.json()


def get_history():

    response = requests.get(
        f"{API_URL}/history"
    )

    return response.json()


# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

st.sidebar.title("🤖 AI Productivity Suite")

if st.sidebar.button("🏠 Dashboard"):
    st.session_state.page = "Dashboard"

if st.sidebar.button("📄 Resume Screening"):
    st.session_state.page = "Resume Screening"

if st.sidebar.button("📝 Meeting Notes"):
    st.session_state.page = "Meeting Notes"

if st.sidebar.button("💬 Feedback Analyzer"):
    st.session_state.page = "Feedback Analyzer"

if st.sidebar.button("📧 Email Generator"):
    st.session_state.page = "Email Generator"

if st.sidebar.button("📚 Text Summarizer"):
    st.session_state.page = "Text Summarizer"

if st.sidebar.button("📜 History"):
    st.session_state.page = "History"

choice = st.session_state.page

# ==========================================================
# DASHBOARD
# ==========================================================

if choice == "Dashboard":

    st.title("🤖 AI Productivity Suite Dashboard")

    data = get_dashboard()

    total = data["total_records"]

    stats = data["stats_by_module"]

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📄 Resume Screening",
            stats.get("Resume Screening",0)
        )

        st.metric(
            "💬 Feedback Analyzer",
            stats.get("Feedback Analyzer",0)
        )

        st.metric(
            "📚 Text Summarizer",
            stats.get("Text Summarizer",0)
        )

    with col2:

        st.metric(
            "📝 Meeting Notes",
            stats.get("Meeting Notes",0)
        )

        st.metric(
            "📧 Email Generator",
            stats.get("Email Generator",0)
        )

    st.markdown("---")

    st.metric(
        "📊 Total Records",
        total
    )

# ==========================================================
# RESUME SCREENING
# ==========================================================

elif choice == "Resume Screening":

    st.title("📄 Resume Screening")

    option = st.radio(

        "Choose Input Method",

        [

            "Manual",

            "Excel Upload"

        ]

    )

    # -------------------------------------------
    # MANUAL
    # -------------------------------------------

    if option == "Manual":

        resume = st.text_area(

            "Paste Resume",

            height=300

        )

        if st.button("Analyze Resume"):

            if resume.strip() == "":

                st.warning("Please enter a resume.")

            else:

                with st.spinner("Analyzing Resume..."):

                    response = requests.post(

                        f"{API_URL}/resume/analyze",

                        json={

                            "resume": resume

                        }

                    )

                    if response.status_code == 200:

                        result = response.json()["result"]

                        st.success("Analysis Completed")

                        st.write(result)

                    else:

                        st.error(response.text)

    # -------------------------------------------
    # EXCEL UPLOAD
    # -------------------------------------------

    else:

        uploaded_file = st.file_uploader(

            "Upload Resume Excel",

            type=["xlsx"]

        )

        if uploaded_file is not None:

            df = pd.read_excel(uploaded_file)

            st.dataframe(df)

            if st.button("Analyze All Resumes"):

                files = {

                    "file": (

                        uploaded_file.name,

                        uploaded_file,

                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                    )

                }

                with st.spinner("Processing..."):

                    response = requests.post(

                        f"{API_URL}/resume/analyze-bulk",

                        files=files

                    )

                if response.status_code == 200:

                    st.success("Completed")

                    st.download_button(

                        "📥 Download Analysis",

                        data=response.content,

                        file_name="Resume_Analysis.xlsx",

                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                    )

                else:

                    st.error(response.text)
# ==========================================================
# MEETING NOTES
# ==========================================================

elif choice == "Meeting Notes":

    st.title("📝 AI Meeting Notes Generator")

    transcript = st.text_area(
        "Meeting Transcript",
        height=300
    )

    if st.button("Generate Notes"):

        if transcript.strip() == "":

            st.warning("Please enter a meeting transcript.")

        else:

            with st.spinner("Generating Notes..."):

                response = requests.post(

                    f"{API_URL}/meeting-notes/generate",

                    json={
                        "transcript": transcript
                    }

                )

            if response.status_code == 200:

                result = response.json()["result"]

                st.success("Meeting Notes Generated")

                st.write(result)

            else:

                st.error(response.text)

# ==========================================================
# FEEDBACK ANALYZER
# ==========================================================

elif choice == "Feedback Analyzer":

    st.title("💬 AI Feedback Analyzer")

    option = st.radio(

        "Choose Input Method",

        [

            "Manual",

            "Excel Upload"

        ]

    )

    # -------------------------------------------------
    # MANUAL INPUT
    # -------------------------------------------------

    if option == "Manual":

        feedback = st.text_area(

            "Customer Feedback",

            height=250

        )

        if st.button("Analyze Feedback"):

            if feedback.strip() == "":

                st.warning("Please enter feedback.")

            else:

                with st.spinner("Analyzing Feedback..."):

                    response = requests.post(

                        f"{API_URL}/feedback/analyze",

                        json={

                            "feedback": feedback

                        }

                    )

                if response.status_code == 200:

                    result = response.json()["result"]

                    st.success("Analysis Completed")

                    st.write(result)

                else:

                    st.error(response.text)

    # -------------------------------------------------
    # EXCEL UPLOAD
    # -------------------------------------------------

    else:

        uploaded_file = st.file_uploader(

            "Upload Feedback Excel",

            type=["xlsx"]

        )

        if uploaded_file is not None:

            df = pd.read_excel(uploaded_file)

            st.dataframe(
                df,
                use_container_width=True
            )

            if st.button("Analyze Feedback File"):

                files = {

                    "file": (

                        uploaded_file.name,

                        uploaded_file,

                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                    )

                }

                with st.spinner("Analyzing Feedback..."):

                    response = requests.post(

                        f"{API_URL}/feedback/analyze-bulk",

                        files=files

                    )

                if response.status_code == 200:

                    st.success("Completed")

                    st.download_button(

                        "📥 Download Results",

                        data=response.content,

                        file_name="Feedback_Analysis.xlsx",

                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                    )

                else:

                    st.error(response.text)

# ==========================================================
# EMAIL GENERATOR
# ==========================================================

elif choice == "Email Generator":

    st.title("📧 AI Email Generator")

    subject = st.text_input(
        "Email Subject"
    )

    purpose = st.text_area(
        "Purpose / Instructions",
        height=250
    )

    if st.button("Generate Email"):

        if subject.strip() == "" or purpose.strip() == "":

            st.warning("Please enter both Subject and Purpose.")

        else:

            with st.spinner("Generating Email..."):

                response = requests.post(

                    f"{API_URL}/email/generate",

                    json={

                        "subject": subject,

                        "purpose": purpose

                    }

                )

            if response.status_code == 200:

                result = response.json()["result"]

                st.success("Email Generated Successfully")

                st.write(result)

            else:

                st.error(response.text)


# ==========================================================
# TEXT SUMMARIZER
# ==========================================================

elif choice == "Text Summarizer":

    st.title("📚 AI Text Summarizer")

    text = st.text_area(

        "Enter Text",

        height=300

    )

    if st.button("Summarize"):

        if text.strip() == "":

            st.warning("Please enter some text.")

        else:

            with st.spinner("Generating Summary..."):

                response = requests.post(

                    f"{API_URL}/summarizer/summarize",

                    json={

                        "text": text

                    }

                )

            if response.status_code == 200:

                result = response.json()["result"]

                st.success("Summary Generated Successfully")

                st.write(result)

            else:

                st.error(response.text)

# ==========================================================
# HISTORY
# ==========================================================

elif choice == "History":

    st.title("📜 AI History")

    # -----------------------------
    # SEARCH
    # -----------------------------

    search = st.text_input(
        "🔍 Search History"
    )

    if search.strip() != "":

        response = requests.get(

            f"{API_URL}/history",

            params={
                "search": search
            }

        )

    else:

        response = requests.get(

            f"{API_URL}/history"

        )

    if response.status_code != 200:

        st.error(response.text)

    else:

        data = response.json()

        records = data["records"]

        if len(records) == 0:

            st.info("No records found.")

        else:

            df = pd.DataFrame(records)

            st.dataframe(

                df,

                use_container_width=True,

                height=500

            )

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            # --------------------------------
            # EXPORT
            # --------------------------------

            with col1:

                if st.button("📥 Export History"):

                    if search.strip() == "":

                        export = requests.get(
                            f"{API_URL}/history/export"
                        )

                    else:

                        export = requests.get(
                            f"{API_URL}/history/export",
                            params={
                                "search": search
                            }
                        )

                    if export.status_code == 200:

                        st.download_button(
                            label="📥 Download Report",
                            data=export.content,
                            file_name="AI_Productivity_Report.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )

                    else:

                        st.error("Failed to export history.")

            # --------------------------------
            # DELETE RECORD
            # --------------------------------

            with col2:

                delete_id = st.number_input(

                    "Record ID",

                    min_value=1,

                    step=1

                )

                if st.button("Delete Record"):

                    response = requests.delete(

                        f"{API_URL}/history/{delete_id}"

                    )

                    if response.status_code == 200:

                        st.success("Record Deleted")

                        st.rerun()

                    else:

                        st.error(response.text)

            # --------------------------------
            # DELETE ALL
            # --------------------------------

            with col3:

                if st.button("Delete All"):

                    response = requests.delete(

                        f"{API_URL}/history"

                    )

                    if response.status_code == 200:

                        st.success("All Records Deleted")

                        st.rerun()

                    else:

                        st.error(response.text)