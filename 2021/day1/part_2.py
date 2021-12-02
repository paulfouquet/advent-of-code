report = []
with open("input") as file:
    while (line := file.readline().rstrip()):
        report.append(int(line))

start = 1
c_sum = 0
p_sum = report[0] + report[1] + report[2]
while start+2 < len(report):
    sum = 0
    for i in range(start, start+3):
        sum = sum + report[i]
        if i == start + 2:
            if sum > p_sum:
                c_sum = c_sum + 1
            p_sum = sum

    start = start + 1

print(c_sum)
