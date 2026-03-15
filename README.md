# 🌀 Bermuda Triangle Optimizer (BTO) Implementation

A physics-based metaheuristic optimization algorithm inspired by the mysterious gravitational forces of the Bermuda Triangle. This project was developed for the **Optimization** course at Sivas Cumhuriyet University (January 2026).

> **⭐ Achievement:** This project was awarded a **100/100 grade**, achieving the highest performance in the class.

## 📌 About the Algorithm

Bermuda Triangle Optimizer (BTO) is a novel metaheuristic method proposed by **H. A. Shehadeh (2025)**. It models the search agents (ships/planes) being pulled toward the global optimum (the center of the triangle) based on gravitational metaphors.

### ⚙️ How It Works
The algorithm balances two main phases:
* **Exploitation (Inside the Triangle):** When agents are close to the best solution, they are pulled strongly toward the center using the **Subtraction (-)** operator.
* **Exploration (Outside the Triangle):** To avoid local optima, agents explore wider areas using the **Addition (+)** operator.

The model is enhanced with **Chaos Theory (Chebyshev/Sinusoidal maps)** and **Levy Flight** to ensure global search efficiency and prevent stagnation.

## 📂 Repository Content

* [BTO_Algorithm.py](./BTO_Python_Algorithm.py): Full implementation of the algorithm in Python.
* [BTO_Report.pdf](./BTO_Report.pdf): Detailed academic paper including mathematical models and literature review.
* [BTO_Presentation.pdf](./BTO_Presentation.pdf): A comprehensive slide deck explaining the theory and results.
* [BTO_Sample_Solution.pdf](./BTO_Sample_Solution.pdf): Step-by-step manual calculation of a sample optimization problem.

## 📊 Performance Analysis
In benchmark tests (CEC 2017 functions), BTO demonstrated superior convergence speed compared to:
1.  **GSA** (Gravitational Search Algorithm)
2.  **CDO** (Chernobyl Disaster Optimizer)

The Python implementation successfully reaches the global optimum ($f(x) \approx 0$) for the Sphere function within 100 iterations.

## 🛠️ Mathematical Model
The position update rule is governed by:
$$X_{i,j}(t+1) = X_{best,j} \pm (Acc \times rand \times PoF \times (UB_j - LB_j) \times Zone_{BF})$$

## 👩‍💻 Developer
**Hatice Kübra ÜNAL**
*Computer Engineering Student at Sivas Cumhuriyet University*
