tea_varities = ['Green Tea', 'Black Tea', 'White Tea', 'Herbal Tea']

# isme zero index ki value aajayegi
# print(tea_varities[0])

# isme last index ki value aajayegi
# print(tea_varities[-1])

# isme 0 se lekar 2 tak ki value aajayegi
# print(tea_varities[1:3])

# isme 2 se lekar akhr tak ki value aajayegi
# print(tea_varities[:2])

# isme 2 se lekar akhr tak ki value aajayegi
# print(tea_varities[2:])

# isme index 3 pr jo value hogi wh ayegi
# tea_varities[3] = "Ginger Tea"
# print(tea_varities)

#isme 1 index value se le ker 2 index value tak ki value aayegi
# print(tea_varities[1:3])
# print(tea_varities)

#isme tea vaeities ki 1 index ki value ko chamomile tea se replace karenge or 2 index ki value ko mint tea se replace karenge
# tea_varities[1:3] = ['Chamomile Tea', 'Mint Tea']
# print(tea_varities)

# isko chala kr check karo phr smjh ayega
# print(tea_varities[1:1])
# tea_varities[1:1] = ['Chamomile Tea', 'Mint Tea']
# print(tea_varities)


# Loops in List

# isse hoga ye ka tamam values line by line print ho jayegi 
# for tea in tea_varities:
#     print(tea)

# isse hoga ye ki tamam values ek hi line me print ho jayegi or har value ke beech me - aayega
# for tea in tea_varities:
#     print(tea, end='-')

# Condition Checking in List

# isme hm ye check kar rahe hain ki kya tea_varities me Oolong Tea hai ya nahi agar nhi hoga to kuch bh nhi hoga agar hoga to print hoga
# if "Oolong Tea" in tea_varities:
#     print("Oolong is available")

# ab hm isme Oolong Tea ko add karenge agar wo list me nahi hai to    
# tea_varities.append("Oolong Tea")
# print(tea_varities)

# ab print hojayega qk oolong tea ko add kar diya hai
# if "Oolong Tea" in tea_varities:
#     print("Oolong is available")

# agar hamien list ki last value ko delete krna hoo tou pop() use krtein hain
# print(tea_varities.pop())

# agar hamien list mai se kese bh value ko delete krna hoo tou remove() use krtein hain
# print(tea_varities.remove("Herbal Tea"))
# print(tea_varities)

#agar hamien list mai kse item ko add krna hai kse bh index pr tou insert() use krtein hain iske anadar index batana hoga
# tea_varities.insert(2, "Chamomile Tea")
# print(tea_varities)

# agar ham apne list ki copy banana chahtein hain tou copy() use krtein hain phr ye copy jb bh call hogi whi print hogi jo pehle tea_variable ki value theeee
# tea_varities_copy = tea_varities.copy()