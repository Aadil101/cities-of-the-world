#city.py
#Aadil Islam
#February 20, 2018

class City:

    # initialize City object
    def __init__(self,country,name,region,pop,lat,long):

        self.country = country
        self.name = name
        self.region = region
        self.pop = pop
        self.lat = lat
        self.long = long

    # print string with commas, but without country and region
    def __str__(self):

        return(self.name + "," + str(self.pop) + "," + str(self.lat) + "," + str(self.long))