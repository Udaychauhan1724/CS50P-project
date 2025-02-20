from project import find, find_neighbours, traverse, maze
from unittest import mock
import curses

def test_find():

    # starting position "O"
    assert find(maze, "O") == (0, 1)

    # target position "X"
    assert find(maze, "X") == (8, 7)

    # Element not found
    assert find(maze, "Z") is None

def test_find_neighbours():

    # cell in the middle
    assert set(find_neighbours(maze, 4, 4)) == {(3, 4), (5, 4), (4, 3), (4, 5)}

    # cell at the edge
    assert set(find_neighbours(maze, 0, 0)) == {(0, 1), (1, 0)}

    # cell at the corner
    assert set(find_neighbours(maze, 0, 8)) == {(0, 7), (1, 8)}



def test_traverse():
    stdscr = mock.Mock()
    curses.color_pair = mock.Mock(side_effect=lambda x: x)

    # Mock the stdscr object for testing
    path = traverse(maze, stdscr)
    expected_path = [
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), 
        (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (8, 7)
    ]
    assert path == expected_path
