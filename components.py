"""
Streamlit UI components and styling for the PickName application.
"""

import streamlit as st
import time


def apply_custom_css() -> None:
    """Apply custom CSS styling to the Streamlit app."""
    st.markdown("""
        <style>
            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
            
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-10px); }
            }
            
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            
            .pulse {
                animation: pulse 0.6s ease-in-out;
            }
            
            .bounce {
                animation: bounce 0.6s ease-in-out;
            }
            
            .spin {
                animation: spin 1s linear infinite;
            }
            
            .title-box {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 30px;
                border-radius: 10px;
                color: white;
                text-align: center;
                margin-bottom: 20px;
            }
            
            .winner-box {
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                padding: 40px;
                border-radius: 15px;
                color: white;
                text-align: center;
                font-size: 48px;
                font-weight: bold;
                margin: 20px 0;
                box-shadow: 0 8px 32px rgba(245, 87, 108, 0.3);
            }
            
            .stats-box {
                background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                padding: 20px;
                border-radius: 10px;
                color: white;
                margin: 10px 0;
            }
            
            .info-box {
                background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
                padding: 15px;
                border-radius: 10px;
                color: white;
                margin: 10px 0;
            }
        </style>
    """, unsafe_allow_html=True)


def render_title() -> None:
    """Render the application title with animation."""
    st.markdown("""
        <div class="title-box">
            <h1>🎯 PickName - Random Name Selector 🎯</h1>
            <p>Select a random name from your list with beautiful visualizations</p>
        </div>
    """, unsafe_allow_html=True)


def render_winner_box(name: str) -> None:
    """
    Render a highlighted winner box.
    
    Args:
        name: The selected name to display
    """
    st.markdown(f"""
        <div class="winner-box">
            🏆 {name} 🏆
        </div>
    """, unsafe_allow_html=True)


def render_stats_box(content: str) -> None:
    """
    Render a statistics box.
    
    Args:
        content: HTML content to display
    """
    st.markdown(f"""
        <div class="stats-box">
            {content}
        </div>
    """, unsafe_allow_html=True)


def render_info_box(content: str) -> None:
    """
    Render an information box.
    
    Args:
        content: HTML content to display
    """
    st.markdown(f"""
        <div class="info-box">
            {content}
        </div>
    """, unsafe_allow_html=True)


def spinning_animation(names: list, duration: float = 1.5) -> str:
    """
    Display a spinning animation through random names.
    
    Args:
        names: List of names to rotate through
        duration: Total animation duration in seconds
        
    Returns:
        The final selected name
    """
    placeholder = st.empty()
    import random
    
    # Spinning animation
    num_spins = int(15)
    for i in range(num_spins):
        random_name = random.choice(names)
        with placeholder.container():
            st.markdown(f"""
                <div class="winner-box" style="animation: spin {0.5}s linear;">
                    {random_name}
                </div>
            """, unsafe_allow_html=True)
        time.sleep(0.1)
    
    # Return random name (already selected before animation starts)
    return random.choice(names)


def initialize_session_state() -> None:
    """Initialize all session state variables."""
    if 'names_list' not in st.session_state:
        st.session_state.names_list = []
    
    if 'selection_history' not in st.session_state:
        st.session_state.selection_history = []
    
    if 'selected_name' not in st.session_state:
        st.session_state.selected_name = None
    
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False
    
    if 'spinning' not in st.session_state:
        st.session_state.spinning = False


def render_name_input_sidebar() -> None:
    """Render the name input section in the sidebar."""
    with st.sidebar:
        st.header("📋 Setup Names")
        
        input_method = st.radio("Choose input method:", ["Single entry", "Paste list"])
        
        if input_method == "Single entry":
            new_name = st.text_input("Enter a name:", placeholder="Type a name here")
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("➕ Add Name", use_container_width=True):
                    if new_name and new_name not in st.session_state.names_list:
                        st.session_state.names_list.append(new_name)
                        st.success(f"✅ Added: {new_name}")
                    elif new_name in st.session_state.names_list:
                        st.warning("⚠️ Name already exists!")
            
            with col2:
                if st.button("🔄 Clear All", use_container_width=True):
                    st.session_state.names_list = []
                    st.session_state.selection_history = []
                    st.success("Cleared all names!")
                    st.rerun()
        
        else:  # Paste list
            names_text = st.text_area("Paste names (one per line):", height=150)
            if st.button("📥 Load Names", use_container_width=True):
                new_names = [name.strip() for name in names_text.split('\n') if name.strip()]
                st.session_state.names_list = list(set(new_names))
                st.success(f"✅ Loaded {len(st.session_state.names_list)} unique names!")
                st.rerun()
        
        render_names_list_sidebar()


def render_names_list_sidebar() -> None:
    """Render the current names list in the sidebar."""
    st.divider()
    st.subheader("📊 Current Names")
    if st.session_state.names_list:
        for i, name in enumerate(st.session_state.names_list, 1):
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(f"{i}. {name}")
            with col2:
                if st.button("❌", key=f"remove_{name}", help=f"Remove {name}"):
                    st.session_state.names_list.remove(name)
                    st.rerun()
    else:
        st.info("No names added yet. Add some names to get started!")


def render_metric_cards(total_picks: int, most_selected: str, avg_picks: float) -> None:
    """
    Render metric cards for statistics.
    
    Args:
        total_picks: Total number of picks made
        most_selected: Name that was selected the most
        avg_picks: Average picks per person
    """
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Picks", total_picks)
    
    with col2:
        st.metric("Most Selected", most_selected if most_selected else "N/A")
    
    with col3:
        st.metric("Avg per Person", f"{avg_picks:.2f}")
