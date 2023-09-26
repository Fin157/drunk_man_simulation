from typing import List, Tuple

class Position2D:
    DIM_COUNT = 2

    def __init__(self, x = 0, y = 0) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> None:
        return self.__x
    
    @x.setter
    def x(self, value: int) -> None:
        self.__x = value

    @property
    def y(self) -> None:
        return self.__y
    
    @y.setter
    def y(self, value: int) -> None:
        self.__y = value

    # Offsets a position by the specified offset
    def offset_pos(self, offset: Position2D) -> Position2D:
        # Create a list representing the altered position
        new_pos = Position2D()

        # Apply the offset in every axis
        for i in range(self.DIM_COUNT):
            new_pos.append(pos[i] + offset[i])

        # Return the altered position
        return new_pos

    def offset_clamped(pos: list | tuple, offset: list | tuple, min: list | tuple, max: list | tuple) -> list:
        if not is_same_space(pos, min) or not is_same_space(pos, max):
            raise Exception("Invalid min or max bound as they are from a different space than the position.")

        result = offset_pos(pos, offset)

        for i in range(len(result)):
            result[i] = clamp(result[i], min[i], max[i])

        return result

    # Executes a scalar multiplication operation on the specified position
    def scalar_multiply(pos: list | tuple, scalar: int) -> list:
        # Copy the position to a new list to alter the copy rather than the original
        new_pos = list(pos).copy()

        # Do the scalar multiplication
        for axis in pos:
            axis *= scalar

        # Return the altered position
        return new_pos

    # Compares two positions and determines if they are equal or not
    def compare(first: list | tuple, second: list | tuple) -> bool:
        # Make sure the positions exist in the same space
        if not is_same_space(first, second):
            raise Exception("The positions are from a different space.")

        # Compare the positions
        for i in range(len(first)):
            # If the positions' value in this axis doesn't match, immediately stop executing with the result of "False"
            if not first[i] == second[i]:
                return False
        
        # The positions fully match
        return True

    # Checks if a position is inside the specified bounds
    def is_on_edge(pos: list | tuple, min_bound: list | tuple, max_bound: list | tuple) -> bool:
        # Make sure the position and the min and max bounds are in the same space
        if not is_same_space(pos, min_bound):
            raise Exception("Min bound belongs to a different space than the position.")
        if not is_same_space(pos, max_bound):
            raise Exception("Max bound belongs to a different space than the position.")

        # Check that the position is inside the bounds in every axis
        for i in range(len(pos)):
            if pos[i] <= min_bound[i] or pos[i] >= max_bound[i]:
                return False
            
        return True

    # Returns the spacial middle point between the minimum and maximum rounded to integral positions
    def get_middle(min: list | tuple, max: list | tuple) -> list:
        if not is_same_space(min, max):
            raise Exception("The min and max positions aren't in the same space.")
        
        middle = list()

        for i in range(len(min)):
            middle.append(round((max[i] - min[i]) / 2))

        return middle

class Endpoint2D(Position2D):
    end_message = str()
    char = None

    def __init__(self, end_message: str, char: chr, x = 0, y = 0) -> None:
        Position2D.__init__(self, x, y)
        self.end_message = end_message
        self.char = char