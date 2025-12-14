"""
-----------------------------------------------------------------------------
XYZ MOBILES: A2 STRATEGIC POSTER (BOARDROOM EDITION)
-----------------------------------------------------------------------------
HOW TO RUN:
1. pip install streamlit pandas plotly
2. streamlit run app.py
-----------------------------------------------------------------------------
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- PAGE CONFIGURATION (Wide Mode for Poster Feel) ---
st.set_page_config(
    page_title="XYZ Strategic Reset",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR A2 POSTER LOOK ---
st.markdown("""
    <style>
    /* Global Styles */
    .main { background-color: #ffffff; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h1 { color: #0f2b46; font-size: 3rem; font-weight: 900; letter-spacing: -1px; margin-bottom: 5px; text-transform: uppercase; }
    h2 { color: #555; font-size: 1.2rem; font-weight: 400; margin-top: 0; border-bottom: 4px solid #0f2b46; padding-bottom: 20px; }
    h3 { color: #0f2b46; font-size: 1.4rem; font-weight: 800; border-left: 5px solid #ffcc00; padding-left: 10px; margin-top: 25px; }
    
    /* Box Styles */
    .section-box { border: 1px solid #e0e0e0; background-color: #f9f9f9; padding: 15px; border-radius: 4px; height: 100%; }
    .highlight-box { background-color: #e8f4f8; border-left: 5px solid #007bb5; padding: 15px; margin-bottom: 15px; }
    .urgent-box { background-color: #fff5f5; border-left: 5px solid #d9534f; padding: 15px; margin-bottom: 15px; }
    .kicker-box { background-color: #0f2b46; color: white; padding: 20px; text-align: center; font-size: 1.2rem; font-weight: bold; margin-top: 40px; border-radius: 8px; }
    
    /* Text Styles */
    .metric-big { font-size: 2.2rem; font-weight: 800; color: #0f2b46; line-height: 1; }
    .metric-small { font-size: 0.9rem; color: #666; font-weight: 500; }
    .table-header { font-weight: bold; color: #0f2b46; border-bottom: 2px solid #ddd; padding-bottom: 5px; margin-bottom: 10px; }
    
    /* Hiding Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- TITLE SECTION ---
st.title("PROJECT RESET: STRATEGIC TURNAROUND PLAN")
st.markdown("## FROM 'CASH TRAP' TO 'SUSTAINABLE ECOSYSTEM' | FY 2025-26 ROADMAP")

# --- ROW 1: CONTEXT & INSIGHT ---
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    <div class="urgent-box">
    <b>🛑 THE URGENT REALITY (THE BLEED)</b><br>
    We are fighting a losing battle in the "Red Ocean" of budget phones.
    <ul style="margin-top:5px; padding-left:20px;">
        <li><b>Cash Locked:</b> ₹25 Cr in depreciating inventory (Models X, Y).</li>
        <li><b>Idle Asset:</b> Factory running at only 30% capacity.</li>
        <li><b>Competition:</b> Dixon & Foxconn own the volume game; we cannot compete on price.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box">
    <b>💡 THE STRATEGIC PIVOT (THE BLUE OCEAN)</b><br>
    <b>Don't sell phones. Sell "Green Utility".</b><br>
    Our survival depends on a "Hybrid Pivot":
    <ol style="margin-top:5px; padding-left:20px;">
        <li><b>Manufacturing (B2B):</b> Become a specialized "Component Hub" for Chinese JVs (Lianchuang/Sunwoda) avoiding tariffs.</li>
        <li><b>Brand (B2C):</b> Pivot the consumer brand to <b>"India's First Carbon-Neutral Tech"</b>. Own the niche nobody else is touching.</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)

# --- ROW 2: STRATEGIC PARTNERSHIP LANDSCAPE (NEW) ---
st.markdown("### 1. STRATEGIC PARTNERSHIP LANDSCAPE (THE 'WHO')")
st.markdown("<i>Targeting 'China+1' players who need Indian assembly to bypass import duties.</i>")

# Creating a clean HTML table for layout control
st.markdown("""
<table style="width:100%; border-collapse: collapse; margin-bottom: 20px;">
  <tr style="background-color: #0f2b46; color: white; text-align: left;">
    <th style="padding: 10px;">TARGET PARTNER</th>
    <th style="padding: 10px;">THEIR PAIN POINT</th>
    <th style="padding: 10px;">OUR PITCH (THE VALUE PROP)</th>
    <th style="padding: 10px;">EST. IMPACT</th>
  </tr>
  <tr style="border-bottom: 1px solid #ddd;">
    <td style="padding: 10px;"><b>SUNWODA</b><br>(Batteries/Power)</td>
    <td style="padding: 10px;">Needs capacity for EV/Power Walls in India but building new plants takes 18 months.</td>
    <td style="padding: 10px;">"We give you Line 3 for <b>Wireless Charging Coil</b> assembly immediately. No Capex for you."</td>
    <td style="padding: 10px;"><b>40%</b> Utilization</td>
  </tr>
  <tr style="border-bottom: 1px solid #ddd;">
    <td style="padding: 10px;"><b>LIANCHUANG</b><br>(Optics/Lenses)</td>
    <td style="padding: 10px;">Investing $50M in India (Apr '25 news) but needs quick "Optical Module" assembly to supply Vivo/Oppo.</td>
    <td style="padding: 10px;">"We become your <b>Precision Assembly Hub</b>. We handle the labor; you bring the tech."</td>
    <td style="padding: 10px;"><b>12%</b> Margin</td>
  </tr>
  <tr>
    <td style="padding: 10px;"><b>NVIDIA PARTNERS</b><br>(Edge AI)</td>
    <td style="padding: 10px;">High demand for "Jetson" AI modules in robotics; few Indian assemblers have clean rooms.</td>
    <td style="padding: 10px;">"Pivot Line 1 to <b>OSAT (Assembly & Test)</b> for high-margin AI hardware."</td>
    <td style="padding: 10px;"><b>Future Proofing</b></td>
  </tr>
</table>
""", unsafe_allow_html=True)

# --- ROW 3: COMPETITIVE BENCHMARKING (NEW) ---
c3, c4 = st.columns([1, 1])

with c3:
    st.markdown("### 2. THE SHIFT: RED vs BLUE OCEAN")
    
    # Scatter plot for Positioning
    df_pos = pd.DataFrame({
        'Brand': ['Xiaomi/Samsung', 'Dixon (White Label)', 'XYZ (OLD)', 'Fairphone (Global)', 'XYZ (NEW)'],
        'Price': [8, 4, 5, 9, 6],  # X-axis
        'Sustainability': [2, 1, 1, 10, 9], # Y-axis
        'Size': [80, 60, 30, 40, 60],
        'Color': ['red', 'grey', 'red', 'green', 'blue']
    })
    
    fig_pos = px.scatter(df_pos, x='Price', y='Sustainability', text='Brand', size='Size', 
                         color='Color', color_discrete_map={'red':'#e63946', 'grey':'#a8dadc', 'green':'#2a9d8f', 'blue':'#457b9d'},
                         title="Brand Positioning Matrix")
    fig_pos.update_traces(textposition='top center')
    fig_pos.update_layout(
        xaxis_title="Price Point", 
        yaxis_title="Sustainability / Green Cert",
        showlegend=False,
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        plot_bgcolor='#f9f9f9'
    )
    st.plotly_chart(fig_pos, use_container_width=True)

with c4:
    st.markdown("### 3. COMPETITIVE LANDSCAPE (INDIA)")
    st.markdown("""
    <div class="section-box">
    <table style="width:100%; font-size: 0.9rem;">
      <tr style="border-bottom: 2px solid #ddd;">
        <th style="text-align:left;">FEATURE</th>
        <th style="text-align:left;">DIXON / FOXCONN</th>
        <th style="text-align:left; color:#007bb5;">XYZ (THE PIVOT)</th>
      </tr>
      <tr>
        <td><b>Core Game</b></td>
        <td>Volume (Millions of units)</td>
        <td style="color:#007bb5;"><b>Niche (Sustainability + Components)</b></td>
      </tr>
      <tr>
        <td><b>Margin</b></td>
        <td>Razor Thin (3-4%)</td>
        <td style="color:#007bb5;"><b>Healthy (8-12%)</b></td>
      </tr>
      <tr>
        <td><b>Regulatory</b></td>
        <td>PLI Dependent</td>
        <td style="color:#007bb5;"><b>CCTS / CBAM Compliant</b></td>
      </tr>
      <tr>
        <td><b>Inventory</b></td>
        <td>High Risk</td>
        <td style="color:#007bb5;"><b>Just-in-Time (Contract Mfg)</b></td>
      </tr>
    </table>
    <br>
    <i><b>Insight:</b> We cannot beat Dixon on volume. We beat them by being the "Greenest" and "Most Flexible".</i>
    </div>
    """, unsafe_allow_html=True)

# --- ROW 4: EXECUTION & FINANCIALS ---
st.markdown("### 4. EXECUTION ROADMAP & FINANCIAL IMPACT")

c5, c6 = st.columns([1, 1])

with c5:
    st.markdown("**💰 FINANCIAL RECOVERY BRIDGE (₹ Cr)**")
    # Waterfall Chart
    fig_water = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "relative", "relative", "total"],
        x = ["Deficit", "Bulk Sale", "Scrap Harvest", "Coupon Rev", "JV Rent", "OpEx Savings", "Net Cash"],
        text = ["-25", "+12", "+3.5", "+4.0", "+8.0", "+2.5", "5.0"],
        y = [-25, 12, 3.5, 4.0, 8.0, 2.5, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
        decreasing = {"marker":{"color":"#e63946"}},
        increasing = {"marker":{"color":"#2a9d8f"}},
        totals = {"marker":{"color":"#1d3557"}}
    ))
    fig_water.update_layout(height=300, margin=dict(l=20, r=20, t=20, b=20), plot_bgcolor='#ffffff')
    st.plotly_chart(fig_water, use_container_width=True)

with c6:
    st.markdown("**🗓️ 12-MONTH GANTT CHART**")
    # Gantt Data
    df_gantt = pd.DataFrame([
        dict(Task="Phase 1: Liquidity (Bulk Sales)", Start='2025-01-01', Finish='2025-03-30', Phase='Stabilize'),
        dict(Task="Vendor Payment Clearing", Start='2025-02-15', Finish='2025-04-01', Phase='Stabilize'),
        dict(Task="JV Setup (Sunwoda/Lianchuang)", Start='2025-04-01', Finish='2025-08-30', Phase='Pivot'),
        dict(Task="ERP Clean-up (AI Integration)", Start='2025-03-01', Finish='2025-06-01', Phase='Pivot'),
        dict(Task="Launch 'Carbon Neutral' Phone", Start='2025-09-01', Finish='2025-12-31', Phase='Grow'),
        dict(Task="CCTS Carbon Credit Trading", Start='2025-10-01', Finish='2025-12-31', Phase='Grow')
    ])
    fig_gantt = px.timeline(df_gantt, x_start="Start", x_end="Finish", y="Task", color="Phase",
                            color_discrete_map={"Stabilize": "#e63946", "Pivot": "#f4a261", "Grow": "#2a9d8f"})
    fig_gantt.update_yaxes(autorange="reversed")
    fig_gantt.update_layout(height=300, margin=dict(l=20, r=20, t=20, b=20), plot_bgcolor='#ffffff')
    st.plotly_chart(fig_gantt, use_container_width=True)

# --- ROW 5: TURNAROUND SWOT (NEW) ---
st.markdown("### 5. TURNAROUND SWOT (THE REALITY CHECK)")

swot1, swot2, swot3, swot4 = st.columns(4)

with swot1:
    st.markdown("""
    <div class="section-box" style="border-top: 3px solid #2a9d8f;">
    <b>STRENGTH (Internal)</b><br>
    - Fully owned Manufacturing Plant (Asset Rich).<br>
    - Service Center Network (High Trust).<br>
    - 10 Years of Customer Data.
    </div>
    """, unsafe_allow_html=True)

with swot2:
    st.markdown("""
    <div class="section-box" style="border-top: 3px solid #e63946;">
    <b>WEAKNESS (Internal)</b><br>
    - Cash Crunch (Liquidity Crisis).<br>
    - Brand Perception ("Old School").<br>
    - Outdated ERP/Tech Stack.
    </div>
    """, unsafe_allow_html=True)

with swot3:
    st.markdown("""
    <div class="section-box" style="border-top: 3px solid #2a9d8f;">
    <b>OPPORTUNITY (External)</b><br>
    - <b>CCTS/CBAM:</b> Carbon Credit Revenue.<br>
    - <b>China+1:</b> JVs with Lianchuang/Sunwoda.<br>
    - <b>Tier 2 Aspiration:</b> Green Tech status.
    </div>
    """, unsafe_allow_html=True)

with swot4:
    st.markdown("""
    <div class="section-box" style="border-top: 3px solid #e63946;">
    <b>THREAT (External)</b><br>
    - <b>Dixon:</b> Aggressive capacity expansion.<br>
    - <b>Vendor Revolt:</b> If payments delayed >90 days.<br>
    - <b>Tech Obsolescence:</b> AI moving too fast.
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="kicker-box">
⚠️ IMMEDIATE ASK: APPROVAL TO LIQUIDATE 15,000 UNITS AT 0% MARGIN (CTC) BY MONTH END.<br>
<span style="font-size: 0.9rem; font-weight: normal;">This unlocks the ₹12 Cr needed to sign the JV deals and pay critical vendors.</span>
</div>
""", unsafe_allow_html=True)
