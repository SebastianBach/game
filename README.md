# A Simple Game

The game board consists of a series of squares. The players place their game piece on the field 0; the winner is the first to reach the field 30.

The players take turns rolling the dice (D6) and have a choice. Either they move their piece towards the goal by the number of points rolled, **or** they move an opposing piece backwards by the same number of points. What would you choose?

# Strategies

## Run

```"run"```: I move forward no matter what.

## Chaos

```"chaos"```: In two out of three cases, I move forward. In one out of three cases, I move a random opponent's piece back.

## Big Steps

```"big"```: If I roll a 4 or more, I go forward. If I roll a 3 or less, I move the leading player's piece back.

## Second Place

```"second"```: Everyone tries to throw back the player who is in the lead. That's why I like to stay in 2nd place at first. Only towards the end do I sprint to the finish.

## Waiting

```"waiting"```: Everyone tries to throw back the player who is in the lead. That's why I stop when I reach square 24 or 25. I throw back anyone who overtakes me and wait for me to roll a 5 or 6 to win.

## Drag Down

```"drag"```: I move forward. But when I see that a player is about to win, I pull him back down.

# Run

Run the game via:

```
python game.py MODE SEED PLAYER_1 PLAYER_2 PLAYER_3 ...
```

- *MODE*: The game mode. *show* will run the game with a delay, *run* will run the game without delay.
- *SEED*: random number generator seed.
- *PLAYER_1* : For each player, set the used strategy.

Example:

```
python game.py show 123 run second waiting
``` 

# Test

Execute test with:

```
python tests.py
```

# Extend

To add a new playing strategy, extend ```strategies.py```:

```
def strategy_custom(move: my_move, id: int, cnt: int, roll: int, state: list):

    move.move_me()
    return move


strategies["custom"] = strategy_custom
```

Now players with the ```custom``` strategy can be added:

```
python game.py show 123 custom run waiting
```

Your custom strategy function must return the modified ```move``` object. Either choose ```move_me()``` to move the player or ```move_other()``` to move back an opponent.

The arguments given to your function are:

- ```move```: ```my_move```object to edit and return.
- ```id```: ID of the current player. Is the index in the ```state``` list.
- ```cnt```: Number of players. Same as ```len(state)```.
- ```roll```: The number that was rolled.
- ```state```: List storing the current position of each player.

The current position of the player is ```state[id]```.

As soon as the points rolled are enough to win the game, the game engine registers this case. The strategy does not have to handle this case explicitly.

Don`t forget to add a unit test to ```tests.py```.
