import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[-1, 12], y=[0, 0], mode='markers', marker_size=20,
))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False,
                 zeroline=True, zerolinecolor='black', zerolinewidth=3,
                 showticklabels=False)
fig.update_layout(height=200, plot_bgcolor='white')
fig.show()
