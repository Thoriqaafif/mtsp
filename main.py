import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import math
from salesman import Salesman
from city import City

# Define a function to be called when the button is clicked
def next_step():
    # get highest relative distance
    # visit pair of salesman and city with highest relative distance
    
    # plot cities and salesman with next state
    plot_cities()
    plot_salesman()
    plt.show()
    
def relative_distance(salesman: Salesman, city: City):
    xs, ys = salesman.get_position()
    xc, yc = city.get_position()
    return

# function to get distance for 2 points
def distance_to_city(salesman: Salesman, city: City) -> float:
    x1, y1 = salesman.get_position()
    x2, y2 = city.get_position()
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# Plot salesmans    
def plot_salesman(salesmans: list[Salesman]):
    salesmans_x = [s.x for s in salesmans]
    salesmans_y = [s.y for s in salesmans]
    ax.scatter(salesmans_x, salesmans_y, color='red', marker='o', label='Data Points')
    for s in salesmans:
        ax.text(s.x, s.y-0.3, s.name, ha='center', va='top')
        for c in s.visited_city:
            ax.plot([s.x, c.x], [s.y, c.y], color='red', linestyle='-', linewidth=2)
    
# Plot cities
def plot_cities(cities: list[City]):
    unvisited_cities = [c for c in cities if c.is_visited == False]
    unvisited_cities_x = [c.x for c in unvisited_cities]
    unvisited_cities_y = [c.y for c in unvisited_cities]
    ax.scatter(unvisited_cities_x, unvisited_cities_y, color='green', marker='o')
    for c in unvisited_cities:
        ax.text(c.x, c.y-0.3, c.name, ha='center', va='top')
    visited_cities = [c for c in cities if c.is_visited == True]
    visited_cities_x = [c.x for c in visited_cities]
    visited_cities_y = [c.y for c in visited_cities]
    ax.scatter(visited_cities_x, visited_cities_y, color='red', marker='o')
    for c in visited_cities:
        ax.text(c.x, c.y-0.3, c.name, ha='center', va='top')

def visit_city(salesman: Salesman, city: City):
    salesman.visited_city.append(city)
    city.is_visited = True
    
    # evaluate distances
    evaluate_distance()
        
def evaluate_distance() -> dict[str, dict[str, float]]:
    distances: dict[str, dict[str, float]] = {}
    
    for s in salesmans:
        distances[s.name] = {}
        for c in cities:
            dist = distance_to_city(s, c)
            distances[s.name][c.name] = dist
            
    # get total Mi
    for c in cities:
        total = 0.0
        for s in salesmans:
            total += distances[s.name][c.name]
        distances["total"][c.name] = total
    return distances
        
def init_data() -> tuple[list[Salesman], list[City]]:
    salesmans: list[Salesman] = [
        Salesman("1", 2, 0),
        Salesman("2", 8, 0),
        Salesman("3", 5, 8),
    ]
    cities: list[City] = [
        City("V", 1, 2),
        City("W", 2, 4),
        City("X", 4, 6),
        City("Y", 8, 4),
        City("Z", 9, 2),
    ]

    return salesmans, cities

def init_plot():
    # init matplotlib
    fig, ax = plt.subplots()
    plt.xlim(0, 10)
    plt.ylim(-2, 10)

    ax.set_title('Scatter Plot with Button')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    # Create a button
    button_ax = plt.axes((0.8, 0.01, 0.1, 0.05))  # Position: [left, bottom, width, height]
    button = Button(button_ax, 'Next')

    # Connect the button to the function
    button.on_clicked(lambda event: next())
    
    return fig, ax

if __name__ == '__main__':
    salesmans: list[Salesman] = []
    cities: list[City] = []
    distances: dict[str, dict[str, float]] = {}
    
    salesmans, cities = init_data()
    distances = evaluate_distance()
    fig, ax = init_plot()
    
    visit_city(salesmans[0], cities[0])
    # plot salesmans and cities
    plot_salesman(salesmans)
    plot_cities(cities)

    # Show the plot
    plt.show()