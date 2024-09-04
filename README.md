# Python statistics project

Uses the premier league fantasy API to fetch premier league data.

*WORK IN PROGESS* - Currently only reads in static data for the season (players, teams, fixtures and
 dates)

# Usage

To run the project, use the following command from the project root:
```bash
python3 src/premier-league-stats/main.py <command> [options]
```
Various arguments will decide what part of the project to run (preprocessing, prediction, ...)

In order to run the whole pipeline, including testing, preprocessing and prediction with all the default values, you can use>
```bash
./run.sh
```

## Commands
**Import data:** Imports the data from a space separated string of sources (only "fantasy" is available now).
  ```bash
  python3 src/premier-league-stats/main.py import "fantasy source_2 source_3"
  ```
**Data preprocessing:** Preprocess the data before performing any analysis.
  ```bash
  python3 src/premier-league-stats/main.py preprocess [options]
  ```
  ```bash
  python3 src/premier-league-stats/main.py predict [options]
  ```

## Data preprocessing
The data preprocessing is not finished yet, but is currently being implemented.

# Testing
The project contains tests created with pytest. To run all tests runt the command `pytest` in the main directory.

# Future plans (in no particular order)
* Train Machine learning models to analyze statistics
* Implement other methods to analyze statistics
* Fantasy Premier League analytics
* Use external database to store data (locally? Supabase? Something else?)
* Supplement with other APIs to fetch statistics
    * For example OneFutbol's
    * Webscraping?
* Create a user interface (webapp?) to visualize and easily use the project

