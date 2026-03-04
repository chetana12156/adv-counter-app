Advanced Counter App
The Advanced Counter App is a Python-based tool that allows users to track and visualize daily activities. Users can log the number of hours, repetitions, or units for any task, and view progress over time through graphs. This project is designed to help users monitor habits, productivity, or any measurable activity effectively.

Features
Add hours/reps for multiple tasks per day

Choose custom dates for task entries

View task progress as a graph

Persistent data storage using JSON

Simple and user-friendly command-line interface

Installation
Clone the repository:

git clone https://github.com/your-username/adv-counter-app.git
Navigate to the project folder:

cd adv-counter-app
Create and activate a virtual environment (optional but recommended):

python -m venv venv
# Windows
.\venv\Scripts\Activate.ps1
# Mac/Linux
source venv/bin/activate
Install required packages:

pip install matplotlib
Usage
Run the app:

python advcounter_app.py
Options in the app:

Add Task Count/Hours – Enter task name, date (optional), and hours/reps.

View Task Stats/Graph – Choose a task to see daily progress and a visual graph.

Exit – Close the app.

Example
1. Add Task Count/Hours
2. View Task Stats/Graph
3. Exit
Choose option: 1
Enter task name: Study
Enter date (DD-MM-YYYY) or leave blank for today: 
Enter hours/reps for this task: 5
Study updated for 2026-03-05 with 5.0 units.
Choose option: 2
Enter task name: Study
05-03-2026: 5.0
06-03-2026: 3.0
[Graph opens showing progress over time]
Files
advcounter_app.py – main Python script

tasks.json – stores task data

.gitignore – ignores unnecessary files like virtual environments

License
This project is open-source and free to use.
