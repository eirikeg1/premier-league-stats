from dataclasses import dataclass
from datetime import datetime

@dataclass
class News:
    description: str
    time_added: str
