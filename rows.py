with open("rows.txt") as file:
    control_sum = 0
    lines = file.readlines()
    for line in lines:
        line_list = []
        for elem in line.split():
            elem = int(elem)
            line_list.append(elem)
            maxi = max(line_list)
            mini = min(line_list)
            diff = maxi - mini
        control_sum = control_sum + diff
    print(f"Suma kontrolna wynosi {control_sum}")

