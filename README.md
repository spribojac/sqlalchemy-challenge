# Climate Analysis and API using Flask

Welcome to the Climate Analysis and API project! In this project, I'll analyze climate data and build a Flask API to provide climate-related information based on the data. I'll follow the steps outlined below to accomplish this task.

## Part 1: Analyze and Explore the Climate Data

### Precipitation Analysis
- Find the most recent date in the dataset.
- Calculate the previous 12 months of precipitation data.
- Load and analyze the data using Pandas and Matplotlib.
- Display summary statistics for the precipitation data.

### Station Analysis
- Find the total number of stations in the dataset.
- Identify the most active stations by listing stations and their observation counts.
- Calculate the lowest, highest, and average temperatures for the most active station.
- Retrieve the last 12 months of temperature observation (TOBS) data for the most active station and visualize it as a histogram.

## Part 2: Design Your Climate App

Design a Flask API with the following routes:

- `/`: The homepage listing all available routes.
- `/api/v1.0/precipitation`: Provides JSON data for the last 12 months of precipitation.
- `/api/v1.0/stations`: Returns a list of stations from the dataset.
- `/api/v1.0/tobs`: Retrieves temperature observations for the most active station in the last year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Returns JSON data with minimum, average, and maximum temperatures for specified date ranges.

## Usage
- Clone the repository to your local machine.
- Install the necessary dependencies (e.g., Flask, SQLAlchemy, Pandas, Matplotlib).
- Run the Flask app using `python app.py`.
- Access the API endpoints to retrieve climate data.

### Credits
Used the exercises in class to build my code, youtube videos, stackoverflow etc to help troubleshoot!
Very tough exercise for me
