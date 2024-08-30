# Simulations Project

This project is designed to simulate interactions between various types of objects within a 2D environment. The simulation is implemented in Python and uses the PyGame library to visualize the interactions. The simulation's parameters and behavior can be customized through the configuration file.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Modules Overview](#modules-overview)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this simulation, you need Python 3.x installed on your system. It is recommended to use a virtual environment to manage dependencies.

### Steps to Install

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/guloff/simulations.git
   cd simulations
   ```

2. **Create a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

After installation, you can start the simulation by running the `main.py` file.

```bash
python main.py
```

The simulation will open a new window where you can observe the interactions between objects. You can modify the behavior of the simulation by adjusting the parameters in the `config.py` file.

## Configuration

The simulation's behavior can be customized via the `config.py` file. This file includes settings such as screen dimensions, object properties, and energy levels.

### Example Configuration:

```python
# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

# Object properties
OBJECT_RADIUS = 7
INITIAL_ENERGY = 100

# Simulation timing
TIME_INTERVAL = 100  # milliseconds
```

Adjust these values to experiment with different simulation scenarios.

## Modules Overview

- **`main.py`:** The main entry point of the simulation, handling initialization and the game loop.
- **`config.py`:** Contains all configuration settings for the simulation.
- **`sim_object.py`:** Defines the `SimObject` class, representing the entities in the simulation.
- **`statistics.py`:** Handles the collection and processing of simulation data.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   
   ```bash
   git checkout -b feature-branch
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Add new feature"
   ```

4. Push to your branch:

   ```bash
   git push origin feature-branch
   ```

5. Open a pull request on GitHub.

## License

This project is licensed under the MIT License.
