
def area_sum(rectangles):
    total_area = 0
    for r in rectangles:
        total_area += r["height"] * r["width"]
    return total_area

def main():
    rectangles = [{"height": 4, "width": 5}, {"height": 18, "width": 5}]
    print(area_sum(rectangles))
main()