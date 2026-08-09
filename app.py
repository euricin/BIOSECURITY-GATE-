import streamlit as st
from Bio.Seq import Seq
import json

# --- The Logic ---
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

# --- The Web UI ---
st.set_page_config(page_title="Biosecurity API Gate", page_icon="🛡️")
st.title("🛡️ Biosecurity Sequence Gate")
st.subheader("Global Youth Biosecurity Taskforce - Prototype")

user_input = st.text_area("Enter DNA sequence to screen:", "GACATGCGCGTGGTA")

if st.button("Run Security Screen"):
    status, risk, details = professional_biosecurity_screen(user_input)
    
    if status == "REJECTED":
        st.error(f"STATUS: {status} | Risk Score: {risk}")
        st.json(details)
    else:
        st.success(f"STATUS: {status} | Risk Score: {risk}")
        st.write("Sequence is clean across all 6 frames.")
  
