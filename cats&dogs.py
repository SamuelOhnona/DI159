# Cat Years 15 cat years for first year +9 cat years for second year +4 cat years for each year after that
# Dog Years 15 dog years for first year +9 dog years for second year +5 dog years for each year after that

def calculate_cat_dog_years(human_years):

    if human_years < 1:
        return "Human years must be greater than or equal to 1."
    
    cat_years = 0
    dog_years = 0
    
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5
    
    return [human_years, cat_years, dog_years]



human_years = 10
result = calculate_cat_dog_years(human_years)
print(result) # Output: [10, 56, 64]


#human_years = 1
#result = calculate_cat_dog_years(human_years)
#print(result) # Output: [1, 15, 15]


#human_years = 2
#result = calculate_cat_dog_years(human_years)
#print(result) # Output: [2, 24, 24]