"""
Reusable plotting utilities for Netflix-style charts.
"""

import matplotlib.pyplot as plt
from config import COLORS


def netflix_barh(labels, values, title):
    """
    Draw a horizontal bar chart using Netflix-style colors.
    """
    plt.figure(figsize=(14, 7))
    plt.style.use('dark_background')

    plt.barh(labels, values, color=COLORS['netflix_red'])
    plt.gca().invert_yaxis()

    plt.title(title, fontsize=18, fontweight='bold', color='white', pad=20)
    plt.xlabel("Frequency", fontsize=12, color='white')
    plt.ylabel("Label", fontsize=12, color='white')

    plt.xticks(color='white')
    plt.yticks(color='white')

    plt.gca().set_facecolor(COLORS['background'])
    plt.gcf().patch.set_facecolor(COLORS['background'])

    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
    plt.tight_layout()
    plt.show()

