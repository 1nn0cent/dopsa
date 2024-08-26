from math import pi
 
def find_farthest_orbit(list_of_orbits):
    return max([orbit for orbit in list_of_orbits if orbit[0] != orbit[1]], key=lambda x: pi * x[0] * x[1])
 
 

