from Airtravel import Flight,Aircraft,console_card_printer,make_flights
from pprint import pprint as pp

""" """
# objf=Flight("SN060")
# # print(type(objf))
# # objf.number() is same as Flight.number(objf)
# print(objf.number())

""" """
# objf=Flight("SE0600")

# print (objf.number())


# num_rows=5
# num_seats_per_row=5
# print((range(1,num_rows+1),"ABCDEFGHJ"[:num_seats_per_row]))


# obja=Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
# print(obja.registration())

# print(obja.model())
objf=Flight("BA758",Aircraft("G-EUPT","Airbus A319",num_rows=22,num_seats_per_row=6))


# print(objf.aircraft_model())

objf.allocate_seat("12A","ross portarico")
objf.allocate_seat("22A","Gani")
objf.allocate_seat("02A","Gani")
# pp(objf._seating)
# objf.relocate_passenger("12A","12B")
# pp(objf._seating)
# print(objf.num_available_seats())
objf.make_boarding_cards(console_card_printer)

f,g=make_flights()

print(f.aircraft_model())

