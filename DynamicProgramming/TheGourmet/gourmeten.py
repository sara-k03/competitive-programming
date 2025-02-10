# M minutes to eat (first line)
# Restaurant offers N different courses (number of courses)
# Each following line is the time it takes to eat a serving of each dish 

mins_to_eat = int(input())
num_courses = int(input())

course_times = []
for i in range(num_courses):
    course_times.append(int(input()))

dp = [0] * (mins_to_eat + 1) # arr -> num minutes 
dp[0] = 1

for i in range(1, mins_to_eat + 1):
    for j in course_times:
        if i - j >= 0:
            dp[i] += dp[i - j]

print(dp[mins_to_eat])
