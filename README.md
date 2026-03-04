# Advanced Counter App

A Python application to track tasks, hours, or repetitions over time with visual progress graphs.

## Overview

This project allows users to record daily counts for any task (e.g., studying, exercise, sleep) and visualize their progress with graphs. The app saves data locally in JSON format, making it persistent across sessions.

## Features

- Add tasks with custom counts/hours per day  
- View task statistics and progress graphs over time  
- Flexible input: choose any date or default to today  
- Data saved automatically in `tasks.json`  

## Installation

1. Make sure you have Python installed (>=3.7)  
2. Clone the repository or download the files  
3. Install required libraries:

```bash
pip install matplotlib
Usage

Activate your virtual environment (optional but recommended):

# Windows PowerShell
.\venv\Scripts\Activate.ps1

Run the application:

python advcounter_app.py

Choose from the menu:

1. Add Task Count/Hours
2. View Task Stats/Graph
3. Exit

Follow the prompts to add tasks or view graphs.

Example
Choose option: 1
Enter task name: study
Enter date (DD-MM-YYYY) or leave blank for today: 
Enter hours/reps for this task: 5
study updated for 05-03-2026 with 5.0 units.

Choose option: 2
Enter task name: study
05-03-2026: 5.0
06-03-2026: 4.0

The graph will display progress over the entered dates.

Files

advcounter_app.py – main Python script for the app

tasks.json – stores task data persistently
