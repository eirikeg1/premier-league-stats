from dataclasses import dataclass
from datetime import datetime

@dataclass
class News:
    description: str
    time_added: datetime

# Example usage
news_item = News(description="New update on the project.", time_added=datetime.now())

# Accessing values
print(news_item.description)  # Output: New update on the project.
print(news_item.time_added)   # Output: (current datetime)
