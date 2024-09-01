# Importing necessary libraries
import numpy as np
import plotly.graph_objects as go

# Implementing of F(X) function
def F(X):
    # X[0]: x1 , X[1]: x2
    return -np.cos(X[0])*np.cos(X[1])*np.exp(-np.power((X[0]-np.pi),2)-np.power((X[1]-np.pi),2))

# Creating 2D-meshgrid space for x1 and x2 dimensions 
start, stop, n_values = -20, 20, 100
x1 = np.linspace(start, stop, n_values)
x2 = np.linspace(start, stop, n_values)
X1, X2 = np.meshgrid(x1, x2)  

# Calculating the value of F(X) function for 2D-meshgrid space as Y
Y = F([X1, X2])

# Drawing contour levels on 3D-Surface
fig = go.Figure(
    go.Surface(
        contours = {
            "z": {"show": True, "start": np.amin(Y), "end": np.amax(Y) , "size": 0.1, "color":"white"}
        },
        x = X1,
        y = X2,
        z = Y    
    )
)

# Other settings on plot
fig.update_layout(
    scene = {
        "xaxis_title": {"text":"x1"},
        "yaxis_title": {"text":"x2"},
        "zaxis_title": {"text":"F(X)"},
        "camera_eye": {"x": 0, "y": -1, "z": 0.5},
        "aspectratio": {"x": 1, "y": 1, "z": 0.2}
    }
)

# HTML View Save
fig.write_html('results/4_(3D_Plot).html', auto_open=True)