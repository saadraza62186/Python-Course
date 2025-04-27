# Basic Class and Object
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def full_name(self):
#         return f"{self.brand} {self.model}"        

# is me jo my_car hai wh aiek object hai or Car aiek class hai
# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)

# isme hum ne function bana kr dekha or bh fn bana sktein hain
# my_new_car = Car("Kia", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())

#           Inheritance

# Inheritence ka matlab wirasat hum inherit karahe hain yani aiek new class ka andar pehle se declared class ko inject karahe hain
# ye car ki class dalne pr hum is ka sare attribute fn or kuch bh declared kya hou tou usse access ker saktein hain
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         # asal me ham ne iss bar srf aiek he attribute yani variable lya mgr chahye brand model or batterysize tha mgr hum ne upper he brand or model declared kr dya tha tou kaam asan hogya supper() laga kr access le lya
#         self.battery_size = battery_size

# tesla = ElectricCar("Tesla", "Model X", "85KWH")
# print(tesla.brand)
# print(tesla.model)
# print(tesla.full_name())
# print(tesla.battery_size)
# # ye aiek line mai bh hoo sakta the phr bh upper line bh line print karaya hai takay yaad rahe
# print(tesla.brand, tesla.model, tesla.full_name(), tesla.battery_size)


#           Encapsulation

# iska matlab jese jab chahtain hain ka tesla.brand mai kya araha hai tou directly pata chl jata tha is process ka matlab hai usse thoda private kro har koi access ka kr ske sewaie aiek method ka jo neeche banayenge
# ye hum ne upper se copy paste kya hai agar upper wala chalana hi tou ye comment krna padega 
# class Car:
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.model = model
#     def full_name(self):
#         return f"{self.__brand} {self.model}" 
#     def get_car(self):
#         return self.__brand + "!"
        
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         # asal me ham ne iss bar srf aiek he attribute yani variable lya mgr chahye brand model or batterysize tha mgr hum ne upper he brand or model declared kr dya tha tou kaam asan hogya supper() laga kr access le lya
#         self.battery_size = battery_size

# ab hum agar dekhien tou hm electric car ki brand ko access nhi krsktein bas get_car ke zerya krsaktein hain
# my_car = ElectricCar("Tesla", "X" , "40KWH")
# print(my_car.brand)
# print(my_car.get_car())

# Polymorphism

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
#     def fuel_type(self):
#         return "Electric Charge"
    
# safari = Car("Tata", "Safari")
# print(safari.fuel_type())

# myTesla = ElectricCar("Tesla", "Model X", "30Kwh")
# print(myTesla.fuel_type())

# Count krna hai kai kitne bar car bane hai

# class Car:
#     total_car = 0
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_car += 1
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"
     
#     def fuel_type(self):
#         return "Petrol or Diesel"

# safari = Car("Toyota", "Corolla")
# safari_two = Car("Toyota", "Yaris")
# safari_three = Car("Toyota", "alto")
# safari_four = Car("Toyota", "mehrab")
# safari_five = Car("Toyota", "land")
# safari_six = Car("Toyota", "aa")
# print(Car.total_car)

# Static Method
# isse hum apne direct object ko print kara saktein hain yani Car.general_description() aese

# class Car:
#     total_car = 0
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_car += 1
        
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#     def fuel_type(self):
#         return "Petrol or Diesel"
#     # isko lagane se me direct acccess le sakta hoon yani kse variable mai stores krne ki zaroorat nhi hai
#     @staticmethod
#     def general_description():
#         return "This Car is amazing"
        
# safari = Car("Toyota", "Corolla")
# print(safari.general_description())
# print(Car.general_description())

# Decoraters
# or ab hum ko model ba access bh private krna hai
class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand} {self.__model}"
    def fuel_type(self):
        return "Petrol or Diesel"
    # hum ne upper isko private krdya tha model ko ka koi access na kr paye ap access bh tou karna hai
    @property
    def model(self):   # yahan return self.__model karna hai
        return self.__model
    
    
# isse hum kse model ko overright krahein hain
my_car = Car("Tata", "Safari")
# my_car.model = "alto"
print(my_car.model)