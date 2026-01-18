# Asteroids Game 🚀

A classic Asteroids game built with Python and Pygame.

## Description

This is a recreation of the classic Asteroids arcade game where you control a spaceship and shoot asteroids. Large asteroids split into smaller ones when hit, and the game ends if an asteroid collides with your ship.

## Features

- Player-controlled spaceship with rotation and movement
- Shooting mechanics with cooldown
- Asteroids that split into smaller pieces when shot
- Collision detection between player, asteroids, and shots
- Game state logging for debugging

## Controls

- **A**: Rotate left
- **D**: Rotate right
- **W**: Move forward
- **S**: Move backward
- **SPACE**: Shoot

## Installation

1. Make sure you have Python 3.8+ installed
2. Clone this repository:
   ```bash
   git clone https://github.com/Ahmed-Yassine-Hajjaji/Asteroids-Game.git
   cd asteroids-game
   ```
3. Install dependencies using uv (recommended):
   ```bash
   uv sync
   ```
   Or using pip:
   ```bash
   pip install pygame
   ```

## Running the Game

```bash
uv run main.py
```

Or if using pip:
```bash
python main.py
```

## Project Structure

- `main.py` - Main game loop and setup
- `player.py` - Player ship class
- `asteroid.py` - Asteroid class with splitting logic
- `shot.py` - Projectile class
- `asteroidfield.py` - Asteroid spawning system
- `circleshape.py` - Base class for circular game objects
- `constants.py` - Game constants and configuration
- `logger.py` - Game state logging utilities

## Requirements

- Python 3.8+
- Pygame

