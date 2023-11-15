# TODO: update to create measure function

from chomp.data_manager import (
    add_food_diary_entry,
    get_food,
    FoodNotFoundException,
)


def measure(food_name, desired_calories=None):
    print(f"You would like to eat {desired_calories:.1f} {food_name}")

    try:
        food = get_food(food_name)
        food_weight = food.get_nutritional_fact("weight")
        cal = food.get_nutritional_fact("calories")
        required_weight = desired_calories * (cal / food_weight)

        print(f"To do this, you need {required_weight}g.")
    except FoodNotFoundException:
        print(f"Cannot find {food_name}!")
