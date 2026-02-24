# PickName - Random Name Selector App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pickname.streamlit.app/)
   
A beautiful Streamlit application to randomly select names from a list with visual animations and statistics.

## Features

✨ **Key Features:**
- 📋 Add names individually or paste a list
- 🎲 Random name selection with spinning animation
- 📊 Multiple interactive charts (bar, pie, horizontal, timeline)
- 📈 Live statistics (total picks, most selected, average per person)
- 🎨 Smooth animations and gradient UI
- 💾 Persistent selection history
- 🗑️ Easy name management (add, remove, clear all)

## Installation

1. **Clone or download this project**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## How to Use

1. **Add Names:**
   - Use the sidebar to add names one by one, or paste a list of names
   - Remove individual names or clear all

2. **Pick a Name:**
   - Click the "🎲 PICK A RANDOM NAME" button
   - Watch the spinning animation as the name is selected
   - The selected name appears in a beautiful highlight box

3. **View Statistics:**
   - Right side shows multiple visualization options via tabs
   - See how many times each name has been picked
   - View detailed statistics and timelines

## Project Structure

```
PickName/
├── app.py                # Main application orchestration
├── logic.py              # Business logic (NameSelector class)
├── components.py         # Streamlit UI components & styling
├── visualizations.py     # Plotly chart creation functions
├── requirements.txt      # Dependencies
└── README.md            # This file
```

## Module Architecture

### `logic.py` - Core Business Logic
Contains the `NameSelector` class that handles:
- Name management (add, remove, clear)
- Random selection and history tracking
- Statistics calculation
- Distribution data generation

**Main Class:** `NameSelector`
- `add_name()` - Add single name
- `add_names_batch()` - Add multiple names
- `pick_random()` - Select random name and record
- `get_statistics()` - Calculate selection statistics
- `get_distribution_data()` - Get data for visualizations

### `components.py` - UI Components
Contains Streamlit-specific UI functions:
- Custom CSS styling (`apply_custom_css()`)
- Component rendering functions
- Session state initialization
- Animation handlers

**Main Functions:**
- `apply_custom_css()` - Apply custom styling
- `render_title()` - Display app title
- `render_winner_box()` - Show selected name
- `render_metric_cards()` - Display statistics
- `spinning_animation()` - Animate name selection
- `initialize_session_state()` - Setup Streamlit state
- `render_name_input_sidebar()` - Sidebar UI

### `visualizations.py` - Data Visualization
Contains Plotly visualization functions:
- Bar charts
- Pie charts
- Horizontal bar charts
- Timeline/scatter plots
- DataFrame preparation

**Main Functions:**
- `create_distribution_chart()` - Vertical bar chart
- `create_pie_chart()` - Proportional pie chart
- `create_comparison_chart()` - Horizontal bar chart
- `create_timeline_chart()` - Selection timeline
- `create_statistics_dataframe()` - Prepare DataFrame

### `app.py` - Main Application
Orchestrates all modules:
- Initializes components
- Manages user interactions
- Coordinates between logic and UI
- Handles session state

## Technical Stack

- **Streamlit** - Web app framework
- **Plotly** - Interactive visualizations
- **Pandas** - Data handling
- **Python** - Core language

## Customization

You can easily extend the app:

### Add New Visualizations
Add new functions to `visualizations.py`:
```python
def create_custom_chart(names, counts):
    # Your chart logic here
    fig = px.scatter(...)
    return fig
```

Then use it in `app.py`:
```python
with tab_new:
    fig = create_custom_chart(names, counts)
    st.plotly_chart(fig, use_container_width=True)
```

### Add New Features
1. Add logic to `logic.py` (NameSelector class)
2. Add UI in `components.py`
3. Orchestrate in `app.py`

### Modify Styling
Edit the CSS in `components.py` `apply_custom_css()` function.

## Tips

- Use the "Paste list" option to quickly load many names
- Selection history is maintained during the session
- Reset all data to start fresh with a new set of names
- The charts update in real-time after each selection
- Multiple visualization options help you understand the data better

## Design Philosophy

The application follows these design principles:

1. **Separation of Concerns** - Logic, visualization, and UI are separated
2. **Reusability** - Components and functions are modular and reusable
3. **Maintainability** - Clear naming and documentation for easy updates
4. **Scalability** - Easy to add new features without modifying existing code
5. **User Experience** - Beautiful animations and intuitive interface

Enjoy picking random names! 🎯

