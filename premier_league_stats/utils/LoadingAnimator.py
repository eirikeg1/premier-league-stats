import sys
import time
from typing import List


class LoadingAnimator:
    
    _animation_speed = 100
    _animation_length = 20
    _direction = 1
    
    # ". . . . . . o O o . . . . . . ."
    # ". . . . . o O o . . . . . . . ."
    def _circle_and_dot_pattern(self):
        frame = 0
        while True:
            yield f"{' . ' * frame}o O o{' . ' * (self._animation_length - frame)}"
            
            frame += self._direction
            
            if frame == self._animation_length or frame == 0:
                self._direction *= -1
    
    def __init__(self, animation_speed: int = None, animation_pattern: List[str] = None):
        if animation_speed:
            self._animation_speed = animation_speed  
        if animation_pattern:    
            self._animation_pattern = animation_pattern
            
        self._animation_pattern = self._circle_and_dot_pattern()
        self._counter = 0
        self._position = 0
    
    def print_animation(self):
        """Animate a loading animation which prints every 1/animation_speed function calls"""
        self._counter += 1
        print(self._animation_pattern[self._counter % len(self._animation_pattern)], end="\r")

    def print_animation_every_x(self, animation_speed = None):
        """Animate a loading animation which prints every 1/animation_speed function calls"""
        # print(f"animation_speed: {animation_speed}, counter: {self._counter}")
        if not animation_speed:
            animation_speed = self._animation_speed
        self._counter += 1
        if self._counter % self._animation_speed == 0:
            #print(self._animation_pattern[self._position % len(self._animation_pattern)], end="\r")
            print(next(self._animation_pattern), end="\r")
            self._position += 1
