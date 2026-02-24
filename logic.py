"""
Core business logic for the PickName application.
Handles name selection, history tracking, and statistics.
"""

import random
from collections import Counter
from typing import List, Dict, Tuple


class NameSelector:
    """Manages name selection and history tracking."""
    
    def __init__(self, names: List[str] = None):
        """
        Initialize the NameSelector.
        
        Args:
            names: Initial list of names
        """
        self.names = names or []
        self.selection_history = []
    
    def add_name(self, name: str) -> bool:
        """
        Add a name to the list.
        
        Args:
            name: Name to add
            
        Returns:
            True if added, False if already exists
        """
        if name and name not in self.names:
            self.names.append(name)
            return True
        return False
    
    def remove_name(self, name: str) -> bool:
        """
        Remove a name from the list.
        
        Args:
            name: Name to remove
            
        Returns:
            True if removed, False if not found
        """
        if name in self.names:
            self.names.remove(name)
            return True
        return False
    
    def add_names_batch(self, names: List[str]) -> int:
        """
        Add multiple names at once, removing duplicates.
        
        Args:
            names: List of names to add
            
        Returns:
            Number of unique names added
        """
        initial_count = len(self.names)
        # Remove duplicates from input
        new_names = list(set(names))
        self.names = list(set(self.names + new_names))
        return len(self.names) - initial_count
    
    def clear_names(self) -> None:
        """Clear all names from the list."""
        self.names = []
    
    def clear_history(self) -> None:
        """Clear the selection history."""
        self.selection_history = []
    
    def reset(self) -> None:
        """Reset both names and history."""
        self.clear_names()
        self.clear_history()
    
    def pick_random(self) -> str:
        """
        Pick a random name from the list.
        
        Returns:
            The selected name
            
        Raises:
            ValueError: If no names in the list
        """
        if not self.names:
            raise ValueError("No names available to pick from")
        
        selected = random.choice(self.names)
        self.selection_history.append(selected)
        return selected
    
    def get_statistics(self) -> Dict:
        """
        Get selection statistics.
        
        Returns:
            Dictionary with statistics
        """
        if not self.selection_history:
            return {
                "total_picks": 0,
                "unique_names": len(self.names),
                "most_selected": None,
                "most_selected_count": 0,
                "average_picks": 0.0,
                "distribution": {}
            }
        
        counter = Counter(self.selection_history)
        most_selected_name, most_selected_count = counter.most_common(1)[0]
        
        return {
            "total_picks": len(self.selection_history),
            "unique_names": len(self.names),
            "most_selected": most_selected_name,
            "most_selected_count": most_selected_count,
            "average_picks": len(self.selection_history) / len(self.names) if self.names else 0,
            "distribution": dict(counter)
        }
    
    def get_distribution_data(self) -> Tuple[List[str], List[int]]:
        """
        Get distribution data for visualization.
        
        Returns:
            Tuple of (names, counts)
        """
        counter = Counter(self.selection_history)
        if not counter:
            return [], []
        
        # Sort by count descending
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        names, counts = zip(*sorted_items)
        return list(names), list(counts)
    
    def get_selection_count(self, name: str) -> int:
        """
        Get how many times a specific name was selected.
        
        Args:
            name: Name to check
            
        Returns:
            Number of times selected
        """
        return self.selection_history.count(name)
    
    def has_names(self) -> bool:
        """Check if there are names in the list."""
        return len(self.names) > 0
    
    def has_history(self) -> bool:
        """Check if there is selection history."""
        return len(self.selection_history) > 0
