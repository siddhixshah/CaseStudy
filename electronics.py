import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="XYZ Mobiles | Project Reset",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR "CONSULTANT" LOOK ---
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    h1 {
        color: #0f2b46;
        font-family: 'Helvetica', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
    }
    h2, h3 {
        color: #2c3e50;
        font-family: 'Helvetica', sans-serif;
        font-weight: 600;
    }
    .metric-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 5px;
        border-left: 5px solid #0f2b46;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .insight-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 5px;
        color: #0f2b46;
        font-weight: 500;
        border: 1px solid #d1e7ef;
    }
    .urgent-box {
        background-color: #fff3cd;
        padding: 15px;
        border-radius: 5px;
        color: #856404;
        border: 1px solid #ffeeba;
    }
    .kicker-box {
        background-color: #0f2b46;
        color: white;
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("PROJECT RESET: FY25-26 STRATEGIC TURNAROUND")
st.markdown("### From 'Cash Trap' to 'Sustainable Ecosystem'")
st.markdown("---")

# --- ROW 1: PROBLEM & INSIGHT ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🛑 The Core Problem")
    st.write("""
    **Liquidity Paralysis.**
    We are asset-rich but cash-poor. 
    * **₹25 Cr** trapped in stagnant inventory.
    * **40%** factory underutilization.
    * Fighting a "Feature War" we cannot win against giants, draining resources.
    """)

with col2:
    st.subheader("💡 Primary Insight")
    st.markdown("""
    <div class="insight-box">
    We must stop competing on <b>Specs</b> and start competing on <b>Infrastructure</b>.
    <br><br>
    The pivot is <b>"Hybrid Manufacturing"</b>: Monetize the factory via B2B contracts (Components/JVs) to cover overheads, 
    while treating the Consumer Brand (B2C) as a niche "Green/ESG" vertical to command higher margins.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- ROW 2: ACTION PLAN & METRICS ---
col3, col4 = st.columns([1.5, 1])

with col3:
    st.subheader("📋 3-Point Action Plan")
    
    tab1, tab2, tab3 = st.tabs(["1. Liquidity (Q1)", "2. Utilization (Q2)", "3. Rebrand (Q3)"])
    
    with tab1:
        st.markdown("**Objective: Operation Clean Slate**")
        st.markdown("""
        - **B2B Bulk Exit:** Sell 15k units to Logistics/Pharma partners at **Cost-to-Company (Flat)**. Speed > Profit.
        - **Scrap Harvest:** Dismantle unsellable 'Model Y' stock. Use screens/batteries for Service Centers (saving 15% on parts procurement).
        - **Coupon Lock-in:** Issue ₹5k "Deferred Value" coupons to existing CRM database instead of brand-damaging discounts.
        """)
        
    with tab2:
        st.markdown("**Objective: The 'Component' Pivot**")
        st.markdown("""
        - **The JV:** Sign with **Lianchuang/Similar** for Wireless Charging Coil assembly.
        - **Target:** Allocate 40% of floor space to JV. This covers fixed factory electricity/labor costs.
        - **Shift:** Move from "Box Assembly" to "Precision Components" (OSAT focus).
        """)
        
    with tab3:
        st.markdown("**Objective: The 'Green' Niche**")
        st.markdown("""
        - **Differentiation:** India’s first **CCTS-Compliant** (Carbon Credit) manufacturer.
        - **USP:** "The Carbon-Neutral Phone." Target Gen Z in Tier 2 cities via regional micro-influencers.
        - **Digital:** Fix 2017 ERP silos. Python scripts to clean 10 years of data for reactivation.
        """)

with col4:
    st.subheader("📈 Topline Impact Metrics")
    
    # Custom Metric Cards
    m1, m2 = st.columns(2)
    with m1:
        st.markdown('<div class="metric-box"><h3>₹12 Cr</h3><p>Working Capital Recovered (Q1)</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-box"><h3>60%</h3><p>Factory Utilization (Target Q3)</p></div>', unsafe_allow_html=True)
    
    st.write("") # Spacer
    
    m3, m4 = st.columns(2)
    with m3:
        st.markdown('<div class="metric-box"><h3>25%</h3><p>Burn Rate Reduction</p></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-box"><h3>Q4</h3><p>First Carbon Credit Revenue</p></div>', unsafe_allow_html=True)

st.markdown("---")

# --- ROW 3: URGENT ISSUE & ROADMAP VISUALIZATION ---

st.subheader("🔥 The Single Most Urgent Issue: Cash Trap")
st.markdown("""
<div class="urgent-box">
<b>The Bleeding Must Stop.</b> We cannot invest in the JV or R&D while capital is locked in depreciating stock. 
Leadership must prioritize <b>Liquidity over Profitability</b> for the next 90 days.
</div>
""", unsafe_allow_html=True)

st.write("")

# --- VISUALIZATIONS ---
v_col1, v_col2 = st.columns(2)

# 1. WATERFALL CHART (Financial Recovery)
with v_col1:
    st.markdown("### 💰 Financial Bridge: Recovery Plan")
    
    fig_waterfall = go.Figure(go.Waterfall(
        name = "20", orientation = "v",
        measure = ["relative", "relative", "relative", "relative", "relative", "relative", "total"],
        x = ["Current Gap", "Bulk Sale", "Scrap Harvest", "Coupon Rev", "JV Deposit", "OpEx Savings", "Net Cash Position"],
        textposition = "outside",
        text = ["-25", "+12", "+3.5", "+4.0", "+8.0", "+2.5", "+5.0"],
        y = [-25, 12, 3.5, 4.0, 8.0, 2.5, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
        decreasing = {"marker":{"color":"#ef553b"}},
        increasing = {"marker":{"color":"#00cc96"}},
        totals = {"marker":{"color":"#0f2b46"}}
    ))

    fig_waterfall.update_layout(
        title = "Working Capital Recovery (₹ Cr)",
        showlegend = False,
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig_waterfall, use_container_width=True)

# 2. GANTT CHART (Roadmap)
with v_col2:
    st.markdown("### 🗓️ 12-Month Execution Roadmap")
    
    df_gantt = pd.DataFrame([
        dict(Task="Phase 1: Liquidity (Bulk Sales)", Start='2025-01-01', Finish='2025-03-30', Phase='Stabilize'),
        dict(Task="Vendor Negotiation", Start='2025-02-01', Finish='2025-03-15', Phase='Stabilize'),
        dict(Task="Phase 2: JV Setup (Retooling)", Start='2025-04-01', Finish='2025-08-30', Phase='Pivot'),
        dict(Task="Digital ERP Overhaul", Start='2025-04-01', Finish='2025-06-30', Phase='Pivot'),
        dict(Task="Phase 3: 'Green' Brand Launch", Start='2025-09-01', Finish='2025-12-31', Phase='Grow'),
        dict(Task="Carbon Credit Trading", Start='2025-11-01', Finish='2025-12-31', Phase='Grow')
    ])

    fig_gantt = px.timeline(df_gantt, x_start="Start", x_end="Finish", y="Task", color="Phase",
                            color_discrete_map={"Stabilize": "#ef553b", "Pivot": "#ffa15a", "Grow": "#00cc96"})
    fig_gantt.update_yaxes(autorange="reversed") # tasks top to bottom
    fig_gantt.update_layout(height=400, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_gantt, use_container_width=True)

# --- FOOTER / KICKER ---
st.markdown("""
<div class="kicker-box">
<b>⚠️ IMMEDIATE DECISION REQUIRED:</b><br>
Authorization to liquidate 15,000 units of legacy stock at <b>0% Margin</b> (Cost-to-Company) to unlock ₹12 Cr working capital by Month-End.
</div>
""", unsafe_allow_html=True)
