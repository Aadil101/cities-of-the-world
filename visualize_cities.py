#visualize_cities.py
#Aadil Islam
#February 25, 2018

from cs1lib import *
from city import *
from quicksort import *

in_file = open("data/world_cities.txt", "r")

# list to hold references for sorting
refs2 = []

for line in in_file:
    # split line into terms
    clauses = line.strip().split(",")

    # add City object to array
    refs2.append(City(str(clauses[0]), str(clauses[1]), str(clauses[2]), int(clauses[3]), float(clauses[4]), float(clauses[5])))

in_file.close()

# sort cities by population
sort(refs2, "city_population")

# list to hold cities that will be printed on map (1 more will be added every second)
map_cities = []

# number of cities counter (to be used in start_graphics)
i = 0

def graphics():

    global i

    # draw map
    clear()
    img = load_image("data/blankMapOfworld.png")
    draw_image(img, 0, 0)

    # set red fill color
    set_fill_color(1, 0, 0)

    # as long as there are not 50 cities on the map yet...
    if len(map_cities) < 50:

        # add one more city each second (note framerate in start_graphics is only at 1!)
        map_cities.append(refs2[i])
        i += 1

    # draw current cities in map_cities list
    for j in range(len(map_cities)):
        draw_circle(2 * refs2[j].long + 360, -(2 * refs2[j].lat) + 180, 3)

start_graphics(graphics, width=720, height=360, framerate=1)