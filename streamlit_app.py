from openai import OpenAI
import streamlit as st
 
# 🔑 Add your API key
client = OpenAI(api_key="YOUR_API_KEY")
 
# 🧠 Your Resume Data (AI Brain)
resume_data = """
Jaimin Upadhyay is a Materials and Supply Chain professional with 7+ years of experience across manufacturing, food, healthcare, and regulated industries.
 
Currently Plant Materials Supervisor at Cargill, leading inventory, MRO, SAP ERP, and team operations.
 
Key achievements:
- Reduced obsolete inventory by 80%
- Recovered $150,000 through supplier discrepancy investigation
- Managed full MRO lifecycle
- Led SAP Fiori implementation support
- Supervised team of 7
 
Experience includes:
Cargill, Alberta Health Services, Sundial Growers
 
Skills:
SAP ERP, Inventory Control, MRO, Procurement, Power BI, Excel, Forecasting, Leadership
 
Education:
Diploma in Supply Management (SCMA)
B.Com in Accounting & Auditing
"""
 
# 🤖 Chat Function
def ask_bot(question):
    prompt = f"""
    You are an AI assistant representing Jaimin Upadhyay.
 
    Speak professionally, confidently, and concisely like a job candidate.
 
    Data:
    {resume_data}
 
    Question: {question}
    """
 
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
 
    return response.output[0].content[0].text
 
 
# 🎯 Resume Tailoring Function
def tailor_resume(job_desc):
    prompt = f"""
    Tailor a resume for this job:
 
    {job_desc}
 
    Candidate:
    {resume_data}
 
    Make it ATS optimized, achievement-focused, and relevant.
    """
 
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
 
    return response.output[0].content[0].text
 
 
# 🎨 UI Design
st.set_page_config(page_title="Jaimin AI Resume", layout="centered")
 
st.title("🤖 Jaimin's AI Resume Bot")
 
st.markdown("Interact with my experience, skills, and achievements in real-time.")
 
# 💬 Chat Section
st.header("💬 Ask Me Anything")
 
user_q = st.text_input("Ask about my experience, skills, achievements...")
 
if user_q:
    answer = ask_bot(user_q)
    st.success(answer)
 
# 🎯 Job Matching Section
st.header("🎯 Tailor My Resume to a Job")
 
job_desc = st.text_area("Paste Job Description")
 
if st.button("Generate Tailored Resume"):
    if job_desc:
        result = tailor_resume(job_desc)
        st.code(result)
    else:
        st.warning("Please paste a job description")
 
# ⭐ Quick Buttons
st.header("⚡ Quick Insights")
 
col1, col2, col3 = st.columns(3)
 
if col1.button("Top Achievements"):
    st.info(ask_bot("What are his top achievements?"))
 
if col2.button("Key Skills"):
    st.info(ask_bot("What are his key skills?"))
 
if col3.button("Why Hire Him?"):
    st.info(ask_bot("Why should we hire him?"))
 
# 👔 Footer Branding
st.markdown("---")
st.markdown("Built as an AI-powered interactive resume")
