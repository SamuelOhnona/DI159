import math
import turtle

class Circle:
    """
    A class representing a circle that allows:
    - Getting and setting radius and diameter
    - Computing area
    - Adding two circles
    - Comparing circles
    - Sorting circles
    - Drawing sorted circles using Turtle (bonus feature)
    """
    
    def __init__(self, radius=None, diameter=None):
        """Initialize the circle with either radius or diameter."""
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided")

    @property
    def radius(self):
        """Getter for radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Setter for radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def diameter(self):
        """Compute the diameter dynamically."""
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        """Setter for diameter with validation."""
        if value <= 0:
            raise ValueError("Diameter must be positive")
        self._radius = value / 2

    @property
    def area(self):
        """Compute the area dynamically."""
        return math.pi * self._radius ** 2

    def __str__(self):
        """User-friendly string representation of the circle."""
        return f"Circle(radius={self._radius}, diameter={self.diameter}, area={self.area:.2f})"

    def __repr__(self):
        """Technical representation of the circle."""
        return f"Circle({self._radius})"

    def __add__(self, other):
        """Add two circles to create a new circle with a combined radius."""
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self._radius + other._radius)

    def __lt__(self, other):
        """Compare two circles based on radius (for sorting)."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius

    def __eq__(self, other):
        """Check if two circles are equal based on radius."""
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius

# Bonus: Draw sorted circles using Turtle
def draw_circles(circles):
    """Draw circles using the Turtle module in order of their size."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    pen = turtle.Turtle()
    pen.speed(0)  # Fastest drawing speed
    
    start_x = -200  # Initial X position
    pen.up()  # Lift pen to move without drawing

    for circle in circles:
        pen.goto(start_x, -circle.radius)  # Move to the correct position
        pen.down()  # Start drawing
        pen.circle(circle.radius)  # Draw the circle
        pen.up()  # Lift pen after drawing
        start_x += circle.diameter + 10  # Shift right for next circle
    
    screen.mainloop()  # Keep window open

# Example Usage
if __name__ == "__main__":
    # Create some circle instances
    c1 = Circle(radius=5)
    c2 = Circle(diameter=20)
    c3 = Circle(radius=3)
    c4 = c1 + c3  # New circle with combined radius

    # Create a list of circles and sort them
    circles = [c1, c2, c3, c4]
    circles.sort()

    # Print sorted circles
    print(circles)  # Output: Sorted by radius

    # Uncomment below to draw sorted circles
    draw_circles(circles)
