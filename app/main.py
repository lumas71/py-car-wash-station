class Car:
    def __init__(self, comfort_class:int, clean_mark:int, brand:str):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power:int, average_rating: float, count_of_ratings: int):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, car_list: list):
        service_income = 0
        for car in car_list:
           if car.clean_mark < self.clean_power:
               service_income += self.calculate_washing_price(car)
        return service_income

    def calculate_washing_price(self, car: Car):
        return round(
        car.comfort_class * (self.clean_power - car.clean_mark)
        * (self.average_rating / self.distance_from_city_center), 1)

    def wash_single_car(self, car: Car):
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power
        return car.clean_mark

    def rate_service(self, rating:float):
        self.count_of_ratings += 1
        self.average_rating = round((self.average_rating + rating / self.count_of_ratings), 1)


pinky_cars = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=3.9,
    count_of_ratings=11
)

bmw = Car(comfort_class=3, clean_mark=3, brand='BMW')
audi = Car(comfort_class=4, clean_mark=2, brand='Audi')

print(f"income = {pinky_cars.serve_cars([bmw, audi])}")
pinky_cars.rate_service(5)

