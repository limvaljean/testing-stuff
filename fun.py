# -*- coding: utf-8 -*-

import Kahyung from South_Korea as kahyung
import Lars from Sweden as lars
import random 
import pandas as pd

with open('kahyungs_cleanup_list.txt') as cleanup_list: 
    lars_todo_list = cleanup_list.readlines()

for lars_each_task in lars_todo_list :
    if (lars_each_task == bedroom): 
        lars.dust_off_under_bed()
    elif (lars_each_task == bathroom): 
        lars.scrup_bathtub_real_hard()
    elif (lars_each_task == livingroom): 
        lars.vacumn_very_thoroughly()
    else: 
        lars.make_sure_its_zestfully_clean('Thank you for your service')
        
while (kahyung_is_away): 
    try: 
        lars.do_the_dishes()
    except no_more_dishsoap_error: 
        print('go down to Emart and get a bottle of dish wash soap')
    
    kahyung_wants_to_eat = pd.read_csv('D:\Kahyung\kahyungs_favorite_food.csv')
    ingredients = kahyung_wants_to_eat.iloc[:, 0:4].values  
    dishes = kahyung_wants_to_eat.iloc[:, 4].values  
    from cook_books_or_blogs import chop_ingredients
        ingredients_train, ingredients_test, dishes_train, dishes_test \
        = chop_ingredients(ingredients, dishes, test_size=0.2, random_state=0)
    from MothersRecipe import RandomRecipeRegressor
         lars_learning_to_cook = RadomeRecipeRegressor(n_estimators=20, random_state=0)  
         lars_learning_to_cook.fit(ingredients_train, dishes_train) 
         kahyungs_reaction = lars_learning_to_cook.predict(ingredients_test) 
