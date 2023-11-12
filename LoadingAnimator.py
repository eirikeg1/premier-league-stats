import sys
import time
from typing import List


class LoadingAnimator:
    
    _animation_speed = 100
    _animation_pattern = [
        ". . . . . . o O o . . . . . . .",
        ". . . . . o O o . . . . . . . .",
        ". . . . o O o . . . . . . . . .",
        ". . . o O o . . . . . . . . . .",
        ". . o O o . . . . . . . . . . .",
        ". o O o . . . . . . . . . . . .",
        "o O o . . . . . . . . . . . . .",
        "O o . . . . . . . . . . . . . .",
        ". . o O o . . . . . . . . . . .",
        ". . . o O o . . . . . . . . . .",
        ". . . . o O o . . . . . . . . .",
        ". . . . . o O o . . . . . . . .",
        ". . . . . . o O o . . . . . . .",
        ". . . . . . . o O o . . . . . .",
        ". . . . . . . . o O o . . . . .",
        ". . . . . . . . . o O o . . . .",
        ". . . . . . . . . . o O o . . .",
        ". . . . . . . . . . . o O o . .",
        ". . . . . . . . . . . . o O o .",
        ". . . . . . . . . . . . . o O o",
        ". . . . . . . . . . . . . . o O",
        ". . . . . . . . . . . . o O o .",
        ". . . . . . . . . . . o O o . .",
        ". . . . . . . . . . o O o . . .",
        ". . . . . . . . . o O o . . . .",
        ". . . . . . . . o O o . . . . .",
        ". . . . . . . o O o . . . . . .",
    ]
    
    def __init__(self, animation_speed: int = None, animation_pattern: List[str] = None):
        if animation_speed:
            self._animation_speed = animation_speed  
        if animation_pattern:    
            self._animation_pattern = animation_pattern
        self._counter = 0
        self._position = 0
    
    def print_animation(self):
        """Animate a loading animation which prints every 1/animation_speed function calls"""
        self._counter += 1
        print(self._animation_pattern[self._counter % len(self._animation_pattern)], end="\r")

    def print_animation_every_x(self, animation_speed = None):
        """Animate a loading animation which prints every 1/animation_speed function calls"""
        if not animation_speed:
            animation_speed = self._animation_speed
        self._counter += 1
        if self._counter % self._animation_speed == 0:
            print(self._animation_pattern[self._position % len(self._animation_pattern)], end="\r")
            self._position += 1
