# Build a Player Interface
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define an abstract class named Player that inherits from the abc.ABC class.

# The Player class should have an __init__ method that sets:

# The moves attribute to an empty list.
# The position attribute to (0, 0).
# The path attribute to a list containing the initial position.
# The Player class should have a method named make_move that:

# Uses random.choice to get a random move from the moves attribute (defined in the concrete class).
# Adds the values from the selected move to the current position and updates the position attribute.
# Appends the new position tuple to the path attribute.
# Returns the new position.
# The Player class should have an abstract method named level_up to be implemented in concrete classes.

# You should define a Pawn class that inherits from the Player class.

# The Pawn class should use super() to call the parent's __init__ method and then set the moves attribute to a list of tuples representing x, y coordinates.

# Each coordinate tuple should represent a movement of 1 unit in the following directions: up, down, left, right.

# The Pawn class should implement a concrete level_up method by adding more moves to the moves attribute. The added moves should represent the four diagonal movements (for example, 1 unit down plus 1 unit left).

# Note: Standard library modules should be imported without using aliases. Tests related to the Player class will fail until the Pawn class becomes instantiable.

# Tests:
# Waiting:1. You should have a class named Player.
# Waiting:2. The Player class should inherit from the ABC class of the abc module.
# Waiting:3. The Player class should have an __init__ method.
# Waiting:4. The Player's __init__ method should have a single parameter self.
# Waiting:5. The Player's __init__ method should set self.moves to an empty list.
# Waiting:6. The Player's __init__ method should set self.position to (0, 0).
# Waiting:7. The Player's __init__ method should set self.path to a list containing the initial position.
# Waiting:8. The Player class should have a make_move method.
# Waiting:9. The Player's make_move method should have a single parameter self.
# Waiting:10. The Player's make_move method should use random.choice to get a random move from the moves attribute.
# Waiting:11. The Player's make_move method should update the position attribute by adding to it the coordinates of the randomly selected move.
# Waiting:12. The Player's make_move method should append the new position tuple to the path attribute.
# Waiting:13. The Player's make_move method should return the updated position attribute.
# Waiting:14. The Player class should have a level_up method.
# Waiting:15. The Player's level_up method should have a single parameter self.
# Waiting:16. The Player's level_up method should be an abstract method.
# Waiting:17. The Player class should be an abstract class.
# Waiting:18. You should have a class named Pawn.
# Waiting:19. The Pawn class should inherit from the Player class.
# Waiting:20. The Pawn class should have an __init__ method.
# Waiting:21. The Pawn's __init__ method should have a single parameter self.
# Waiting:22. The Pawn's __init__ method should call the parent's __init__ with using the super function.
# Waiting:23. The Pawn's __init__ method should set the moves attribute to a list of tuples representing x, y coordinates, where each coordinate tuple represents a movement of 1 unit in the following directions: up, down, left, right.
# Waiting:24. The Pawn class should have a level_up method.
# Waiting:25. The Pawn's level_up method should add the four diagonal movement of 1 unit to the moves attribute.








from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self) -> tuple:
        move = random.choice(self.moves)
        new = (self.position[0] + move[0],
               self.position[1] + move[1])
        self.position = new  #  (new_x, new_y)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]
    
    def level_up(self):
        self.moves.extend([
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ])


#player = Player()
#print(player.moves)
pawn = Pawn()
print(pawn.moves)
pawn.level_up()
print(pawn.moves)
