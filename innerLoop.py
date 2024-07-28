import time
current_time = time.localtime;
# print(f"Current time is {current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}")
current_time = time.time()
for i in range(10,20):
    for j in range(10,20):
        print(f"[{i}],[{j}]",end=" ")
    print()
print(f"Total time taken in Loop is {round(time.time() - current_time)} seconds")

a = isinstance("aa",str)
print(a)