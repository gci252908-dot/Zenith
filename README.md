# Zenith
A text-based RPG where you attempt to claim the epic Zenith. This is a legendary command-line tale where you make choices to unfold the story around you. 
This version is just a demo to show off the features of the game and direction of the development. Created by Max Natzke with some help from Liam Sholler,
This epic saga will rock your socks off and leave you thinking... what if I had the Zenith?

## Video demo
https://youtu.be/5kvSBM02Av0

## Usage

### Requirements

* You must have `Python3.10 >=` to use this program.

### Building / Running
 
1. Clone the repository using your command-line
```bash
git clone https://github.com/gci252908-dot/Zenith.git
```

2. Download the requirements using your command-line
```bash
pip install -r requirements.txt
```

3. Run the program using your command-line
```bash
python project.py
```

## Features

### High-Level Breakdown

* Modular classes for the player, game, weapons, zones, etc.
* A game loop based on `PyTerminal`, the terminal "game-engine"
* JSON-based formatting in the `res/` folder to avoid unnecessary programming
* Tests for ensuring implementations are correct

### The Architecture

Entry point -> project.py
project.py -> Game / PyTerminal setup -> game.run()
Every frame -> Update / draw function called 
Update / draw function -> call into Game update / draw
Game update / draw -> update player stats, and show the next option
