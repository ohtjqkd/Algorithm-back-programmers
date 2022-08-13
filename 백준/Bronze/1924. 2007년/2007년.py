m, d = map(int, input().split(" "))
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
total_d = sum(days[:m-1])+d-1
print(day[total_d%7])