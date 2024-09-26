from city import City

class Salesman:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y
        self.current_distance = 0
        self.visited_city: list[City] = []
        
    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self):
        num_of_city = len(self.visited_city)
        if num_of_city != 0:
            return self.visited_city[num_of_city-1].x, self.visited_city[num_of_city-1].y
        return self.x, self.y
    
    def visit(self, city):
        self.visited_city.append(city)