class Customer:
    def __init__(self, id, name, ticket_obj):
        self.id = id
        self.name = name
        self.ticket = ticket_obj


class Ticket:
    def __init__(self, time, movie_obj, seat_obj, screen_obj):
        self.time = time
        self.movie = movie_obj
        self.seat = seat_obj
        self.screen = screen_obj


class Seat:
    def __init__(self, seat_no, screen_obj):
        self.seat_no = seat_no
        self.screen = screen_obj


class Screen:
    def __init__(self, location, movie_obj):
        self.location = location
        self.seat = []
        self.movie = movie_obj

    def screen_has_seat(self, seat_obj):
        self.seat.append(seat_obj)


class Movie:
    def __init__(self, name, language, price):
        self.name = name
        self.language = language
        self.price = price


bahubali = Movie('Bahubali', 'Telugu', 300)
banglore = Screen('Bangalore', bahubali)
seat_obj = Seat(10,banglore)
ticket_obj = Ticket('3PM', bahubali, seat_obj, banglore)
customer_obj = Customer(1,'Samarth', ticket_obj)

banglore.screen_has_seat(seat_obj)

print(f"Customer Name: {customer_obj.name}")
print(f"Ticket Number: {customer_obj.ticket.seat.seat_no}")
print(f"Movie Name: {customer_obj.ticket.movie.name}")
print(f"Screen name: {customer_obj.ticket.screen.location}")
print(f"Timing: {customer_obj.ticket.time}")

