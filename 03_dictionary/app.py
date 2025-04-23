# ye aiek dictionary hai jis mai key aur is ki value hai
chai_Types = {"Masala" : "Spicy", "Ginger" : "Sweet", "Lemonade" : "Sour"}

# agar hamain key ki value chahiye to hamain is tarah se likhna paray ga
# print(chai_Types["Masala"]) # Spicy

# agar value aur key add krne hooo
# chai_Types["Mint"] = "Fresh"
# print(chai_Types) # {'Masala': 'Spicy', 'Ginger': 'Sweet', 'Lemonade': 'Sour', 'Mint': 'Fresh'}

# Loops in Dictionary

# isme loop chalay ga aur key aur srf key aege yani masala ginger lemonade mint
# for chai in chai_Types:
#     print(chai) # Masala Ginger Lemonade Mint

# isme loop chalay ga aur key aur value dono aege 
# for chai in chai_Types:
#     print(chai, chai_Types[chai]) # Masala Spicy Ginger Sweet Lemonade Sour Mint Fresh

# isse bh key aur value dono aege ya opper wala kelo ya ye
# for key, value in chai_Types.items():
#     print(key, value) # Masala Spicy Ginger Sweet Lemonade Sour Mint Fresh
    
# ham condition laga kr question kr saktein hain ka ye cheez hai tou ye kar do
# if "Masala" in chai_Types:
#     print("Masala chai is available") # Masala chai is available

# isse length maloom ki ja sakte ha
# print(len(chai_Types)) # 4

# ham apne dictionary se kse bhi key or iski value ko delete kar sakte hain
# chai_Types.pop("Masala") # isse masala chai delete ho jayegi
# print(chai_Types) # {'Ginger': 'Sweet', 'Lemonade': 'Sour', 'Mint': 'Fresh'}

# isse bh hm apne dictionary se kse sab se akher ki key or iski value ko delete kar sakte hain
# chai_Types.popitem() 
# print(chai_Types) 

# isse ham apne dictionary se kse bhi key or iski value ko delete kar sakte hain
# del chai_Types["Ginger"]
# print(chai_Types) 

# isse ham apne dictionary ki copy bana sakte hain
# chai_Types_Copy = chai_Types.copy()

# ye ham ne aiek new dictionary banai hai jisme tea_Shop hai
tea_Shop = {
    "chai" : {"Masala" : "Spicy", "Ginger" : "Sweet", "Lemonade" : "Sour"},
    "pastry" : {"Chocolate" : "Sweet", "Vanilla" : "Sweet", "Strawberry" : "Sweet"},
}

# print(tea_Shop) 

# isse ham dictionary ki key or uski value ko print kar sakte hain
# print(tea_Shop["chai"])

# ab ham ne upper aiek key ka andar value de the or uski value ka anadar nhi key or value de the ab hamain usko print krna hai
# print(tea_Shop["chai"]["Masala"]) 

#  ham number ko square krwa saktein hain loop laga kr
# squared_numbers = {x: x**2 for x in range(6)}
# print(squared_numbers) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# or agar is squarerd_numbers ko clear krke empty karna hai tou
# squared_numbers.clear() 
# print(squared_numbers) # {}

# ab ham ne aiek list banaenge or aiek variable gool ye hai us list ko dictionary bana hai key hogi hamare list or value hogi iski default varaiable
# keys = ["Masala", "Ginger", "Lemonade"]
# default_value = "Spicy"
# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict) # {'Masala': 'Spicy', 'Ginger': 'Spicy', 'Lemonade': 'Spicy'}

# agar ham chahtain hain ka jsse masla key ho or uski value keys ki list ho tou
# keys = ["Masala", "Ginger", "Lemonade"]
# new_dict = dict.fromkeys(keys, keys)
# print(new_dict) # {'Masala': ['Masala', 'Ginger', 'Lemonade'], 'Ginger': ['Masala', 'Ginger', 'Lemonade'], 'Lemonade': ['Masala', 'Ginger', 'Lemonade']}
