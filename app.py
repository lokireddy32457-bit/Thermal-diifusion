import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="PDE Thermal Solver", layout="wide")
st.title("🔥 2D Heat Equation: Interactive Simulation")

# --- Sidebar Controls ---
st.sidebar.header("Simulation Parameters")
alpha = st.sidebar.slider("Thermal Diffusivity (α)", 0.1, 5.0, 2.0)
steps = st.sidebar.slider("Time Iterations", 10, 1000, 200)
grid_size = 50

# --- Mathematical Engine ---
u = np.zeros((grid_size, grid_size))
u[20:30, 20:30] = 100  # Initial Heat Source

dt = 0.05
dx = 1.0

# Numerical Integration
for _ in range(steps):
    u_next = u.copy()
    # Finite Difference Method
    u_next[1:-1, 1:-1] = u[1:-1, 1:-1] + alpha * dt * (
        (u[2:, 1:-1] + u[:-2, 1:-1] + u[1:-1, 2:] + u[1:-1, :-2] - 4*u[1:-1, 1:-1]) / dx**2
    )
    u = u_next

# --- 3D Interactive Visualization ---
x = np.linspace(0, grid_size, grid_size)
y = np.linspace(0, grid_size, grid_size)
X, Y = np.meshgrid(x, y)

fig = go.Figure(data=[go.Surface(z=u, colorscale='Hot')])
fig.update_layout(
    title=f'Temperature Distribution after {steps} steps',
    scene=dict(zaxis=dict(range=[0, 100], title='Temp (°C)')),
    width=800, height=800
)

st.plotly_chart(fig, use_container_width=True)
st.write("This interactive plot allows you to rotate and zoom into the thermal gradient.")
