# list datastructure
my_list=["Toyota","Mercedez" , "BMW" , "subaru"]
my_list.append("Mazda")
print(my_list)
print(my_list[0])
my_list[2]="BMW" # mutable
print(my_list[2],"is manufactured in Germany")

my_goodies=["2", "3" , "5", "7"]
my_goodies.insert(2, "34")
print(my_goodies)

# tuple datastructure
my_tuple=("Apple" , "Mango" , "Guava" , "Melon")
print(my_tuple)
print(my_tuple[0],"i love eating them")

# set datastructure
my_set={"Jamaica" , "Kenya" , "Egypt" , "Dubai"}
print(my_set)

# dictionaries datastructure
my_dict={"name":"Michael","Age":18,"Gender":"Male","Hobby":"swimming"}
print(my_dict)
print(my_dict["Age"])
print(my_dict["Gender"])
print(f"My name is Michael am 18 yrs old{my_dict}")
my_dict={"Pet":"Dog","Name":"Tarzan","Type":"Caucasian","Age":"8 mnths"}
print(my_dict)
print(f"My pet is a dog called Tarzan a caucasian type which is 8 months old{my_dict}")