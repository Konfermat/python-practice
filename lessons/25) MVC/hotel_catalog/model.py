

class Hotel:
    def __init__(self, name, city, rating, price, available=True):
        self.name = name
        self.city = city
        self.rating = rating
        self.price = price
        self.available = available
    def __str__(self):
        status = 'Доступен' if self.available else 'Забронирован'
        return f'{self.name} ({self.city}) | Рейтинг: {self.rating}/5 | Цена: {self.price:.2f} | Статус: {status}'

class HotelCatalog:
    def __init__(self):
        self._hotels = [
            Hotel("Grand Plaza", "Москва", 5, 150.00),
            Hotel("Cozy Inn", "Санкт-Петербург", 3, 75.50),
            Hotel("Sunset View", "Сочи", 4, 120.00),
            Hotel("Budget Stay", "Москва", 2, 50.00, available=False),
        ]
    def get_all_hotels(self):
        return self._hotels
    def find_hotels_by_city(self, city):
        search_city = city.lower()
        return [h for h in self._hotels if h.city.lower() == search_city]
    def book_hotel(self, hotel_name):
        for h in self._hotels:
            if h.name.lower() == hotel_name.lower() and h.available:
                h.available = False
                return True
        return False

