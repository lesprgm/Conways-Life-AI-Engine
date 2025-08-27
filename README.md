# Conway's Game of Life: AI Pattern Optimization Engine (Genetic Algorithm)

[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![NumPy](https://img.shields.io/badge/numpy-2.2.6-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/matplotlib-3.10.3-green.svg)](https://matplotlib.org/)

## Table of Contents

- [Project Overview](#project-overview)
- [Demo](#demo)
- [Fitness Plot](#fitness-plot)
- [Core Features](#core-features)
- [Technical Details](#technical-details)
- [Genetic Algorithm Objective & Parameters](#genetic-algorithm-objective--parameters)
- [Installation & Setup](#installation--setup-docker-focused)
- [Usage](#usage)
- [Output Interpretation](#output-interpretation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Author](#author)

## Project Overview

This project implements a sophisticated intersection of **cellular automata** and **artificial intelligence**: a Genetic Algorithm (GA) designed to evolve stable and long-lived patterns for Conway's Game of Life. 

**What it does:**
- Uses evolutionary computation to discover patterns that survive as long as possible in Conway's Game of Life
- Employs advanced fitness evaluation that detects not just death, but also premature oscillations and stagnation
- Provides comprehensive visualization of both the evolutionary process and the resulting patterns
- Containerized with Docker for consistent execution across different environments

**Why it matters:**
Conway's Game of Life, despite its simple rules, exhibits complex emergent behavior. Finding patterns that survive for extended periods is computationally challenging and provides insights into pattern formation, stability, and evolution in complex systems.

## Demo

<p align="center">
  <img src="media/demo.gif" alt="GUI Demo">
</p>

## Fitness Plot

This graph illustrates the Genetic Algorithm's evolutionary progress over **2000 generations**. With a population size of **300** and a mutation rate of **0.03**, the "Best Fitness" steadily increased in distinct steps, reflecting the GA's ability to discover fitter patterns. The fitness ultimately plateaued around **1063**, indicating the best pattern found survived for over half of the maximum possible **2000 simulation steps**.

<p align="center">
    <img src="media/fitness.png" width="600"/>
    <br>
    <i>Best fitness score over 2000 generations</i>
</p>

---
 
## Core Features

### Game of Life Engine
- **High-Performance Simulation**: NumPy-based implementation optimized for speed and memory efficiency
- **Configurable Board Size**: Customizable grid dimensions (default: 20x20)
- **Accurate Rule Implementation**: Faithful reproduction of Conway's original rules

### Genetic Algorithm Components
- **Population Management**: Initializes and evolves populations of Game of Life patterns
- **Tournament Selection**: Selects fitter parents through competitive selection process
- **Uniform Crossover**: Combines genetic material from parents with configurable crossover rate
- **Adaptive Mutation**: Introduces random changes to maintain genetic diversity
- **Enhanced Fitness Evaluation**: 
  - Detects pattern death (all cells become inactive)
  - Identifies oscillation cycles (patterns that repeat)
  - Rewards longevity while penalizing early stagnation
- **Elitism Strategy**: Preserves the best individual from each generation

### Visualization & Analysis
- **Real-time Progress Tracking**: Live console output showing generation progress
- **Fitness Plotting**: Matplotlib-generated graphs showing evolutionary progress
- **Pattern Visualization**: Pygame-based display of evolved patterns in action
- **Comprehensive Data Export**: Multiple file formats for further analysis

### Infrastructure
- **Docker Containerization**: Ensures consistent runtime environment across platforms
- **Data Persistence**: Host-mapped volumes for result preservation
- **Flexible Configuration**: Easy parameter tuning through configuration files

## Technical Details

### Conway's Game of Life Rules
The Game of Life follows these simple rules that create complex emergent behavior:

1. **Birth**: A dead cell with exactly 3 live neighbors becomes alive
2. **Survival**: A live cell with 2 or 3 live neighbors stays alive
3. **Death**: A live cell with fewer than 2 neighbors dies (underpopulation)
4. **Death**: A live cell with more than 3 neighbors dies (overpopulation)

### Genetic Algorithm Implementation

#### Fitness Function
The fitness function evaluates pattern longevity with sophisticated detection mechanisms:

```python
# Simplified fitness calculation logic
def calculate_fitness(pattern, max_steps):
    current_board = pattern.copy()
    seen_states = set()
    
    for step in range(max_steps):
        # Convert board to hashable format for cycle detection
        board_hash = hash(current_board.tobytes())
        
        if board_hash in seen_states:
            # Pattern entered a cycle - return current step
            return step
        
        seen_states.add(board_hash)
        next_board = apply_game_of_life_rules(current_board)
        
        if np.array_equal(next_board, current_board):
            # Pattern is static (still life)
            return step
        
        if not next_board.any():
            # Pattern died completely
            return step
            
        current_board = next_board
    
    return max_steps  # Pattern survived all steps
```

#### Selection Strategy
- **Tournament Selection**: Randomly selects a subset of individuals and chooses the fittest
- **Tournament Size**: Configurable (default: 5) - larger values increase selection pressure
- **Diversity Preservation**: Prevents premature convergence while maintaining evolutionary pressure

#### Crossover Method
- **Uniform Crossover**: Each cell has a 50% chance of coming from either parent
- **Genetic Diversity**: Creates novel combinations while preserving successful patterns
- **Crossover Rate**: Configurable probability (default: 0.8) that crossover occurs

#### Mutation Process
- **Bit-flip Mutation**: Each cell has a small probability of flipping state (alive ↔ dead)
- **Mutation Rate**: Low probability (default: 0.03) to maintain pattern integrity
- **Exploration vs. Exploitation**: Balances discovering new patterns with refining existing ones

## Genetic Algorithm Objective & Parameters

### Primary Objective
The GA seeks to discover initial Game of Life patterns that **maximize survival time** while avoiding:
- **Early Death**: Patterns that quickly die out completely
- **Premature Oscillation**: Patterns that enter short cycles too early
- **Stagnation**: Patterns that become static (still lifes) without sufficient evolution

### Configuration Parameters

All parameters are defined in `ga_parameters.py` and can be modified before building the Docker image:

| Parameter | Default Value | Description | Impact |
|-----------|---------------|-------------|---------|
| `ga_population_size` | 200 | Number of patterns in each generation | Larger = more diversity, slower execution |
| `ga_num_generations` | 10 | Maximum generations to evolve | More = better solutions, longer runtime |
| `ga_mutation_rate` | 0.03 | Probability of cell mutation (3%) | Higher = more exploration, less stability |
| `ga_simulation_steps` | 2000 | Max steps to evaluate each pattern | Longer = finds truly stable patterns |
| `ga_board_width` | 20 | Grid width in cells | Larger = more complex patterns possible |
| `ga_board_height` | 20 | Grid height in cells | Larger = more complex patterns possible |
| `ga_fitness_threshold` | 2001 | Stop if fitness reaches this value | Early stopping for perfect solutions |
| `ga_crossover_rate` | 0.8 | Probability of crossover (80%) | Higher = more genetic mixing |
| `ga_tournament_size` | 5 | Number of candidates in selection | Larger = stronger selection pressure |

### Example Configurations

**Quick Testing** (faster execution):
```python
ga_population_size = 50
ga_num_generations = 100
ga_simulation_steps = 500
```

**Deep Search** (better results):
```python
ga_population_size = 500
ga_num_generations = 2000
ga_simulation_steps = 5000
```

**High Mutation Exploration**:
```python
ga_mutation_rate = 0.1  # 10% mutation rate
ga_crossover_rate = 0.6  # Lower crossover for more mutation impact
```

### Parameter Tuning Tips
- **Start Small**: Use smaller values for initial testing and parameter exploration
- **Balance Trade-offs**: Population size vs. generation count vs. simulation steps
- **Monitor Results**: Watch fitness plots to understand if parameters need adjustment
- **Computational Cost**: Remember that total evaluations = population_size × num_generations × simulation_steps

## Installation & Setup (Docker-Focused)

### Prerequisites

- **Docker Desktop** (Windows/macOS) or **Docker Engine** (Linux)
- **Git** installed
- **8GB+ RAM** recommended for larger populations
- **2GB+ disk space** for Docker image and results

### Quick Start

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lesprgm/Conways-Life-AI-Engine.git
   cd Conways-Life-AI-Engine
   ```

2. **Create Host Results Directory**:
   ```bash
   mkdir ga_results_host
   ```

3. **Build Docker Image**:
   ```bash
   docker build --no-cache -t game-of-life-ga .
   ```

### Alternative: Local Python Setup

If you prefer running without Docker:

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Create Results Directory**:
   ```bash
   mkdir ga_results
   ```

3. **Run Directly**:
   ```bash
   python main.py
   ```

### Customizing Parameters

Before building the Docker image, you can modify parameters in `ga_parameters.py`:

```python
# Example modifications
ga_population_size = 100      # Smaller for faster testing
ga_num_generations = 500      # Moderate evolution time
ga_mutation_rate = 0.05       # Slightly higher exploration
```

After changes, rebuild the Docker image:
```bash
docker build --no-cache -t game-of-life-ga .
```

## Usage

### Running with Docker (Recommended)

#### Standard Execution
For macOS/Linux:
```bash
docker run -it --rm -v $(pwd)/ga_results_host:/app/ga_results game-of-life-ga
```

For Windows (PowerShell):
```powershell
docker run -it --rm -v ${PWD}/ga_results_host:/app/ga_results game-of-life-ga
```

For Windows (Command Prompt):
```cmd
docker run -it --rm -v %cd%/ga_results_host:/app/ga_results game-of-life-ga
```

#### Background Execution
To run in the background and save logs:
```bash
docker run -d --name gol-ga -v $(pwd)/ga_results_host:/app/ga_results game-of-life-ga > evolution.log 2>&1
```

Check progress:
```bash
docker logs -f gol-ga
```

#### Interactive Mode
For development or debugging:
```bash
docker run -it --rm -v $(pwd)/ga_results_host:/app/ga_results --entrypoint /bin/bash game-of-life-ga
```

### Running Locally

If you installed dependencies locally:
```bash
python main.py
```

### Expected Runtime

Execution time varies significantly based on parameters:

| Configuration | Population | Generations | Approx. Time |
|---------------|------------|-------------|--------------|
| Quick Test | 50 | 100 | 5-10 minutes |
| Standard | 200 | 1000 | 1-2 hours |
| Deep Search | 500 | 2000 | 8-12 hours |

### Monitoring Progress

The application provides real-time feedback:

```
Generation 1/1000
Generation 2/1000  
Best fitness improved: 45 -> 67
Generation 3/1000
...
Generation 234/1000
Best fitness improved: 67 -> 128
...
```

## Output Interpretation

### Console Output
- **Generation Progress**: Shows current generation number and total
- **Fitness Updates**: Reports when a better pattern is discovered
- **Final Summary**: Best fitness achieved and total generations completed

### Generated Files

The application creates three types of output files in `ga_results_host/`:

#### 1. Pattern Files (`.txt`)
**Format**: `evolved_pattern_YYYYMMDD-HHMMSS.txt`
```
1 0 1 0 0 0 0 0 1 1 0 0 0 0 1 0 0 0 0 0
0 1 0 1 0 1 1 0 0 0 1 1 1 0 0 0 1 1 0 0
1 1 0 0 0 0 1 0 0 0 0 0 1 1 1 1 1 1 1 1
```
- **Content**: The best evolved pattern as a space-separated grid
- **Usage**: Can be loaded and visualized in other Game of Life simulators
- **Format**: 1 = alive cell, 0 = dead cell

#### 2. NumPy Arrays (`.npy`)
**Format**: `evolved_pattern_YYYYMMDD-HHMMSS.npy`
- **Content**: Binary format of the pattern for Python analysis
- **Usage**: Load with `numpy.load()` for programmatic analysis
- **Advantage**: Preserves exact data types and array structure

#### 3. Fitness History (`.csv`)
**Format**: `fitness_history_YYYYMMDD-HHMMSS.csv`
```
Generation,Fitness
1,23
2,23
3,45
4,45
5,67
```
- **Content**: Best fitness score for each generation
- **Usage**: Create custom plots, analyze convergence patterns
- **Applications**: Parameter tuning, performance analysis

### Interpreting Fitness Scores

| Fitness Range | Interpretation | Pattern Behavior |
|---------------|----------------|-------------------|
| 0-50 | Poor survival | Dies quickly or becomes static early |
| 51-200 | Moderate success | Short-lived activity before stabilizing |
| 201-500 | Good patterns | Sustained activity with eventual cycles |
| 501-1000 | Excellent patterns | Long-lived with complex evolution |
| 1000+ | Outstanding | Near-maximum survival or gliders |

**Note**: Maximum possible fitness equals `ga_simulation_steps` (default: 2000)

### Visual Analysis

After evolution completes, the application displays:
1. **Fitness Plot**: Shows evolutionary progress over generations
2. **Pattern Animation**: Live visualization of the best evolved pattern
3. **Final State**: The pattern's behavior after evolution

## Troubleshooting

### Common Issues

#### Docker Problems

**Issue**: "Docker command not found"
```bash
# Install Docker first
# Windows/macOS: Download Docker Desktop
# Linux: sudo apt-get install docker.io
```

**Issue**: Permission denied errors on Linux
```bash
sudo usermod -aG docker $USER
# Log out and back in, or restart terminal
```

**Issue**: "No space left on device"
```bash
# Clean up Docker
docker system prune -a
```

#### Performance Issues

**Issue**: Very slow execution
- **Solution**: Reduce `ga_population_size` or `ga_simulation_steps`
- **Alternative**: Use fewer generations for initial testing

**Issue**: Memory errors
- **Solution**: Reduce `ga_population_size` or `ga_board_width/height`
- **Check**: Available RAM (recommend 8GB+ for large populations)

#### Output Issues

**Issue**: No files in `ga_results_host/`
- **Check**: Directory exists and has write permissions
- **Verify**: Docker volume mounting syntax for your OS
- **Solution**: Create directory manually: `mkdir ga_results_host`

**Issue**: "Permission denied" when accessing results
```bash
# Fix permissions (Linux/macOS)
sudo chown -R $USER:$USER ga_results_host/
```

#### Pattern Issues

**Issue**: All patterns die quickly (low fitness)
- **Increase**: `ga_simulation_steps` to allow more evolution time
- **Increase**: `ga_population_size` for more diversity
- **Adjust**: `ga_mutation_rate` to balance exploration vs. exploitation

**Issue**: Fitness not improving over generations
- **Increase**: `ga_mutation_rate` for more exploration
- **Decrease**: `ga_tournament_size` to reduce selection pressure
- **Check**: If fitness threshold is too low

### Getting Help

1. **Check Parameters**: Verify `ga_parameters.py` values are reasonable
2. **Review Logs**: Examine console output for error messages
3. **Test Smaller**: Try reduced parameters for faster debugging
4. **Dependencies**: Ensure all requirements are installed correctly

## Contributing

We welcome contributions! Here's how you can help:

### Types of Contributions
- **Bug Reports**: Found an issue? Please report it!
- **Feature Requests**: Ideas for improvements or new features
- **Code Contributions**: Bug fixes, optimizations, or new features
- **Documentation**: Improvements to README, code comments, or examples

### Development Setup
1. Fork the repository
2. Clone your fork locally
3. Install dependencies: `pip install -r requirements.txt`
4. Make your changes
5. Test thoroughly
6. Submit a pull request

### Code Style
- Follow PEP 8 Python style guidelines
- Add comments for complex algorithms
- Include docstrings for new functions
- Update tests if modifying core functionality

### Testing
Run the test suite before submitting:
```bash
python tests/2gof_test.py
python tests/test_ga_population.py
python tests/test_ga_functions.py
```



---

## Author

**Leslie Osei-Anane** - *Initial work and development*

This project was created as an exploration of genetic algorithms applied to cellular automata, specifically Conway's Game of Life. It demonstrates the power of evolutionary computation in discovering complex, emergent patterns from simple rules.

### Connect
- GitHub: [@lesprgm](https://github.com/lesprgm)
- Project Link: [Conway's Life AI Engine](https://github.com/lesprgm/Conways-Life-AI-Engine)

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
- John Conway for creating the Game of Life
- The scientific community for advancing genetic algorithm research
- Open source contributors who made the dependencies possible
