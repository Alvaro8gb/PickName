"""
PickName - Random Name Selector Application
A Streamlit app for selecting random names from a list with visualizations.
"""

import streamlit as st
from logic import NameSelector

from components import (
    apply_custom_css,
    render_title,
    render_winner_box,
    render_stats_box,
    render_info_box,
    spinning_animation,
    initialize_session_state,
    render_name_input_sidebar,
    render_metric_cards
)
from visualizations import (
    create_distribution_chart,
    create_pie_chart,
    create_comparison_chart,
    create_timeline_chart,
    create_statistics_dataframe
)

# Page configuration
st.set_page_config(
    page_title="PickName - Random Name Selector",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply styling
apply_custom_css()

# Initialize session state
initialize_session_state()

# Sync session state with NameSelector logic
if 'selector' not in st.session_state:
    st.session_state.selector = NameSelector(st.session_state.names_list)
else:
    # Keep selector synced with session state
    st.session_state.selector.names = st.session_state.names_list
    st.session_state.selector.selection_history = st.session_state.selection_history

selector = st.session_state.selector

# Title
render_title()

# Sidebar
render_name_input_sidebar()

# Statistics at the top
if selector.has_history():
    st.header("📈 Statistics")
    stats = selector.get_statistics()
    render_metric_cards(
        stats["total_picks"],
        stats["most_selected"],
        stats["average_picks"]
    )
    st.divider()

# Main content
col1, col2 = st.columns([0.85, 1.15], gap="large")

with col1:
    st.header("🎮 Selection Zone")
    
    if selector.has_names():
        # Pick button
        if st.button(
            "🎲 PICK A RANDOM NAME",
            use_container_width=True,
            key="pick_button",
            help="Click to select a random name!"
        ):
            st.session_state.spinning = True
            st.rerun()
        
        # Spinning animation
        if st.session_state.spinning:
            selected = spinning_animation(selector.names)
            st.session_state.selected_name = selected
            st.session_state.selection_history.append(selected)
            st.session_state.spinning = False
            st.rerun()
        
        # Show result
        if st.session_state.selected_name:
            render_winner_box(st.session_state.selected_name)
            
            count = selector.get_selection_count(st.session_state.selected_name)
            render_stats_box(
                f"✨ This person has been selected <strong>{count}</strong> time(s)! ✨"
            )
    
    else:
        st.warning("👆 Add names first using the sidebar to get started!")

with col2:
    st.header("📊 Distribution & Analytics")
    
    if selector.has_history():
        # Tabs for different visualizations
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Bar Chart", "Pie Chart", "Horizontal", "Timeline", "Table"])
        
        names, counts = selector.get_distribution_data()
        
        with tab1:
            fig = create_distribution_chart(names, counts)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            fig = create_pie_chart(names, counts)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            fig = create_comparison_chart(names, counts)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            fig = create_timeline_chart(selector.selection_history)
            st.plotly_chart(fig, use_container_width=True)
        
        with tab5:
            dist_df = create_statistics_dataframe(selector.get_statistics()["distribution"])
            st.dataframe(dist_df, use_container_width=True, hide_index=True)
    
    else:
        render_info_box("📊 Pick some names to see the distribution charts!")

# Footer
st.divider()
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🗑️ Reset All Data", use_container_width=True):
        selector.reset()
        st.session_state.names_list = []
        st.session_state.selection_history = []
        st.session_state.selected_name = None
        st.session_state.show_result = False
        st.rerun()
