# Flappy Bird Game with NEAT AI
Welcome to the Flappy Bird game made using Pygame and NEAT (NeuroEvolution of Augmenting Topologies)! This project combines classic gameplay with artificial intelligence to create an engaging gaming experience. In this game, you can play as the flappy bird yourself or watch an AI take control and attempt to navigate through the obstacles.

## Installation
1. Ensure you have Python installed on your system (Python 3.6 or higher).
2. Clone this repository to your local machine using the following command:

        git clone https://github.com/Siddharth-2382/Flappy-Bird-AI.git
3. Navigate to the project directory:

        cd Flappy-Bird-AI
4. Install the required dependencies. It is recommended to set up a virtual environment before installing the dependencies:

        pip install -r requirements.txt

## Game Controls
1. To play the game manually, run the `main.py` script:

        python main.py
    Press the `Spacebar` to make the bird flap and navigate through the pipes.
2. To watch the AI play the game, run the `AI_mode.py` script:

        python AI_mode.py
    The AI will use the pre-trained neural network stored in `winner_genome.pkl` to play the game automatically.

## Training the AI
If you are interested in training your own AI to play the Flappy Bird game, you can use the `training.py` script. The NEAT algorithm will be applied to evolve a neural network capable of playing the game.

Here's how to run the training:
1. Run the `training.py` script:

        python training.py
2. The training process will start, and you will see each generation's progress being printed to the console. The script will keep training until a bird successfully reaches a score of 100 or more.
3. Once a successful bird is found, the winning neural network's genome will be saved as `winner_genome.pkl`. This file contains the genetic information of the neural network that achieved the highest score during the training process.
4. You can then use this winner_genome.pkl file to observe the AI playing the game automatically by running the `AI_mode.py` script.

Feel free to modify the parameters and settings in `config-feedforward.txt` to experiment with the training process. You can adjust parameters like population size, mutation rate, and others to see how they impact the AI's learning.

## Project Structure
The project directory contains the following files:
- `Bird.py`: This file contains the implementation of the Bird class, representing the player-controlled bird in the game.
- `Base.py`: The Base class is defined in this file, representing the moving base/ground in the game.
- `Pipe.py`: This file contains the Pipe class, representing the pipes that the bird needs to navigate through.
- `main.py`: The main entry point of the game. Run this script to play the game manually.
- `training.py`: The script that runs the NEAT algorithm to train a neural network to play the game. The training goes through multiple generations until a bird achieves a score of 100 or more. The winning genome is then saved as `winner_genome.pkl`.
- `AI_mode.py`: This script uses the `winner_genome.pkl` to showcase the AI playing the game automatically.
- `config-feedforward.txt`: The configuration file used by the NEAT algorithm for training. It contains parameters such as population size, mutation rates, and other genetic algorithm-related settings.
- `requirements.txt`: A file containing the list of required Python packages to run the project. Install these packages using pip before running the game.

## How the NEAT AI works
NEAT (NeuroEvolution of Augmenting Topologies) is a method of evolving artificial neural networks. In this project, the NEAT algorithm is utilized to train an AI to play the Flappy Bird game.

1. The NEAT algorithm starts with a population of randomly generated neural networks (genomes) that control the birds.
2. Each bird's performance in the game is evaluated using a fitness function. The fitness function could be based on how far the bird travels, how many pipes it successfully passes through, etc.
3. The genomes with the highest fitness scores are selected to create the next generation. These genomes undergo mutation and crossover to create offspring, introducing new genetic material to potentially improve their performance.
4. The process of evaluation, selection, and reproduction is repeated for multiple generations until a bird successfully reaches a score of 100 or higher.
5. The winning genome with the highest fitness score is saved as `winner_genome.pkl`, which is then used by the `AI_mode.py` script to demonstrate the AI playing the game automatically.


## Training Mode Demo

https://github.com/Siddharth-2382/Flappy-Bird-AI/assets/94699055/fc11a58f-8a4a-450c-8f2a-554b38da3c66

## AI Mode Demo

https://github.com/Siddharth-2382/Flappy-Bird-AI/assets/94699055/4d2bd3a8-ced7-42ff-9e5b-39f860f4fc80
