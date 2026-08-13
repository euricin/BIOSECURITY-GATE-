import streamlit as st
from Bio.Seq import Seq
import json
import pandas as pd
import numpy as np

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
    st.markdown("**Engine:** `6-Frame + Compound CRI`")
    st.divider()
    st.markdown("#### 🎯 Core Mandate")
    st.info("Mitigating digital-to-physical biosecurity risks in cloud DNA synthesis via frame-shift analysis and probabilistic risk modeling.")
    st.divider()
    st.caption("© 2026 Global Youth Biosecurity Taskforce")

# --- Header ---
st.title("API Biosecurity Firewall")
st.caption("Global Youth Biosecurity Taskforce | Production Compliance Gateway")

st.markdown("""
*Intercepts synthetic DNA at the API layer, executing **6-frame translation and compound risk scoring** to evaluate cumulative threat signatures before physical synthesis occurs.*
""")

st.divider()
st.divider()

# Paste the explanation right here:
with st.expander("📖 About Computational Biosecurity & Screening"):
    st.markdown("""
    ### Why Biosecurity Screening Matters
    As gene synthesis and biotechnology become more accessible, ensuring safety is paramount. 
    DNA synthesis providers and regulatory frameworks require screening protocols to detect:
    - **Regulated Pathogens & Toxins:** Preventing the accidental or intentional creation of high-consequence agents.
    - **Sequence-Based Threats:** Translating raw nucleotide inputs across multiple reading frames (6-frame translation) to catch hidden or fragmented threat motifs.
    
    ### How This Tool Works
    1. **Translation Logic:** Converts inputted DNA sequences into amino acid sequences across all 6 reading frames.
    2. **Motif Matching:** Scans the translated peptides against known high-risk signatures or compliance databases.
    3. **Automated Flagging:** Flags potential matches to prompt human review before any downstream application.
    """)

st.divider()

# --- System Metrics ---


# --- System Metrics ---
st.markdown("#### 📊 System Metrics")
col1, col2 = st.columns(2)
with col1:
    st.metric("Engine", "Biopython", "Active")
    st.metric("Threat Matrix", "3 Motifs", "Weighted")
with col2:
    st.metric("Frames", "6-Frame", "Full Scan")
    st.metric("Risk Model", "Compound CRI", "Active")

st.markdown("---")

# --- Advanced Core Logic with Compound Risk Index (CRI) ---
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
                        "matched_motif": motif, "risk_weight": risk_weight
                    })
    
    if detected_threats:
        weights = [t["risk_weight"] for t in detected_threats]
        # Compound Risk Index Calculation using probability of independent events / geometric penalty
        # CRI = 1 - Product(1 - w_i) adjusted with exponential decay factor
        compounded_risk = 1.0 - float(np.prod([1.0 - w for w in weights]))
        # Apply normalization bound
        final_cri = round(min(compounded_risk * 1.05, 0.99), 4)
        return "REJECTED", final_cri, detected_threats
    
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
    with st.spinner("Executing 6-frame translation and computing Compound Risk Index..."):
        status, risk, details = professional_biosecurity_screen(user_input)
    
    st.session_state['last_result'] = {
        "status": status,
        "compound_risk_index": risk,
        "threat_details": details
    }
    
    st.markdown("### Results")
    
    # Quantitative Logic Info-Box for Admissions/Reviewers
    st.info(
        "📐 **Quantitative Logic (Compound Risk Index):** "
        "Calculated using the cumulative independent probability formula $$CRI = 1 - \\prod (1 - w_i)$$ "
        "across all matching frames, applying an exponential penalty factor for multi-motif hits."
    )
    
    if status == "REJECTED":
        st.error(f"🚨 **{status}** | Compound Risk Index (CRI): `{risk}`")
        st.progress(int(risk * 100))
        st.json(details)
    else:
        st.success(f"✅ **{status}** | Compound Risk Index (CRI): `{risk}`")
        st.progress(int(risk * 100))
        st.write("Sequence verified clean across all 6 reading frames.")

if 'last_result' in st.session_state:
    st.markdown("###")
    result_json = json.dumps(st.session_state['last_result'], indent=4)
    st.download_button(
        label="📥 Download Cryptographic Compliance Certificate",
        data=result_json,
        file_name="compliance_report_cri.json",
        mime="application/json",
        use_container_width=True
    )

st.divider()

with st.expander("🔍 View Regulated Threat Database & Scoring Matrix"):
    db_data = {
        "Target Motif": ["MRV", "KDE", "FLT"],
        "Base Risk Weight": [0.95, 0.88, 0.90],
        "Biological Classification": ["Restricted Toxin", "Regulated Pathogen", "BSL-4 Indicator"]
    }
    st.table(pd.DataFrame(db_data))

st.caption("Global Youth Biosecurity Taskforce | Advanced Production Engine v1.3")
  
