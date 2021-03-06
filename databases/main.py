#!/usr/bin/env python

import os

### parameters
mainDir = os.getcwd()
numStores = 5
chanceToBeOrganic = 30 #percent
priceVariance = 10 #percent
organicPriceMultiplier = 1.10
numIngredientsPerStore = 100
maxIngredientsPerRecipe = 10
numRecipes = 100
numIngredientsTotal = numIngredientsPerStore + numStores*20 #20 extra ingredients per store
availableIngredientsList = 'availableIngredientList.list'
recipesList = 'recipes.list'
manualIngredientsList = 'manualIngredientsList.list'
manualRecipesList = 'manualRecipesList.list'

try:
	print('\n-----Creating availble ingredient list-----\n')
	from library.modules import createAvailableIngredientList
	createAvailableIngredientList.__main__(mainDir, numIngredientsTotal, availableIngredientsList)
	print('Done')
except Exception as e:
	print('Exception found during creating ingredient list: ' + str(e))
	exit()

try:
	print('\n-----Creating store catalogs----\n')
	from library.modules import createStoreCatalog
	for i in range(numStores): createStoreCatalog.__main__(mainDir, organicPriceMultiplier, priceVariance, chanceToBeOrganic, numIngredientsPerStore, i, availableIngredientsList, ('store' + str(i) + '.store'))
	print('Done')
except Exception as e:
	print('Exception found during creating store catalogs: ' + str(e))
	exit()

try:
	print('\n-----Creating recipe catalog-----\n')
	from library.modules import createRecipeCatalog
	createRecipeCatalog.__main__(mainDir, availableIngredientsList, maxIngredientsPerRecipe, numRecipes, recipesList)
	print('Done')
except Exception as e:
	print('Exception found during creating recipe catalog: ' + str(e))
	exit()

try:
	print('\n-----Injecting manual entries-----\n')
	from library.modules import injectManualEntries
	injectManualEntries.__main__(mainDir, manualIngredientsList, manualRecipesList, availableIngredientsList, recipesList, priceVariance, organicPriceMultiplier, chanceToBeOrganic)
	print('Done')
except Exception as e:
	print('Exception found during injecting manual entries: ' + str(e))
	exit()
	

print('')
