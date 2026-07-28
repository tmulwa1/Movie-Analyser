import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from src.stats import genre_breakdown, ratings_over_time

def create_genre_chart():
    # Creating the chart folder
    os.makedirs('static/charts', exist_ok=True)
    data = genre_breakdown()
    data.plot.bar(title="Genre Breakdown")
    # Rotates the labels to make them more readable
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/charts/genre_breakdown.png')
    plt.close()

def create_ratings_chart():
    data = ratings_over_time()
    data.plot(kind='line')
    plt.tight_layout()
    plt.savefig('static/charts/ratings.png')
    plt.close()