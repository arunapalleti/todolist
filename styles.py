import streamlit as st

def apply_custom_styles():
    """Applies global CSS styles to the Streamlit app based on the active theme."""
    # Ensure dark mode key exists in session state
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    # Get current theme state
    dark = st.session_state.dark_mode

    # CSS color definitions based on theme
    if dark:
        bg_color = "#111827"  # Dark Charcoal
        card_bg = "#1F2937"   # Slate Blue/Gray
        text_primary = "#F9FAFB"
        text_secondary = "#9CA3AF"
        border_color = "#374151"
        shadow = "0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2)"
    else:
        bg_color = "#FFFFFF"  # Pure White
        card_bg = "#F9FAFB"   # Cool Gray Tint
        text_primary = "#1F2937"
        text_secondary = "#4B5563"
        border_color = "#E5E7EB"
        shadow = "0 4px 6px -1px rgba(79, 70, 229, 0.04), 0 2px 4px -1px rgba(0, 0, 0, 0.02)"

    primary_color = "#4F46E5"  # Indigo Primary Accent
    success_color = "#10B981"  # Emerald Green
    warning_color = "#F59E0B"  # Amber Yellow
    danger_color = "#EF4444"   # Rose Red

    # Custom CSS injection
    css = f"""
    <style>
    /* Main app canvas */
    .stApp {{
        background-color: {bg_color} !important;
        color: {text_primary} !important;
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
    }}
    
    /* Headers & Labels */
    h1, h2, h3, h4, h5, h6, label {{
        color: {text_primary} !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
    }}
    
    /* Metrics panel customization */
    div[data-testid="stMetricValue"] {{
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        color: {primary_color} !important;
        letter-spacing: -0.025em;
    }}
    
    div[data-testid="stMetricLabel"] p {{
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: {text_secondary} !important;
    }}

    /* Elegant Custom Card styles */
    .todo-card {{
        background-color: {card_bg};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: {shadow};
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }}
    
    .todo-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 12px 20px -8px rgba(79, 70, 229, 0.15), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-color: {primary_color};
    }}
    
    .card-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }}
    
    .task-title-text {{
        font-size: 1.2rem;
        font-weight: 700;
        color: {text_primary};
        margin: 0;
        letter-spacing: -0.01em;
    }}
    
    .task-desc-text {{
        font-size: 0.95rem;
        color: {text_secondary};
        margin-bottom: 14px;
        line-height: 1.5;
    }}
    
    .task-footer {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.8rem;
        color: {text_secondary};
        border-top: 1px dashed {border_color};
        padding-top: 12px;
        margin-top: 12px;
    }}
    
    /* Badges */
    .badge {{
        padding: 5px 10px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.025em;
        text-transform: uppercase;
        display: inline-block;
    }}
    
    .badge-priority-high {{
        background-color: rgba(239, 68, 68, 0.12);
        color: {danger_color};
        border: 1px solid rgba(239, 68, 68, 0.25);
    }}
    
    .badge-priority-medium {{
        background-color: rgba(245, 158, 11, 0.12);
        color: {warning_color};
        border: 1px solid rgba(245, 158, 11, 0.25);
    }}
    
    .badge-priority-low {{
        background-color: rgba(16, 185, 129, 0.12);
        color: {success_color};
        border: 1px solid rgba(16, 185, 129, 0.25);
    }}
    
    .badge-category {{
        background-color: rgba(79, 70, 229, 0.08);
        color: {primary_color};
        border: 1px solid rgba(79, 70, 229, 0.2);
    }}
    
    .badge-completed {{
        background-color: rgba(16, 185, 129, 0.12);
        color: {success_color};
        border: 1px solid rgba(16, 185, 129, 0.25);
    }}

    /* Global Input controls styling */
    .stTextInput input, .stTextArea textarea, .stSelectbox select, .stDateInput input {{
        background-color: {card_bg} !important;
        color: {text_primary} !important;
        border: 1px solid {border_color} !important;
        border-radius: 8px !important;
    }}
    
    /* Button theme injection */
    div.stButton > button {{
        background-color: {primary_color} !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.15) !important;
    }}
    
    div.stButton > button:hover {{
        background-color: #4338CA !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.25) !important;
    }}
    
    div.stButton > button:active {{
        transform: translateY(1px) !important;
    }}

    /* Custom sidebar modifications */
    section[data-testid="stSidebar"] {{
        background-color: {card_bg} !important;
        border-right: 1px solid {border_color} !important;
    }}
    
    section[data-testid="stSidebar"] div.stButton > button {{
        background-color: transparent !important;
        color: {text_primary} !important;
        border: 1px solid {border_color} !important;
        box-shadow: none !important;
        width: 100%;
    }}
    
    section[data-testid="stSidebar"] div.stButton > button:hover {{
        background-color: {border_color} !important;
        color: {primary_color} !important;
    }}

    /* Animation success notification */
    @keyframes checkmark-burst {{
        0% {{ transform: scale(0.9); opacity: 0.4; }}
        70% {{ transform: scale(1.04); opacity: 0.9; }}
        100% {{ transform: scale(1); opacity: 1; }}
    }}
    
    .animated-success-card {{
        animation: checkmark-burst 0.45s cubic-bezier(0.34, 1.56, 0.64, 1);
        border: 1.5px solid {success_color} !important;
        background-color: rgba(16, 185, 129, 0.04) !important;
    }}

    /* Dataframe table enhancements */
    .dataframe {{
        border: 1px solid {border_color} !important;
        border-radius: 8px !important;
    }}
    
    .dataframe th {{
        background-color: {primary_color} !important;
        color: white !important;
        font-weight: 600 !important;
    }}
    
    .dataframe td {{
        border-bottom: 1px solid {border_color} !important;
        background-color: {card_bg} !important;
        color: {text_primary} !important;
    }}

    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def render_sidebar_header():
    """Renders a modern header in the sidebar, with theme configuration and utilities."""
    st.sidebar.markdown(
        """
        <div style='display: flex; align-items: center; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid rgba(128,128,128,0.2);'>
            <div style='background-color: #4F46E5; width: 44px; height: 44px; border-radius: 10px; display: flex; align-items: center; justify-content: center; margin-right: 12px; box-shadow: 0 4px 10px rgba(79, 70, 229, 0.35);'>
                <span style='color: white; font-weight: 800; font-size: 1.4rem;'>S</span>
            </div>
            <div>
                <h2 style='margin: 0; font-size: 1.35rem; font-weight: 800; color: #4F46E5; letter-spacing: -0.02em;'>SmartTodo</h2>
                <p style='margin: 0; font-size: 0.78rem; color: #6B7280; font-weight: 500;'>Organize intelligently</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Theme configuration
    st.sidebar.markdown("<h4 style='font-size: 0.9rem; font-weight: 700; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em; color: gray;'>Preferences</h4>", unsafe_allow_html=True)
    dark_mode = st.sidebar.toggle("Dark Mode 🌙", value=st.session_state.get("dark_mode", False))
    if dark_mode != st.session_state.get("dark_mode", False):
        st.session_state.dark_mode = dark_mode
        st.rerun()
