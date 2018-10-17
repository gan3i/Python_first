"""model for aircraft flights"""
"""method or functions, fuctions are objects"""
# class Flight:

#     def __init__(self,number):
#         self._number=number #"_number is a object attribute , we don't have to declare them before we create them"

#     def number(self):
#         return self._number
""" """
class Flight:
    """A flight with a perticular passenger aircraft"""

    def __init__(self,number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not (number[2:].isdigit() and len(number[2:])<=4):
            raise ValueError("Invalid route numberr '{}".format(number))
        self._number=number
        self._aircraft=aircraft
        rows, seats=self._aircraft.seating_plan()
        self._seating=[None]+[{letter:None for letter in seats} for _ in rows]# produces list of set of dictionaries
        # [{'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
        # {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
        # {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
        # {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None},
        # {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]
# Instance method
    def aircraft_model(self):
        return self._aircraft.model()
# Method
    def allocate_seat(self, seat, passenger):
        """allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or "21F"

        Raises:
            Valueerror is the seat is nor avialble
         """
        row,letter=self._parse_seat(seat)
        
        
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter]=passenger

    def relocate_passenger(self,from_seat,to_seat):
        """Relocate a passenger to a different seat

        Args:
            from_seat:the existing seat designator for the passenger to be moved.

            to_seat: the new seat designator.
        """
        from_row,from_letter=self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seatt {}".format(from_seat))

        to_row,to_letter=(self._parse_seat(to_seat))
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(to_seat))

        self._seating[to_row][to_letter]=self._seating[from_row][from_letter]
        self._seating[from_row][from_letter]=None

    def  _parse_seat(self,seat):

        _, seat_letters=self._aircraft.seating_plan()

        letter =seat[-1]
        if letter not in  seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_num=seat[:-1]
        try:
            row=int(row_num)
        except ValueError:
            raise ValueError("Invalid Row Number {}".format(row_num))

        return row, letter

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                        for row in self._seating
                        if row is not None)

    def make_boarding_cards(self,card_printer):
        for passenger, seat in sorted(self.passenger_seats()):
            card_printer(passenger,seat, self.number(),self.aircraft_model())

    def passenger_seats(self):#generator function
        """An iterable series of passenger seating"""
        row_num, seat_letters=self._aircraft.seating_plan();
        for row in row_num:
            for letter in seat_letters:
                passenger =self._seating[row][letter]
                if passenger is not None:
                    yield (passenger,"{}{}".format(row,letter))

# class Aircraft:

#     def __init__(self, registration, model, num_rows, num_seats_per_row):
#         self._registration=registration
#         self._model=model
#         self._num_rows=num_rows
#         self._num_seats_per_row=num_seats_per_row

#     def registration(self):
#         return self._registration

#     def model(self):
#         return self._model

#     def seating_plan(self):
#         return (range(1,self._num_rows+1),
#                 "ABCDEFGHJ"[:self._num_seats_per_row]) #GET A TUPLE OF ROW NUMBER AND SEAT NUMBER

class Aircraft:

    def num_seats(self):
        rows,row_seats=self.seating_plan()
        return len(rows)*len(row_seats)

    def registration(self):
       return self._registration

class Airbus319(Aircraft):

    def __init__(self,registration):
        self._registration=registration
    
    # def registration(self):
    #    return self._registration

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23),"ABCDEF"

    # def num_seats(self):
    #     rows,row_seats=self.seating_plan()
    #     return len(rows)*len(row_seats)

class Boeing777(Aircraft):
    
    def __init__(self,registarion):
        self._registration=registarion

    # def registration(self):
    #    return self._registration

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
            #for simplicity sake we ignore the complex
            #seating arrangement for first class
            return range(1,56),"ABCDEF"

    # def num_seats(self):
    #     rows,row_seats=self.seating_plan()
    #     return len(rows)*len(row_seats)



# def make_flight():
#     f=Flight("BA758", Aircraft("E-Gut","Airbus A319", num_rows=22,num_seats_per_row=6))
#     f.allocate_seat("12A","Barito")
#     f.allocate_seat("15B","John")
#     f.allocate_seat("13C","Kerry")
#     f.allocate_seat("14D","Ken Munday")


def make_flights():
    f=Flight("BA758", Boeing777("E-EUPT"))
    f.allocate_seat("12A","Barito")
    f.allocate_seat("15B","John")
    f.allocate_seat("13C","Kerry")
    f.allocate_seat("14D","Ken Munday")

    g=Flight("BA758", Airbus319("F-GSPS"))
    g.allocate_seat("12A","Barito")
    g.allocate_seat("15B","John")
    g.allocate_seat("13C","Kerry")
    g.allocate_seat("14D","Ken Munday")
    return f,g



def console_card_printer(passenger, seat , flight_number, aircraft):
    output="| Name: {0}"      \
            " Flight: {1}"    \
            " Seat: {2}"      \
            " Aircraft: {3}"  \
            " |".format(passenger,flight_number,seat,aircraft)
            
    banner="+" + "-" * (len(output)-2) + "+"
    border="|" + " " * (len(output)-2) + "|"
    lines =[banner, border, output,border,banner]
    card="\n".join(lines)
    print(card)
    print()


