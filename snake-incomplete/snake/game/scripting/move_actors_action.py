from game.scripting.action import Action

# TODO: Implement MoveActorsAction class here!

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor


class MoveActorsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of MoveActorsAction is to move all the actors involved in the game.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new MoveActorsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        for actor in cast.get_all_actors():
            actor.move_next()
