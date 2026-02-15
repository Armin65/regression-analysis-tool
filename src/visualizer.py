import plotly.graph_objects as go
import numpy as np
import pandas as pd

class Visualizer:
    def __init__(self, actual, predicted):
        self.actual = actual
        self.predicted = predicted
        self.residuals = self.actual - self.predicted

    def plot(self):
        # Create subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=("Regression Fit", "Residuals", "Distribution", "Actual vs Predicted"),
            specs=[[{}, {}], [{}, {}]]
        )

        # Regression Fit
        fig.add_trace(
            go.Scatter(x=self.actual, y=self.predicted, mode='markers', name='Predicted'),
            row=1, col=1
        )
        fig.add_trace(
            go.Scatter(x=self.actual, y=self.actual, mode='lines', name='Fit Line', line=dict(color='red')),
            row=1, col=1
        )

        # Residuals
        fig.add_trace(
            go.Scatter(x=self.actual, y=self.residuals, mode='markers', name='Residuals'),
            row=1, col=2
        )
        fig.add_hline(y=0, line_color='red', line_dash='dash', row=1, col=2)

        # Distribution
        fig.add_trace(
            go.Histogram(x=self.residuals, name='Distribution', nbinsx=30),
            row=2, col=1
        )

        # Actual vs Predicted
        fig.add_trace(
            go.Scatter(x=self.actual, y=self.predicted, mode='markers', name='Actual vs Predicted'),
            row=2, col=2
        )
        fig.add_trace(
            go.Scatter(x=self.actual, y=self.actual, mode='lines', name='Line', line=dict(color='red')),
            row=2, col=2
        )

        # Update layout
        fig.update_layout(
            title_text='Interactive Visualizations',
            height=800,
            width=800
        )

        # Show the figures
        fig.show()