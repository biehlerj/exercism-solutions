"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self) -> None:
        """Reduces the HP of the Alien by one."""
        self.health -= 1

    def is_alive(self) -> bool:
        """Checks if the Alien is still alive

        :return: bool - True if HP > 0 else False
        """
        if self.health > 0:
            return True
        return False

    def teleport(self, new_x: int, new_y: int) -> None:
        """Teleports the alien to the new coordinates

        :param new_x: int - new x coordinate
        :param new_y: int - new y coordinate
        """
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other_object) -> None:
        """Checks if the Alien has collided with something"""
        pass


def new_aliens_collection(aliens: list[tuple[int, int]]):
    """Creates new Aliens from a given list

    :param aliens: list[tuple[int, int]] - list of tuples that represents new Aliens and their coordinates
    :return: list[Alien] - list of the created Aliens
    """
    return [Alien(x_coord, y_coord) for x_coord, y_coord in aliens]
