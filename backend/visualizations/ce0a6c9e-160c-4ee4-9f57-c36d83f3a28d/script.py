import plotly.graph_objects as go
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='sin(x)'))
fig.update_layout(
    title='Interactive Sine Wave',
    xaxis_title='X',
    yaxis_title='sin(X)',
    template='plotly_white'
)