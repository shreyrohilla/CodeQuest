import sys

no_of_test_cases = int(sys.stdin.readline().rstrip())
# print (no_of_test_cases)

for i in range (no_of_test_cases):
    planet_info = (sys.stdin.readline().rstrip().split())
    # print (planet_info)

    p_temp = float(planet_info[0])
    p_water = planet_info[1]
    p_mfield = planet_info[2]
    p_orbit = float(planet_info[3])

    # new_planet_info = [p_temp, p_water, p_mfield, p_orbit]
    # print (new_planet_info)

    if p_temp > 100:
        print ("The planet is too hot.")
    elif p_temp < 0:
        print ("The planet is too cold.")
    elif p_water != "true":
        print ("The planet has no water.")
    elif p_mfield != "true":
        print ("The planet has no magnetic field.")
    elif p_orbit > 0.6:
        print ("The planet's orbit is not ideal.")
    else:
        print ("The planet is habitable.")


