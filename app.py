import sys
import os

# Add root directory to python path
root_dir = os.path.dirname(os.path.abspath(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

import streamlit as st
import pandas as pd
from datetime import datetime

from utils.database import load_tasks, load_history
from utils.styles import apply_custom_styles, render_sidebar_header
from utils.helper import format_datetime_pretty

# Page setup
st.set_page_config(
    page_title="SmartTodo - Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply styling and sidebar header
apply_custom_styles()
render_sidebar_header()

# Sidebar: Auto Refresh Feature
st.sidebar.markdown("---")
st.sidebar.markdown("<h4 style='font-size: 0.9rem; font-weight: 700; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.05em; color: gray;'>Dashboard Utility</h4>", unsafe_allow_html=True)
auto_refresh = st.sidebar.checkbox("Auto Refresh (30s) 🔄", value=False)
if auto_refresh:
    # Inject JavaScript that reloads the window parent context after 30 seconds
    st.components.v1.html(
        """
        <script>
            setTimeout(function() {
                window.parent.location.reload();
            }, 30000);
        </script>
        """,
        height=0
    )

# Page Header Banner
today_str = datetime.now().strftime("%A, %B %d, %Y")
st.markdown(
    f"""
    <div style='background: linear-gradient(135deg, #4F46E5 0%, #312E81 100%); padding: 30px; border-radius: 16px; margin-bottom: 30px; box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3);'>
        <h1 style='margin: 0; color: white !important; font-size: 2.2rem; font-weight: 800;'>Dashboard</h1>
        <p style='margin: 5px 0 0 0; color: #E0E7FF !important; font-size: 1rem; font-weight: 500;'>Welcome back! Here is your productivity summary for {today_str}.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Load data
active_tasks = load_tasks()
completed_history = load_history()

total_pending = len(active_tasks)
total_completed = len(completed_history)
total_tasks = total_pending + total_completed

# Statistics Calculations
if total_tasks > 0:
    completion_rate = int((total_completed / total_tasks) * 100)
else:
    completion_rate = 0

# Metrics Layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Tasks", total_tasks)
with col2:
    st.metric("Pending Tasks", total_pending)
with col3:
    st.metric("Completed Tasks", total_completed)
with col4:
    st.metric("Completion Rate", f"{completion_rate}%")

# Progress Bar
st.markdown("### Completion Progress")
st.progress(completion_rate / 100.0)
st.markdown(f"**{completion_rate}%** of your tasks are completed. Keep going!")
st.markdown("---")

# Main Content Layout: Charts vs Recent Tasks
left_col, right_col = st.columns([3, 2])

with left_col:
    st.markdown("### Task Statistics & Distribution")
    
    if total_pending > 0:
        # Create DataFrame for pending tasks
        df_pending = pd.DataFrame(active_tasks)
        
        tab1, tab2 = st.tabs(["Priority Distribution", "Category Breakdown"])
        
        with tab1:
            # Group by priority
            priority_counts = df_pending['priority'].value_counts().reindex(["High", "Medium", "Low"]).fillna(0).astype(int)
            chart_data = pd.DataFrame({'Tasks Count': priority_counts})
            st.bar_chart(chart_data, color="#4F46E5")
            
        with tab2:
            # Group by category
            category_counts = df_pending['category'].value_counts()
            st.bar_chart(category_counts, color="#10B981")
            
        # Download Data Options
        st.markdown("#### Export Active Tasks")
        csv_data = df_pending.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Active Tasks as CSV",
            data=csv_data,
            file_name=f"active_tasks_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("🎉 All caught up! Add tasks in the Task Page to view statistics.")

with right_col:
    st.markdown("### Recent Tasks")
    if total_pending > 0:
        # Sort active tasks by creation date (newest first) and select top 3
        sorted_tasks = sorted(active_tasks, key=lambda x: x.get("created_at", ""), reverse=True)[:3]
        
        for task in sorted_tasks:
            # Render card using clean custom CSS
            priority = task.get("priority", "Low")
            category = task.get("category", "Personal")
            title = task.get("title", "Untitled Task")
            desc = task.get("description", "")
            deadline = task.get("deadline", "No Deadline")
            created_at = format_datetime_pretty(task.get("created_at", ""))
            
            st.markdown(f"""
            <div class="todo-card">
                <div class="card-header">
                    <span class="task-title-text">{title}</span>
                    <span class="badge badge-priority-{priority.lower()}">{priority} Priority</span>
                </div>
                <p class="task-desc-text">{desc}</p>
                <div class="task-footer">
                    <span class="badge badge-category">{category}</span>
                    <span>📅 Due: {deadline}</span>
                </div>
                <div style="font-size: 0.72rem; color: #9CA3AF; margin-top: 6px; text-align: right;">
                    Added: {created_at}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("<p style='font-size: 0.9rem; text-align: center;'><a href='/Task_Page' target='_self'>View and manage all tasks in the Task Page &rarr;</a></p>", unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div style='border: 2px dashed #E5E7EB; border-radius: 12px; padding: 40px; text-align: center; color: #6B7280;'>
                <p style='font-size: 1.2rem; font-weight: 600; margin: 0;'>No Pending Tasks Found</p>
                <p style='font-size: 0.9rem; margin: 8px 0 0 0;'>Use the sidebar page navigation to add some tasks!</p>
            </div>
            """,
            unsafe_allow_html=True
        )
