# Blackjack (Twenty-One)

A command-line Blackjack game written in Python. Play one or more rounds against a dealer that follows standard casino rules.

## How to play

- You and the dealer are each dealt two cards. One of the dealer's cards stays hidden until the round ends.
- Number cards are worth their face value, face cards (J/Q/K) are worth 10, and an Ace is worth 11 unless that would bust your hand, in which case it counts as 1.
- On your turn, choose to **Hit** (take another card) or **Stand** (keep your current hand) until you stand or bust (go over 21).
- The dealer then reveals their hidden card and must keep hitting until their hand totals 17 or more.
- Closest to 21 without going over wins. A tie is a push, and going over 21 is an automatic loss.

## Requirements

- Python 3.6+
- No external dependencies (uses only the Python standard library)

## Getting started

```bash
git clone git@github.com:maroun28/Blackjack.git
cd Blackjack
python3 main.py
```

You'll be prompted for how many games you want to play, then dealt in. Follow the on-screen prompts to hit or stand.

## Project structure

```
main.py   # Card, Deck, Hand, and Game classes, plus the game loop
```

- **`Card`** – a single playing card (suit and rank).
- **`Deck`** – a standard 52-card deck that can be shuffled and dealt from.
- **`Hand`** – a player's or dealer's cards, with Blackjack value calculation (including Ace handling).
- **`Game`** – runs the main game loop: dealing, player turns, dealer turns, and scoring.

## Status

This is a learning project for practicing Python and object-oriented programming. Contributions and suggestions are welcome.
