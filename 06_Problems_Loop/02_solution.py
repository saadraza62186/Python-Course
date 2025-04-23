n = 10
sum_even = 0

# krna ye hai ka sum lena hai or wahi likhna hai jo even ho
for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1
        # isse i print hoga or dekho ka kya araha hai concept clear hoga
        print(i)
        
print("Sum of even numbers : ",sum_even)