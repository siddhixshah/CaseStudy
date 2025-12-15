"""
-----------------------------------------------------------------------------
XYZ MOBILES: STRATEGIC TURNAROUND DASHBOARD (FINAL REVISED VERSION)
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
    
    /* Table Styling */
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
    <b>Cash Trap:</b> INR 600 Cr locked in unsold inventory.<br>
    <b>Debt Load:</b> INR 1,200 Cr concern for solvency.<br>
    <b>Asset Idle:</b> Noida & Pune plants running at 30% capacity.<br>
    <b>Brand:</b> Losing the "Feature War" to Xiaomi/Samsung.
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("### 💡 THE VALUE SHIFT (Primary Insight)")
    st.markdown("""
    <div class="insight-box">
    <b>Stop fighting the "Specs War". Start fighting the "Ecosystem War".</b><br>
    We cannot win on <i>Selling Phones</i> right now. We win by:<br>
    1. <b>Pivot to Contract Manufacturing:</b> Lease idle Noida/Pune lines to 'China+1' players.<br>
    2. <b>Positioning Brand</b> where they aren't: <b>Sustainability (Green Tech).</b><br>
    3. <b>New PMF:</b> Capitalize on <b>#RightToDisconnect Bill</b> by competing on <i>Less Features</i>. Potential <b>₹250 Cr Blue Ocean</b> pan-India.<br>
    </div>
    """, unsafe_allow_html=True)

# --- ROW 2: THE 3-POINT BATTLE PLAN ---
st.markdown("### ⚔️ 3-POINT ACTION PLAN (EXECUTION)")

c_p1, c_p2, c_p3 = st.columns(3)

with c_p1:
    st.markdown("""
    <div class="strategy-card">
    <b>1. LIQUIDITY (The Cash Engine)</b><br>
    <i>Goal: Unlock INR 50 Cr (Emergency Fund)</i>
    <hr style="margin:5px 0;">
    <ul>
    <li><b>Corporate Bulk Exit:</b> Liquidate 6% of stock (~45k units) to B2B/Logistics/Pharma for field staff (e.g., Delhivery riders, Sun Pharma med reps). <b>Price: At Cost | Target : INR 35CR.</b></li>
    <li><b>Spare Parts Harvest:</b> Dismantle 'Dead Stock'. Reuse screens/batteries for Service Centers (Save <b>15%</b> procurement cost).</li>
    <li><b>Logistics Consolidation:</b> Merge vendor contracts to stop INR 45 Cr/yr leakage. <b>Save INR 5 Cr in Q1.</b></li>
    <li><b>Coupon Lock-in:</b> Sell old units at 10-15% discount + <b>INR 5k 'Deferred Value' Coupon</b>. <i>(Minimizes immediate loss; lowers CAC for future products).</i>
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
    <li><b>JV Strategy:</b> "Complement, Don't Compete." Partner with <b>Sunwoda</b> (Batteries) or <b>Lianchuang</b> (Optics).</li>
    <li><b>Nvidia/AI Angle:</b> Pivot Pune Facility to <b>White Label / Contract Manufacturing</b> for Edge AI (OSAT). High-margin, low competition assembly.</li>
    <li><b>China+1 Play:</b> Pitch our factory as the "Indian Assembly Hub" for component makers avoiding tariffs.</li>
    <li><b> Utilize legacy manufacturing units for high-End Feature Phones:</b> Requires zero retooling for 5G, maximizing ROCE. Low Specs (~Low Direct Cost) + <b>Cognitive Luxury</b> = High Premium.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c_p3:
    st.markdown("""
    <div class="strategy-card">
    <b>3. BRAND (The Differentiator)</b><br>
    <i>Goal: New Revenue Stream via Carbon Compliance & Feature Phones</i>
    <hr style="margin:5px 0;">
    <ul>
    <li><b>EU CBAM Readiness:</b> Prepare for European 'Carbon Border Tax'. Become the <i>only</i> India-ready exporter.</li>
    <li><b>CCTS Revenue:</b> Earn & Trade credits on the <b>Indian Carbon Market</b> by solar-roofing the Noida plant.</li>
    <li><b>The "Carbon-Neutral" Phone:</b> Marketing USP for Gen Z. Box Display: <i>"This phone planted 10 trees; generated 45kg CO2, offset to 0kg."</i></li>
    <li><b>The "Zen" Phone:</b> Curated OS for the burnt-out youth. Luxury in Focus and Attention. Increases friction for dopamine (No Social Media, Reading-specific Browsing modes), removes friction for utility (UPI/Maps, E-Ink/OLED, AI-Voice, Multi-day battery, tough build).<br>
    <i>Position "missing features" as premium exclusions.</i> Branding: <i>"Smart enough to navigate life. Dumb enough for peace."</i></li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- NEW SECTION: PARTNERSHIP TABLE ---
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
    <td>"We give you Pune Line 2 for <b>Battery & Wireless Charging Coil</b> assembly immediately. Zero Capex."</td>
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
    <td>"Pivot Noida Line 1 to <b>OSAT (Assembly & Test)</b> for high-margin AI hardware."</td>
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
        measure = ["relative", "relative", "relative", "relative", "relative", "total"],
        x = ["Vendor Gap", "Bulk Sale", "Scrap Harvest", "Logistics Fix", "JV Deposit", "Net Cash"],
        text = ["-50", "+35", "+5", "+5", "+10", "<b>+5.0</b>"],
        y = [-50, 35, 5, 5, 10, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
        decreasing = {"marker":{"color":"#cc0000"}},
        increasing = {"marker":{"color":"#009933"}},
        totals = {"marker":{"color":"#0f2b46"}}
    ))
    
    # Visual Tweaks for Visibility
    fig_waterfall.update_layout(
        title="Immediate Working Capital Bridge (INR Cr)", 
        height=300, 
        margin=dict(l=0, r=0, t=30, b=0),
        yaxis=dict(range=[-55, 15]) # Fixed range to ensure labels don't get cut off
    )
    fig_waterfall.update_traces(textposition='outside', textfont_size=11)
    
    st.plotly_chart(fig_waterfall, use_container_width=True)

with c_road:
    st.markdown("### 🗓️ 12-MONTH EXECUTION ROADMAP")
    # Data for Gantt
    df_gantt = pd.DataFrame([
        dict(Task="Phase 1: Liquidity (Bulk Sales)", Start='2025-01-01', Finish='2025-03-30', Phase='Urgent'),
        dict(Task="Vendor Payment Clearing", Start='2025-02-15', Finish='2025-04-01', Phase='Urgent'),
        dict(Task="JV Setup (Sunwoda/Lianchuang)", Start='2025-04-01', Finish='2025-08-30', Phase='Pivot'),
        dict(Task="ERP Clean-up (AI Integration)", Start='2025-03-01', Finish='2025-06-01', Phase='Pivot'),
        dict(Task="Launch 'Carbon Neutral' Phone", Start='2025-09-01', Finish='2025-12-31', Phase='Growth'),
        dict(Task="CCTS Carbon Credit Trading", Start='2025-10-01', Finish='2025-12-31', Phase='Growth')
    ])
    
    fig_gantt = px.timeline(
        df_gantt, 
        x_start="Start", 
        x_end="Finish", 
        y="Task", 
        color="Phase",
        color_discrete_map={"Urgent": "#cc0000", "Pivot": "#ff9900", "Growth": "#009933"}
    )
    fig_gantt.update_yaxes(autorange="reversed")
    fig_gantt.update_layout(height=300, margin=dict(l=0, r=0, t=30, b=0))
    st.plotly_chart(fig_gantt, use_container_width=True)

# --- IMPACT METRICS ROW ---
st.markdown("### 📊 PROJECTED IMPACT (FY26)")
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown("""<p class="metric-value">INR 55 Cr</p><p class="metric-label">Immediate Cash Unlocked (Q1)</p>""", unsafe_allow_html=True)
with m2:
    st.markdown("""<p class="metric-value">85%</p><p class="metric-label">Target Factory Utilization</p>""", unsafe_allow_html=True)
with m3:
    st.markdown("""<p class="metric-value">Zero</p><p class="metric-label">Dependencies on 'Pure' Phone Sales</p>""", unsafe_allow_html=True)
with m4:
    st.markdown("""<p class="metric-value">New IP</p><p class="metric-label">EU CBAM & CCTS Compliant</p>""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="kicker-box">
⚠️ IMMEDIATE DECISION REQUIRED: APPROVE LIQUIDATION OF 45,000 UNITS AT 0% MARGIN.<br>
<i>Rationale: We are buying cash flow (INR 35 Cr), not profit. This prevents vendor default.</i>
</div>
""", unsafe_allow_html=True)
