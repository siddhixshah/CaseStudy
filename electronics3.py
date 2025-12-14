"""
-----------------------------------------------------------------------------
XYZ MOBILES: STRATEGIC TURNAROUND DASHBOARD (FINAL HYBRID VERSION)
-----------------------------------------------------------------------------

HOW TO RUN LOCALLY:
1. pip install streamlit pandas plotly
2. streamlit run app.py

HOW TO DEPLOY TO GITHUB/STREAMLIT CLOUD:
1. Create 'requirements.txt' with:
   streamlit
   pandas
   plotly
2. Push both files to GitHub.
-----------------------------------------------------------------------------
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="XYZ Strategic Turnaround",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR "REPORT" LOOK ---
st.markdown("""
    <style>
    /* Global Font & Spacing */
    .main { background-color: #ffffff; color: #333333; font-family: 'Arial', sans-serif; }
    h1 { color: #003366; font-size: 2.2rem; font-weight: 800; margin-bottom: 0px; }
    h3 { color: #003366; font-size: 1.2rem; font-weight: 700; margin-top: 20px; border-bottom: 2px solid #ddd; padding-bottom: 5px; }
    p, li { font-size: 0.95rem; line-height: 1.5; color: #444; }
    
    /* Custom Boxes */
    .insight-box {
        background-color: #eef4fa; border-left: 5px solid #003366;
        padding: 15px; border-radius: 4px; margin-bottom: 10px;
    }
    .problem-box {
        background-color: #fff0f0; border-left: 5px solid #cc0000;
        padding: 15px; border-radius: 4px; margin-bottom: 10px;
    }
    .strategy-card {
        background-color: #f8f9fa; border: 1px solid #ddd;
        padding: 15px; border-radius: 5px; height: 100%;
    }
    .kicker-box {
        background-color: #003366; color: white; padding: 15px;
        text-align: center; font-weight: bold; font-size: 1.1rem;
        border-radius: 5px; margin-top: 30px; margin-bottom: 20px;
    }
    .metric-value { font-size: 1.8rem; font-weight: 800; color: #003366; margin: 0; }
    .metric-label { font-size: 0.85rem; color: #666; margin: 0; }
    
    /* Table Styling to match Report Look */
    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
    th { background-color: #003366; color: white; text-align: left; padding: 8px; font-size: 0.9rem; }
    td { border-bottom: 1px solid #ddd; padding: 8px; font-size: 0.9rem; color: #333; }
    tr:nth-child(even) { background-color: #f2f2f2; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("XYZ MOBILES: FY25-26 STRATEGIC TURNAROUND")
st.markdown("**OBJECTIVE:** Stabilize Cash Flow (Q1) -> Pivot Manufacturing (Q2) -> Rebrand as Green Tech (Q3)")

st.markdown("---")

# --- ROW 1: THE REALITY CHECK ---
c1, c2 = st.columns([1, 2])

with c1:
    st.markdown("### 🛑 THE INERTIA TRAP (Problem Statement)")
    st.markdown("""
    <div class="problem-box">
    <b>Cash Trap:</b> ₹25 Cr locked in depreciating inventory.<br>
    <b>Asset Idle:</b> Factory running at 30% capacity.<br>
    <b>Brand:</b> Losing the "Feature War" to Xiaomi/Samsung.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("### 💡 THE VALUE SHIFT (Primary Insight)")
    st.markdown("""
    <div class="insight-box">
    <b>Stop fighting the "Specs War". Start fighting the "Ecosystem War".</b><br>
    We cannot win on <i>Selling Phones</i> right now. We win by:<br>
    1. Monetizing our <b>Factory</b> (B2B Manufacturing for others).<br>
    2. Positioning our <b>Brand</b> where they aren't: <b>Sustainability (Green Tech).</b>
    </div>
    """, unsafe_allow_html=True)

# --- ROW 2: THE 3-POINT BATTLE PLAN ---
st.markdown("### ⚔️ 3-POINT ACTION PLAN (EXECUTION)")

c_p1, c_p2, c_p3 = st.columns(3)

with c_p1:
    st.markdown("""
    <div class="strategy-card">
    <b>1. LIQUIDITY (The Cash Engine)</b><br>
    <i>Goal: Unlock ₹12 Cr by March</i>
    <hr style="margin:5px 0;">
    <ul>
    <li><b>Corporate Bulk Exit:</b> Sell 15k units to Logistics/Pharma (e.g., Delhivery, Sun Pharma) for field staff. <b>Price: At Cost.</b></li>
    <li><b>Spare Parts Harvest:</b> Dismantle 'Dead Stock'. Reuse screens/batteries for Service Centers (Save 15% procurement cost).</li>
    <li><b>Coupon Lock-in:</b> Don't discount; give existing users a <b>₹5k Deferred Coupon</b> for future "Green" products.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c_p2:
    st.markdown("""
    <div class="strategy-card">
    <b>2. ASSETS (The Manufacturing Pivot)</b><br>
    <i>Goal: 85% Utilization by Q3</i>
    <hr style="margin:5px 0;">
    <ul>
    <li><b>JV Strategy:</b> "Complement, Don't Compete." Partner with <b>Sunwoda</b> (Wireless Charging) or <b>Lianchuang</b> (Optics).</li>
    <li><b>Nvidia/AI Angle:</b> Pivot Line 2 to <b>OSAT</b> (Assembly & Test) for Edge AI modules. Higher margin, low competition.</li>
    <li><b>China+1 Play:</b> Offer our facility as the "Indian Assembly Hub" to component makers avoiding tariffs.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c_p3:
    st.markdown("""
    <div class="strategy-card">
    <b>3. BRAND (The Green Differentiator)</b><br>
    <i>Goal: New Revenue Stream via Carbon</i>
    <hr style="margin:5px 0;">
    <ul>
    <li><b>EU CBAM Readiness:</b> Prepare for European 'Carbon Border Tax'. Become the <i>only</i> India-ready exporter.</li>
    <li><b>CCTS Revenue:</b> Earn & Trade credits on the <b>Indian Carbon Market</b> by solar-roofing the plant.</li>
    <li><b>The "Carbon-Neutral" Phone:</b> Marketing USP for Gen Z. "This phone planted 10 trees."</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- NEW SECTION: PARTNERSHIP TABLE (INSERTED AS REQUESTED) ---
st.markdown("### 🤝 STRATEGIC PARTNERSHIP LANDSCAPE (TARGETS)")
st.markdown("""
<table>
  <tr>
    <th style="width:20%">TARGET PARTNER</th>
    <th style="width:35%">THEIR PAIN POINT (WHY THEM?)</th>
    <th style="width:35%">OUR PITCH (THE VALUE PROP)</th>
    <th style="width:10%">IMPACT</th>
  </tr>
  <tr>
    <td><b>SUNWODA</b><br>(Batteries/Power)</td>
    <td>Needs immediate capacity for EV/Power Walls in India; building new plants takes 18 months.</td>
    <td>"We give you Line 3 for <b>Wireless Charging Coil</b> assembly immediately. Zero Capex for you."</td>
    <td><b>40%</b> Util.</td>
  </tr>
  <tr>
    <td><b>LIANCHUANG</b><br>(Optics/Lenses)</td>
    <td>Investing $50M in India (Apr '25 news) but needs quick "Optical Module" assembly to supply Vivo/Oppo.</td>
    <td>"We become your <b>Precision Assembly Hub</b>. We handle the labor; you bring the tech."</td>
    <td><b>12%</b> Margin</td>
  </tr>
  <tr>
    <td><b>NVIDIA PARTNERS</b><br>(Edge AI Hardware)</td>
    <td>High demand for "Jetson" AI modules in robotics; few Indian assemblers have clean rooms.</td>
    <td>"Pivot Line 1 to <b>OSAT (Assembly & Test)</b> for high-margin AI hardware."</td>
    <td><b>Future Proof</b></td>
  </tr>
</table>
""", unsafe_allow_html=True)

st.write("") # Spacer

# --- ROW 3: FINANCIALS & ROADMAP ---
c_fin, c_road = st.columns([1, 1])

with c_fin:
    st.markdown("### 💰 FINANCIAL RECOVERY (WATERFALL)")
    # Data for Waterfall
    fig_waterfall = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "relative", "relative", "total"],
        x = ["Deficit", "Bulk Sale", "Scrap Harvest", "Coupon Rev", "JV Rent", "OpEx Savings", "Net Cash"],
        text = ["-25", "+12", "+3.5", "+4.0", "+8.0", "+2.5", "5.0"],
        y = [-25, 12, 3.5, 4.0, 8.0, 2.5, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
        decreasing = {"marker":{"color":"#cc0000"}},
        increasing = {"marker":{"color":"#009933"}},
        totals = {"marker":{"color":"#003366"}}
    ))
    fig_waterfall.update_layout(title="
