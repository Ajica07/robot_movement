class Terrain:
    def __init__(self, rows, cols):
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols
        self.robots = {}
    
    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError(f"Robot {robot_id} already exists.")
        # Start all robots at (0, 0)
        self.robots[robot_id] = (0, 0)
        self.grid[0][0] = robot_id
    
    def move_robot(self, robot_id, commands):
        if robot_id not in self.robots:
            raise ValueError(f"Robot {robot_id} does not exist.")
        
        x, y = self.robots[robot_id]
        for command in commands:
            direction = command[0]
            steps = int(command[1:])
            
            for _ in range(steps):
                new_x, new_y = x, y
                
                # Determine new position based on direction
                if direction == 'N':
                    new_x -= 1
                elif direction == 'S':
                    new_x += 1
                elif direction == 'E':
                    new_y += 1
                elif direction == 'W':
                    new_y -= 1
                
                # Check for grid boundaries
                if not (0 <= new_x < self.rows and 0 <= new_y < self.cols):
                    print(f"Robot {robot_id} reached boundary at ({x}, {y}).")
                    break
                
                # Check if destination is occupied by another robot
                if self.grid[new_x][new_y] is not None:
                    print(f"Robot {robot_id} stopped due to another robot at ({x}, {y}).")
                    break
                
                # Move the robot to the new position
                self.grid[x][y] = None  # Clear the old cell
                x, y = new_x, new_y
                self.grid[x][y] = robot_id  # Set the new cell
                
        # Update the robot's final position
        self.robots[robot_id] = (x, y)
    
    def get_robot_position(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError(f"Robot {robot_id} does not exist.")
        return self.robots[robot_id]
    
# Unit Tests
import unittest

class TestRobotMovement(unittest.TestCase):
    def setUp(self):
        # Initialize a 5x5 terrain for testing
        self.terrain = Terrain(5, 5)
        self.terrain.add_robot(1)
        self.terrain.add_robot(2)
    
    def test_move_robot_north_boundary(self):
        self.terrain.move_robot(1, ["N1"])
        self.assertEqual(self.terrain.get_robot_position(1), (0, 0))
    
    def test_move_robot_simple_movement(self):
        self.terrain.move_robot(1, ["E2", "S2"])
        self.assertEqual(self.terrain.get_robot_position(1), (2, 2))
    
    def test_robot_collision(self):
        self.terrain.move_robot(1, ["E1", "S1"])
        self.terrain.move_robot(2, ["S1", "E1"])
        self.assertEqual(self.terrain.get_robot_position(2), (1, 0))  # Robot 2 should stop

if __name__ == "__main__":
    unittest.main()
