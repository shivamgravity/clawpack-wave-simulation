# 🌊 Interactive Wave Propagation Simulator using Clawpack

An interactive scientific simulation that models **wave propagation in shallow water** using numerical PDE solvers from **Clawpack**.

The project visualizes how disturbances in water propagate over time and allows users to interactively control simulation parameters through a **Streamlit web interface**.

---

# 📌 Project Overview

This project simulates **wave dynamics using the shallow water equations**, which are widely used in computational fluid dynamics and geophysical modeling.

A disturbance is introduced in the water surface, and the simulation computes how the waves propagate outward using **finite volume methods** implemented in **Clawpack**.

Users can interactively modify simulation parameters and visualize the resulting wave patterns in real time.

---

# 🚀 Key Features

- Numerical simulation using **Clawpack PDE solvers**
- Interactive simulation controls via **Streamlit**
- 3D visualization of water surface
- Adjustable simulation parameters:
  - Grid resolution
  - Disturbance strength
  - Simulation time
- Animated wave propagation
- Scientific computing workflow using **Linux + Conda**

---

# 🧠 Scientific Background

The simulation uses the **Shallow Water Equations (SWE)**:

* ∂h/∂t + ∇·(hu) = 0
* ∂(hu)/∂t + ∇·(hu² + ½gh²) = 0


Where:

| Symbol | Meaning |
|------|--------|
| h | Water height |
| u | Water velocity |
| g | Gravitational acceleration |

These equations describe **fluid flow where horizontal scales are much larger than vertical scales**.

They are commonly used in:

- Tsunami simulation
- Ocean modeling
- Flood modeling
- Atmospheric modeling
- Hydrodynamics research

---

# 🏗 System Architecture

            User Interface
                 │
                 │
         ┌───────▼────────┐
         │   Streamlit UI │
         │  Parameter UI  │
         └───────┬────────┘
                 │
                 │ user inputs
                 ▼
         ┌─────────────────┐
         │ Simulation Core │
         │   (Clawpack)    │
         │  PDE Solver     │
         └───────┬─────────┘
                 │
                 │ simulation frames
                 ▼
       ┌─────────────────────┐
       │ Visualization Layer │
       │  Matplotlib (3D)    │
       └─────────┬───────────┘
                 │
                 ▼
          Animated Wave Surface


---

# ⚙️ Simulation Workflow

User sets simulation parameters
│
▼
Initialize shallow water domain
│
▼
Apply disturbance to water surface
│
▼
Clawpack solves PDE system
│
▼
Generate simulation frames
│
▼
Render 3D wave surface
│
▼
Display animated result in Streamlit


---

# 🛠 Tech Stack

| Technology | Purpose |
|-----------|--------|
| Python | Programming language |
| Clawpack | Numerical PDE solver |
| NumPy | Numerical computation |
| Matplotlib | Scientific visualization |
| Streamlit | Interactive web interface |
| Conda | Environment management |
| WSL + Ubuntu | Linux environment for scientific libraries |

---

# 📂 Project Structure

```text
ClawPack-Wave-Simulation
│
├── wave_simulation.py
│ Standalone simulation script
│
├── streamlit_app.py
│ Interactive Streamlit simulation app
│
├── README.md
│ Project documentation
│
└── requirements.txt
│
└── requirements.txt
```

---

# ⚙️ Installation

## 1️⃣ Install WSL (Linux Environment)

```bash
wsl --install -d Ubuntu
```

---

## 2️⃣ Install Miniconda

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
Miniconda3-latest-Linux-x86_64.sh
```

Restart the terminal afterwards.

---

## 3️⃣ Create Environment

```bash
conda create -n clawpack_env python=3.10
```

---

## 4️⃣ Install Dependencies

```bash
conda install -c conda-forge clawpack
pip install numpy matplotlib streamlit
```

---

# ▶️ Running the Simulation

Navigate to the project directory:

```bash
cd "/mnt/e/Projects/ClawPack - Wave Simulation"
```
**Note:** *Make sure to customize the project directory path according to yours.*

Activate the environment:

```bash
conda activate clawpack_env
```

Run the interactive app:

```bash
streamlit run streamlit_app.py
```

Open the browser at:

```bash
http://localhost:8501
```

---

# 🎮 Using the Interactive Simulator

Users can control the following parameters:

| Parameter | Description |
|--------|-------------|
| Grid Resolution | Controls simulation accuracy |
| Disturbance Strength | Initial wave amplitude |
| Simulation Time | Duration of simulation |

Press **Run Simulation** to visualize the wave propagation.

---

# 📊 Example Simulation

Example visualization produced by the simulator:

![Demo Simulation](/demo_simulation/demo.gif)


The disturbance creates circular waves that propagate outward across the water surface.

---

# 🔬 Applications

Wave simulations like this are used in:

- Tsunami prediction models
- Ocean wave forecasting
- Hydrodynamic research
- Climate and atmospheric simulations
- Computational fluid dynamics

---

# 📈 Possible Future Improvements

This project can be extended with:

- Multiple disturbance points
- Wave interference patterns
- Real-time GPU acceleration
- Coastal boundary modeling
- Tsunami simulation scenarios
- Web deployment

---

# 👨‍💻 Author

Shivam  
Computer Science Student

Project developed as part of exploring **scientific computing, numerical simulations, and interactive visualization**.

---

# 📚 References

Clawpack Documentation  
https://www.clawpack.org

Streamlit Documentation  
https://docs.streamlit.io

Numerical Methods for Hyperbolic PDEs
