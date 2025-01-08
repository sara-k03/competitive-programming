from math import sqrt

def distance(x1, y1, x2, y2):
    x_part = (x2 - x1)**2
    y_part = (y2 - y1)**2
    final = sqrt(x_part + y_part)
    return final

while True:
    case = input().split()
    fighting_distance = float(case[0])
    number_of_hives = int(case[1])

    if (fighting_distance == 0.0):
        break

    positions = []
    for i in range(number_of_hives):
        pos = list(map(float, input().split()))
        positions.append(pos)

    sour_hives = set()
    
    for i in range(0, len(positions) - 1):
        x1 = positions[i][0]
        y1 = positions[i][1]
        for j in range(i + 1, len(positions)):
                x2 = positions[j][0]
                y2 = positions[j][1]
                if distance(x1, y1, x2, y2) < fighting_distance:
                    sour_hives.add(i)
                    sour_hives.add(j)
    
    sour = len(sour_hives)
    sweet = number_of_hives - sour
    print(sour, "sour,", sweet, "sweet")