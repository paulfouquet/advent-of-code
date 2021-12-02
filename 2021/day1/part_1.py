report = []
with open("input") as file:
    while (line := file.readline().rstrip()):
        report.append(int(line))

n_increase = 0
for i in range(1, len(report)):
    if report[i] > report[i-1]:
        n_increase = n_increase + 1

print(n_increase)
