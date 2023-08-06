from yahtzee_api.game import Game
from .constants import (NOT_INT)


class YahtzeeSinglePlayerV1:
    """Environment for training a single RL agent to maximize their
    score in a Yahtzee game. This is very close to the V0 environment,
    with the exception of the reward distribution system, which has been rebuilt.
    This is the first environment to correspond with the deployment of the recommendation
    feature added in API v1.3.0. Agents using this environment will feature a new style Q table.
    """

from yahtzee_api.game import Game
from .constants import (NOT_INT)


class YahtzeeSinglePlayerV1:
    """Environment for training a single RL agent to maximize their
    score in a Yahtzee game. Follows a similar structure to Open AI
    Gym environments, but does not fully conform to their standard.
    This is the first version of the Single Player Environment. 
    """
    def __init__(self, roll_rwd, roll_all_rwd):
        """Constructor that parameterizes the rewards for rolling.

        In general, if the agent scores a value it receives that score
        as reward. When it decides to roll some or all of the dice,
        it also should receive some reward. However, it is not clear
        what the best values for that reward is, so for research
        purposes it is made configurable here. 
        Args:
            roll_rwd (int): reward for rolling some dice
            roll_all_rwd (int): reward specifically for rolling all
                of the dice (action 25).
        """
        self.ytz = Game(1)      # Initialize 1-player game of Yahtzee
        self.roll_rwd = roll_rwd
        self.rol_all_rwd = roll_all_rwd

    def step(self, action):
        """Executes a single timestep in the environment.

        Args:
            action (int): specifies the action to take.
                Actions 0-12 score the corresponding index
                of the Player's scorecard. Actions 13-25 
                reroll the dice to pursue the score at 
                index action - 13. For example, taking action
                13 would pass the list of dice indices from
                the theoretical scorecard for the 1's item 
                to the roll function. In this way, the agent 
                can "freeze" the 1's it rolled and try to get more,
                while still being free to roll any of the dice it 
                chooses on subsequent re-rolls. Action 26 rolls all dice.
                See the Yahtzee API docs at
                https://yahtzee-api.tomarbeiter.com for more info
                about how the scorecard, dice rolling, etc. works.
        Returns:
            Tuple: The entire instance of the self.ytz
            Game object. Also returns reward, boolean done indicator,
            and basic debugging info.
        """
        if not isinstance(action, int):
            raise TypeError(NOT_INT)
        # Roll dice to pursue certain score
        if action > 12 and action < 26:
            self.ytz.c_player.roll(self.ytz.c_player.t_scorecard[action - 13][1])
            return (self.ytz, self._make_reward(action), False, "Dice were rolled.")
        if action == 26:
            self.ytz.c_player.roll([0, 0, 0, 0, 0])
            return (self.ytz, 0, False, "Dice were rolled.")
        # Score
        else:
            self.ytz.c_player.end_turn(action)
            # One player game, so always advance global turn
            self.ytz.next_player()
            # If the game is over, set Done flag
            return (
                self.ytz,
                self.ytz.c_player.scorecard[action][0],
                len(self.ytz.winner) != 0,
                str(action - 1) + " was scored."
            )

    def reset(self):
        """Starts a new game of Yahtzee in the same class instance."""
        self.ytz = Game(1)

    def _make_reward(self, action):
        """Generates discoutned rewards for rerolling.
        
        All of these rewards are based on a similar fraction of the max score
        in question. 3 of a kind, 4 of a kind, and Chance are not really 
        optimized for this sort of learning system (API v1.3.0), but as a 
        starting point we'll just let them be whatever they end up being.
        """
        # 1 -> 6
        if action >= 13 and action <= 18:
            return self.ytz.c_player.t_scorecard[action - 13][0] / \
                self.ytz.c_player.t_scorecard[action - 13][1].count(1)
        # 3/4 of a Kind
        elif action == 19 or action == 20:
            return sum(self.ytz.c_player.dice) / \
                self.ytz.c_player.t_scorecard[action - 13][1].count(1)
        # Full House
        elif action == 21:
            return 25 / self.ytz.c_player.t_scorecard[action - 13][1].count(1)
        # Small Straight
        elif action == 22:
            return 30 / self.ytz.c_player.t_scorecard[action - 13][1].count(1)
        # Large Straight
        elif action == 23:
            return 40 / self.ytz.c_player.t_scorecard[action - 13][1].count(1)
        # Chance
        elif action == 24:
            return 12 if sum(self.dice) <= 12 else 3
        # Yahtzee
        else:
            return 50 * self.ytz.c_player.t_scorecard[action - 13][1].count(1)
        