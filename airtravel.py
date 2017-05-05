
class Flight:

    def __init__(self, number, aircraft):
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]
    
    def number(self):
        return self._number

    def airline(self):
        return self_number[:2]

    def aircraft_model():
        return self._aircraft.model()

    def _parse_seat(self, seat):
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid set row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))
        
        return (row, letter)

    def allocate_seat(self, seat, passenger):
        row, letter = self._parse_seat(seat)
        print(row, letter)
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        
        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to rellocate in seat {}".fomat(from_seat))
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError

class Aircraft:
        def __init__(self, registration, model, num_rows, num_seats_per_row):
            self._registration = registration
            self._model = model
            self._num_rows = num_rows
            self._num_seats_per_row = num_seats_per_row

        def registration(self):
            return self._registration

        def model(self):
            return self._model

        def seating_plan(self):
            return (range(1, self._num_rows + 1), "ABCDEFGHK"[:self._num_seats_per_row])


def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A320", 30, 6))
    f.allocate_seat("12A", "Cookie")
    f.allocate_seat("15F", "Bing")
