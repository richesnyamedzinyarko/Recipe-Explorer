#Step 1

pasta = ("Pasta Arrabiata", "Italian", 20 , "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")

print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

#Stap 2-Nested tuples and slicing
all_recipes = (pasta, biryani)

print("\nFirst recipe name: ", all_recipes [0][0])
print("\nSecond recipe name time: ", all_recipes [1][2],"mins")
print("\nPasta details (sliced): ", all_recipes[0] [0:3])

#Step 3 Itrate through a tuple
print("/nPasta Recipe deatils")
for detail in pasta:
    print("-",detail)
    print("*",detail)

    #Step 4 : Creating sets for Ingredients
    pasta_Ingredients = { "tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
    biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
    print("\nPasta INgredients: ", pasta_Ingredients )
    print("\n Biryani INgredients: ",biryani_ingredients )
    print("\n  TotalBiryani INgredients: ", len(biryani_ingredients ))

#Step 5
pasta_Ingredients.add ("paramesan")
pasta_Ingredients.discard ("chilli")
print("\n Updated pasta ingredients:", pasta_Ingredients)
        