def simple_area():
	side = 20
	print("AREA IS : {}".format( side*side ))

def area(side):
    print(side * side)


def get_area(side):
	area = side * side
	return area

simple_area()
area(20)

area = get_area(20)

print("Area : {}".format(area))