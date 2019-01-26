#sort_cities.py
#Aadil Islam
#February 25, 2018

from city import*
from quicksort import*

def main():

    in_file = open("data/world_cities.txt", "r")

    # create arrays to hold references, one for each file to be created after sorting
    references = []
    refs1 = []
    refs2 = []
    refs3 = []

    # cycle through every line of file
    for line in in_file:

        # split line into terms
        clauses = line.strip().split(",")

        # add City object to array
        references.append(City(str(clauses[0]), str(clauses[1]), str(clauses[2]), int(clauses[3]), float(clauses[4]), float(clauses[5])))

    # separate references for each file
    refs1 = references[:]
    refs2 = references[:]
    refs3 = references[:]

    in_file.close()

    # sort each reference list appropriately
    sort(refs1,"city_name")
    sort(refs2, "city_population")
    sort(refs3, "city_latitude")

    # create new file to output to
    out_file1 = open("data/cities_alpha.txt","w")
    out_file2 = open("data/cities_population.txt", "w")
    out_file3 = open("data/cities_latitude.txt", "w")

    # cycle through array of references
    for i in range(len(refs1)):

        #output every City object, add new line appropriately
        out_file1.write(str(refs1[i]))
        if i != len(refs1)-1:
            out_file1.write("\n")

    out_file1.close()

    for i in range(len(refs2)):

        #output every City object, add new line appropriately
        out_file2.write(str(refs2[i]))
        if i != len(refs2)-1:
            out_file2.write("\n")

    out_file2.close()

    for i in range(len(refs3)):

        #output every City object, add new line appropriately
        out_file3.write(str(refs3[i]))
        if i != len(refs3)-1:
            out_file3.write("\n")

    out_file3.close()

main()