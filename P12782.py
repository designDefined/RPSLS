from RPSLS_player import RPSLS_player
import random


# counter enemy's most pick

class P12782(RPSLS_player):

    def __init__(self):
        self._all: [str] = ["rock", "paper", "scissors", "spock", "lizard"]
        self._memory: [[str, int]] = [["rock", 0], ["paper", 0], ["scissors", 0], ["lizard", 0], ["spock", 0]]
        self._count: int = 0
        self._strategy: str = "random"

    def shoot(self):
        self._choose_strategy()
        if self._strategy == "random":
            return self._random()
        elif self._strategy == "counter_most":
            return self._counter(self._memory[4][0])

    def update(self, result: str, competitor_shot: str):
        self._count = self._count + 1
        for item in self._memory:
            if item[0] == competitor_shot:
                item[1] = item[1] + 1
        self._memory.sort(key=lambda x: x[1])

    def _choose_strategy(self):
        if self._memory[4][1] > self._count / 2:
            self._strategy = "counter_most"
        else:
            self._strategy = "random"

    def _counter(self, enemy: str):
        if enemy == "rock":
            return "paper"
        elif enemy == "paper":
            return "scissors"
        elif enemy == "scissors":
            return "spock"
        elif enemy == "spock":
            return "lizard"
        else:
            return "rock"

    def _random(self):
        return self._all[random.randint(0, 4)]
