# Basketball Offensive Passing Optimization using DFS 🏀

This repository contains the Python simulation code for the paper: **"Algorithmic Pathfinding and Directed Graphs for Optimizing Offensive Passing Sequences in Basketball Strategy"**.

**Author:** Muhammad Adnan Kurniawan (13525071)  
**Course:** IF1220 Matematika Diskrit  
**Institution:** Institut Teknologi Bandung (ITB)

## 📌 Project Overview
Modern basketball heavily relies on strategic passing to dismantle elite defensive formations. This project models an offensive basketball possession as a mathematical graph. By applying combinatorial principles and utilizing a depth-limited **Depth-First Search (DFS)** algorithm, the program calculates and identifies the optimal sequence of passes that yields the highest probability of a successful shot.

## ⚙️ Features
- **Directed Weighted Graph Modeling:** Represents players as nodes and pass success probabilities as edge weights.
- **DFS Traversal:** Exhaustively searches for valid passing routes.
- **Algorithmic Constraints:** Hardcoded maximum depth of 4 passes to mathematically simulate the 24-second NBA shot clock.
- **Dynamic Scenarios:** Includes a baseline scenario and an adaptive scenario against elite interior defenses.

## 🚀 How to Run
1. Ensure you have Python 3.x installed.
2. Clone this repository or download the `.py` files.
3. Run the scripts via terminal or command prompt.

**For Scenario 1 (Baseline Offense):**
```bash
python src/simulasi_basket.py
```
**For Scenario 2 (Elite Interior Defense):**
```bash
python src/imulasi_basket2.py
```
The terminal will output the optimal passing route and its cumulative success probability for each scenario.
