# game-of-life-py

## About
- Console implementation of Conway's "Game of life"
- No external dependencies are required

## Installation
Clone this repository:
```bash
git clone https://github.com/SandorDiGriz/game-of-life-py.git
```

## Usage
```bash
execution: python <your path to main.py> *args

obligatory arguments:
  --rows, -r,
        Number of grid's rows
  --columns, -c
        Number of grid's columns
  
optional arguments:
  --mode, -m, 
        Mode of cell generation change  ("auto" | "one-step"), default = auto
  --birth_chance, -b,
        Percentage probability of a cell being born, default = 25
  --generations_limit, -g,
        Maximum number of generations, default = 250
```

## Examples

Auto game mode

![auto mode example](https://github.com/SandorDiGriz/game-of-life-py/blob/dev/images/auto_mode_example.gif)

One-step game mode

![one-step mode example](https://github.com/SandorDiGriz/game-of-life-py/blob/dev/images/one_step_mode_example.gif)
