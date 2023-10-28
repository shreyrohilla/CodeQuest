import sys
import re
no_of_test_cases = int(sys.stdin.readline().rstrip())
# print (no_of_test_cases)

for i in range (no_of_test_cases):
    no_of_ships = int( sys.stdin.readline().rstrip())
    # print (no_of_ships)

    list_of_all_ships_info = []

    for i in range(no_of_ships):
        ship_info = str(sys.stdin.readline().rstrip())
        # print (ship_info)

        ship_info = re.split('[_:,]', ship_info)        
        # print (ship_info)

        sname = ship_info[0]
        # print(sname)
        
        sclass = ship_info[1]
        # print(sclass)

        s_x_coord = int(ship_info[2])
        # print(s_x_coord)

        s_y_coord = int(ship_info[3])
        # print(s_y_coord)

        new_ship_info = [sname, sclass, s_x_coord, s_y_coord, 'A']

        list_of_all_ships_info.append(new_ship_info)

    # print(list_of_all_ships_info)

    for i in range(len(list_of_all_ships_info)):
        list_of_all_ships_info.sort(key = lambda x: (x[4], x[2], -x[3]))
        #print (list_of_all_ships_info)
        ship_info = list_of_all_ships_info[0]
        ship_info[4] = 'D'
        # print(i)
        print (f'Destroyed Ship: {ship_info[0]} xLoc: {ship_info[2]}')
        for j in range(len(list_of_all_ships_info)):
            ship_info = list_of_all_ships_info[j]
            if ship_info[1] == 'A':
                ship_info[2] = ship_info[2] - 10
            elif ship_info[1] == 'B':
                ship_info[2] = ship_info[2] - 20
            elif ship_info[1] == 'C':
                ship_info[2] = ship_info[2] - 30
