# Author: Riley Rabelos
# GitHub User: rabelosr20
# Date: 03/11/2021
# Description: This program is a ship game where two players place as many ships as they want
#     on a 10 by 10 grid and then take turns firing torpedoes at each other's grids trying to hit and
#     then sink the others ship. Once the one player has sunk all the other players ships then the game
#     has been won.


class ShipGame:
    """
    Represents a ship game object where two players place ships on a grid and then take turns firing
    torpedoes at each others grids trying to hit and then sink the others ships
    """

    def __init__(self):
        """
        Creates a ship game object, it does not take any parameters and it initializes the current state of the game
        to unfinished, the current player to first, the number of ships for both to 0, and creates an empty ship
        dictionary for each player
        """
        self._current_state = "UNFINISHED"
        self._current_player = "first"
        self._first_num_of_ships = 0
        self._sec_num_of_ships = 0
        self._first_ship_dict = {}
        self._sec_ship_dict = {}

    def place_ship(self, player, ship_length, coordinate, ship_orientation):
        """
        In this method each player will place their ships at a specific coordinate and it will first check if their
        placement is valid, if it is not it will return false. If it is it will add the coordinates to a list
        within the player dictionary and return true. Takes parameters for player, ship length, coordinate, and
        ship orientation.
        """
        if self.check_if_ship_valid(player, ship_length, coordinate, ship_orientation) is True:
            if player == "first":
                self._first_num_of_ships += 1
                self._first_ship_dict[self._first_num_of_ships] = []
                letter = coordinate[0]
                ship_coord = int(coordinate[1])
                for num in range(ship_length):
                    if ship_orientation == "R":
                        self._first_ship_dict[self._first_num_of_ships].append(str(letter) + str(ship_coord))
                        ship_coord += 1
                    elif ship_orientation == "C":
                        self._first_ship_dict[self._first_num_of_ships].append(str(letter) + str(ship_coord))
                        letter = chr(ord(letter) + 1)
                return True

            if player == "second":
                self._sec_num_of_ships += 1
                self._sec_ship_dict[self._sec_num_of_ships] = []
                letter = coordinate[0]
                ship_coord = int(coordinate[1])
                for num in range(ship_length):
                    if ship_orientation == "R":
                        self._sec_ship_dict[self._sec_num_of_ships].append(str(letter) + str(ship_coord))
                        ship_coord += 1
                    elif ship_orientation == "C":
                        self._sec_ship_dict[self._sec_num_of_ships].append(str(letter) + str(ship_coord))
                        letter = chr(ord(letter) + 1)
                return True
        else:
            return False

    def check_if_ship_valid(self, player, ship_length, coordinate, ship_orientation):
        """
        This method checks to see if the placement of the ship by the player is valid, it checks to see if the ships is
        too long or if it will overlap with another ship. If the ship is valid it will return true if not it will
        return false. Takes parameters for player, ship length, coordinate, and ship orientation. This is used by
        the place_ship method.
        """
        ship_coord = int(coordinate[1])
        letter = ord(coordinate[0])
        if ship_length < 2:
            return False
        if ship_orientation == "R":
            if ship_length + ship_coord > 11:
                return False

        if ship_orientation == "C":
            if ship_length + letter > 75:
                return False

        letter = coordinate[0]
        ship_coord = int(coordinate[1])
        if player == "first":
            for num in range(ship_length):
                for value in self._first_ship_dict.values():
                    for coord in value:
                        if str(letter) + str(ship_coord) == coord:
                            return False
            return True

        if player == "second":
            for num in range(ship_length):
                for value in self._sec_ship_dict.values():
                    for coord in value:
                        if str(letter) + str(ship_coord) == coord:
                            return False
            return True

    def get_current_state(self):
        """Returns current state of the game"""
        return self._current_state

    def fire_torpedo(self, player, coordinate):
        """
        In this method players take turns firing torpedoes at one another. First it checks to see if the torpedo
        fired is valid if not it will return false otherwise it will return true.
        If the shot is valid it will then go through their dictionary and check if there is a ship at that
        coordinate and if there is it will remove it from the list within
        the dictionary. If the list is empty then the ship has sunk. It then checks to see if the player has any
        remaining ships. If the player does not then the current state of the game is changed to the winner. Takes
        as parameters the player and the coordinate.
        """
        if self.check_if_torpedo_valid(player) is True:
            if player == "first":
                for value in self._sec_ship_dict.values():
                    for coord in value:
                        if coordinate == coord:
                            value.remove(coord)
                            if len(value) == 0:
                                self._sec_num_of_ships -= 1
                                if self._sec_num_of_ships == 0:
                                    self._current_state = "FIRST_WON"
                                    return True
                            else:
                                self._current_player = "second"
                                return True
                        else:
                            continue
                self._current_player = "second"
                return True

            if player == "second":
                for value in self._first_ship_dict.values():
                    for coord in value:
                        if coordinate == coord:
                            value.remove(coord)
                            if len(value) == 0:
                                self._first_num_of_ships -= 1
                                if self._first_num_of_ships == 0:
                                    self._current_state = "SECOND_WON"
                                    return True
                            else:
                                self._current_player = "first"
                                return True
                        else:
                            continue
            self._current_player = "first"
            return True
        else:
            return False

    def check_if_torpedo_valid(self, player):
        """
        This method is used to check if the torpedo fired is valid. If it is valid it returns true if it is not it
        returns false. Takes player as a parameter. It is used by the fire torpedo class.
        """
        if player != self._current_player:
            return False
        elif self._current_state != "UNFINISHED":
            return False
        else:
            return True

    def get_num_ships_remaining(self, player):
        """
        Returns the number of ships that are remaining for each player. Takes player as a parameter.
        """
        if player == "first":
            return self._first_num_of_ships
        else:
            return self._sec_num_of_ships


new_game = ShipGame()
print(new_game.place_ship("first", 3, "A1", "C"))
print(new_game.place_ship("second", 2, "A1", "C"))
print(new_game.place_ship("second", 3, "A1 ", "R"))
print(new_game.place_ship("first", 3, "A1", "C"))
