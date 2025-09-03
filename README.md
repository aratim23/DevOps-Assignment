ACEest_Fitness and Gym - DevOps Assignment
============================

### BITS ID: 2024TM93091
### Name: Arati Manoj Chandri

### Overview

ACEest_Fitness and Gym is a simple desktop application to log and track workout routines. This project demonstrates core DevOps practices by integrating source control, automated unit testing with Pytest, containerization using Docker, and CI/CD automation with GitHub Actions.

### Folder Structure

    DevOps-Assignment/
    ├
    ├── ACEest_fitness.py        # Main application code (Tkinter + WorkoutManager)
    ├── test_workout_manager.py  # Pytest unit tests for WorkoutManager logic
    ├── requirements.txt         # Python packages list
    ├── Dockerfile               # Instructions for Docker containerization
    ├── README.md                # This documentation file
    └── .github/
       └── workflows/
           └── main.yml          # Github Actions CI/CD pipeline config 


### Local Setup

1. Requirements
   - Python 3.11+
   - pip

2. Install dependencies

   pip install -r requirements.txt

3. Run application

   python ACEest_fitness.py

4. Running unit test

   pytest test_workout_manager.py

5. To build and use docker

   docker build -t aceest_fitness_app .
   docker run aceest_fitness_app

