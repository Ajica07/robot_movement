**Robot Movement Simulation**

This project simulates robots moving on a grid. The robots can be moved in four directions (North, South, East, West) based on given input commands like N4, E3, etc. The program handles robot collisions, ensures robots don't move outside the grid, and tracks the current position of each robot.

To use the program, first create robots by assigning them a unique ID. By default, all robots start at position (0, 0) on the grid. You can move robots by passing a series of commands such as "E2" (move 2 steps east) or "S1" (move 1 step south). If a robot tries to move outside the grid or into a cell already occupied by another robot, the movement stops, and the robot stays in its last valid position.

The program includes unit tests to check robot movements, boundary conditions, and robot collisions. To run the program, ensure Python 3 is installed on your system and execute the script using the following command in your terminal:

python robot_movement.py

To Run the Program:
Use the code in robot_movement.py to simulate the robots. Here's an example of how to create robots and move them:

terrain = Terrain(5, 5)  # Create a 5x5 grid
terrain.add_robot(1)     # Add robot with ID 1
terrain.add_robot(2)     # Add robot with ID 2

# Move robot 1 (2 steps East, 2 steps South) 
terrain.move_robot(1, ["E2", "S2"])

# Move robot 2 (1 step South, 1 step East)
terrain.move_robot(2, ["S1", "E1"])

# Get robot positions
print(terrain.get_robot_position(1))
print(terrain.get_robot_position(2))

Run Unit Tests:
To ensure everything is working, run the unit tests:

python -m unittest robot_movement.py
