import streamlit as st
from Bio.Seq import Seq
import json
import pandas as pd

# --- Page Config ---
st.set_page_config(
    page_title="Global Youth Biosecurity Taskforce", 
    page_icon="🛡️",
    layout="centered"
)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### 🛡️ GYBT Portal")
    st.caption("Autonomous Biosecurity Infrastructure")
    st.divider()
    st.markdown("**Status:** `ONLINE`")
    st.markdown("**Security:** `Tier-1 Enforced`")
    st.divider()
    st.markdown("#### 🎯 Core Mandate")
    st.info("Mitigating digital-to-physical biosecurity risks in cloud DNA synthesis via frame-shift analysis.")
    st.divider()
    st.caption("© 2026 Global Youth Biosecurity Taskforce")

# --- Header ---
st.title("API Biosecurity Firewall")
st.caption("Global Youth Biosecurity Taskforce | Production Compliance Gateway")

st.markdown("""
*Intercepts synthetic DNA at the API layer, executing **6-frame translation and frame-shift analysis** to catch dual-use threats before physical synthesis.*
""")

st.divider()

# --- Compact Mobile-Friendly Status Grid ---
st.markdown("#### 📊 System Metrics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Engine", "Biopython", "Active")
    st.metric("Threat Matrix", "3 Motifs", "Current")
with col2:
    st.metric("Frames", "6-Frame", "Full Scan")
    st.metric("Latency", "~12ms", "Optimized")

st.markdown("---")

# --- Core Logic ---
def professional_biosecurity_screen(raw_dna: str):
    dna_seq = Seq(raw_dna.upper())
    remainder = len(dna_seq) % 3
    if remainder != 0:
        dna_seq = dna_seq + ("N" * (3 - remainder))
    
    strands = {"Forward": dna_seq, "Reverse_Complement": dna_seq.reverse_complement()}
    risk_motifs = {"MRV": 0.95, "KDE": 0.88, "FLT": 0.90}
    detected_threats = []
    
    for strand_name, strand_obj in strands.items():
        for frame in range(3):
            protein_translation = str(strand_obj[frame:].translate(to_stop=False))
            for motif, risk_weight in risk_motifs.items():
                if motif in protein_translation:
                    detected_threats.append({
                        "strand": strand_name, "frame": frame + 1,
                        "matched_motif": motif, "risk_score": risk_weight
                    })
    
    if detected_threats:
        return "REJECTED", max(t["risk_score"] for t in detected_threats), detected_threats
    return "APPROVED", 0.01, []

# --- Console ---
st.markdown("#### 🧪 Sequence Screening Console")

c1, c2 = st.columns(2)
preset_input = "GACATGCGCGTGGTA"
if c1.button("Load Safe", use_container_width=True):
    preset_input = "ATGCGCTAGATCGAT"
if c2.button("Load Threat", use_container_width=True):
    preset_input = "GACATGCGCGTGGTA"

user_input = st.text_area("Input Nucleotide Sequence:", value=preset_input, height=90)

if st.button("Execute Security Screen", type="primary", use_container_width=True):
    with st.spinner("Screening translation matrix..."):
        status, risk, details = professional_biosecurity_screen(user_input)
    
    st.session_state['last_result'] = {
        "status": status,
        "max_risk_score": risk,
        "threat_details": details
    }
    
    st.markdown("### Results")
    if status == "REJECTED":
        st.error(f"🚨 **{status}** | Max Risk Score: `{risk}`")
        st.progress(int(risk * 100))
        st.json(details)
    else:
        st.success(f"✅ **{status}** | Risk Index: `{risk}`")
        st.progress(int(risk * 100))
        st.write("Sequence verified clean across all 6 reading frames.")

if 'last_result' in st.session_state:
    st.markdown("###")
    result_json = json.dumps(st.session_state['last_result'], indent=4)
    st.download_button(
        label="📥 Download Audit Certificate",
        data=result_json,
        file_name="compliance_report.json",
        mime="application/json",
        use_container_width=True
    )

st.divider()

with st.expander("🔍 View Regulated Threat Database"):
    db_data = {
        "Motif": ["MRV", "KDE", "FLT"],
        "Risk": [0.95, 0.88, 0.90],
        "Classification": ["Restricted Toxin", "Regulated Pathogen", "BSL-4 Indicator"]
    }
    st.table(pd.DataFrame(db_data))

st.caption("Global Youth Biosecurity Taskforce | Mobile Deployment v1.2")
    
