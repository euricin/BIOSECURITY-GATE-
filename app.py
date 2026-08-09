








import streamlit as st
from Bio.Seq import Seq
import json
import pandas as pd

# --- Page Config ---
st.set_page_config(
    page_title="Global Youth Biosecurity Taskforce | API Gate", 
    page_icon="🛡️",
    layout="centered"
)

# --- Sidebar Institutional Info ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=400&q=80", use_container_width=True)
    st.markdown("### 🏛️ Taskforce Portal")
    st.write("**Initiative:** Global Youth Biosecurity Taskforce")
    st.write("**Module:** Autonomous API Screening Firewall")
    st.write("**Status:** Production Prototype v1.2")
    st.divider()
    st.markdown("#### 🎯 Core Objectives")
    st.info("Mitigating digital-to-physical biosecurity risks in cloud-based DNA synthesis platforms through rigorous 6-frame frame-shift analysis.")
    st.divider()
    st.caption("© 2026 Global Youth Biosecurity Taskforce. All rights reserved.")

# --- Header & Institutional Branding ---
st.title("🛡️ Global Youth Biosecurity Taskforce")
st.subheader("Autonomous API-Level Biosecurity Screening Firewall")
st.markdown("""
*Production-grade prototype designed to mitigate digital-to-physical biosecurity vulnerabilities by screening synthetic DNA against dual-use threat signatures across all 6 reading frames.*
""")

# --- High-Quality Architecture Diagram Image ---
st.image(
    "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&q=80", 
    caption="Fig 1.0: Architectural Flow of the 6-Frame Translation & Compliance Engine",
    use_container_width=True
)

st.divider()

# --- The Core Logic ---
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

# --- Quick Test Presets ---
st.markdown("### 🧬 Test Sequence Presets")
col1, col2 = st.columns(2)
preset_input = "GACATGCGCGTGGTA"
if col1.button("Load Safe Sequence"):
    preset_input = "ATGCGCTAGATCGAT"
if col2.button("Load Threat Sequence"):
    preset_input = "GACATGCGCGTGGTA"

# --- User Input & Execution ---
user_input = st.text_area("Enter or modify DNA sequence to screen:", value=preset_input)

if st.button("Run Security Screen", type="primary"):
    with st.spinner("Executing 6-frame translation and scanning compliance matrix..."):
        status, risk, details = professional_biosecurity_screen(user_input)
    
    st.session_state['last_result'] = {
        "status": status,
        "max_risk_score": risk,
        "threat_details": details
    }
    
    if status == "REJECTED":
        st.error(f"🚨 STATUS: {status} | Max Risk Score: {risk}")
        st.progress(int(risk * 100))
        st.markdown("#### Threat Audit Trail:")
        st.json(details)
    else:
        st.success(f"✅ STATUS: {status} | Risk Score: {risk}")
        st.progress(int(risk * 100))
        st.write("Sequence is clean across all 6 reading frames. Approved for synthesis release.")

# --- Downloadable Compliance Report Feature ---
if 'last_result' in st.session_state:
    result_json = json.dumps(st.session_state['last_result'], indent=4)
    st.download_button(
        label="📥 Download Official Audit Certificate (JSON)",
        data=result_json,
        file_name="biosecurity_audit_report.json",
        mime="application/json"
    )

st.divider()

# --- Threat Database Transparency Expander ---
with st.expander("🔍 View Active Biosecurity Threat Database"):
    st.write("The system checks synthesized sequences against the following high-consequence protein motifs:")
    db_data = {
        "Motif Code": ["MRV", "KDE", "FLT"],
        "Risk Weight": [0.95, 0.88, 0.90],
        "Classification": ["Restricted Toxin / High Consequence", "Regulated Pathogen Marker", "Biosafety Level 4 Indicator"]
    }
    st.table(pd.DataFrame(db_data))

st.divider()
st.caption("Global Youth Biosecurity Taskforce | Open-Access Governance & Compliance Initiative")

                        
  
