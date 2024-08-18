#!/bin/bash

# Run tests
pytest && 


# Run the main script
python3 src/premier_league_stats/main.py --command "full"

