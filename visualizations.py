"""
Visualization components using Plotly for the PickName application.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Tuple


def create_distribution_chart(names: List[str], counts: List[int]) -> go.Figure:
    """
    Create an interactive distribution histogram.
    
    Args:
        names: List of names
        counts: List of corresponding selection counts
        
    Returns:
        Plotly figure
    """
    df = pd.DataFrame({
        'Name': names,
        'Times Selected': counts
    })
    
    fig = px.bar(
        df,
        x='Name',
        y='Times Selected',
        title='Selection Distribution',
        labels={'Times Selected': 'Number of Times', 'Name': 'Names'},
        color='Times Selected',
        color_continuous_scale='Viridis',
        text='Times Selected'
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        height=300,
        showlegend=False,
        hovermode='x unified',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_tickangle=-45
    )
    
    return fig


def create_pie_chart(names: List[str], counts: List[int]) -> go.Figure:
    """
    Create a pie chart of selection distribution.
    
    Args:
        names: List of names
        counts: List of corresponding selection counts
        
    Returns:
        Plotly figure
    """
    fig = px.pie(
        values=counts,
        names=names,
        title='Selection Distribution (Proportional)',
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    
    fig.update_layout(
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig


def create_comparison_chart(names: List[str], counts: List[int]) -> go.Figure:
    """
    Create a horizontal bar chart for better readability with many names.
    
    Args:
        names: List of names
        counts: List of corresponding selection counts
        
    Returns:
        Plotly figure
    """
    df = pd.DataFrame({
        'Name': names,
        'Times Selected': counts
    }).sort_values('Times Selected', ascending=True)  # Ascending for horizontal bar
    
    fig = px.bar(
        df,
        x='Times Selected',
        y='Name',
        title='Selection Distribution (Horizontal)',
        labels={'Times Selected': 'Number of Times'},
        color='Times Selected',
        color_continuous_scale='Plasma',
        text='Times Selected'
    )
    
    fig.update_traces(textposition='outside')
    fig.update_layout(
        height=max(280, len(names) * 25),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig


def create_timeline_chart(selection_history: List[str]) -> go.Figure:
    """
    Create a timeline showing selections over time.
    
    Args:
        selection_history: List of selected names in order
        
    Returns:
        Plotly figure
    """
    df = pd.DataFrame({
        'Pick #': range(1, len(selection_history) + 1),
        'Name': selection_history
    })
    
    fig = px.scatter(
        df,
        x='Pick #',
        y='Name',
        hover_data=['Name'],
        title='Selection Timeline',
        labels={'Pick #': 'Selection Number', 'Name': 'Name'},
    )
    
    fig.update_traces(marker=dict(size=10))
    fig.update_layout(
        height=300,
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode='closest'
    )
    
    return fig


def create_statistics_dataframe(distribution: Dict[str, int]) -> pd.DataFrame:
    """
    Create a statistics dataframe from distribution data.
    
    Args:
        distribution: Dictionary of name -> count
        
    Returns:
        Pandas DataFrame with sorted statistics
    """
    df = pd.DataFrame(
        list(distribution.items()),
        columns=['Name', 'Times Selected']
    ).sort_values('Times Selected', ascending=False)
    
    return df
