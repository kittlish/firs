from economy import Economy
economy = Economy(id = "EXTREME",
                  numeric_id = 2,
                  # as of May 2015 the following cargos must have fixed positions if used by an economy:
                  # passengers: 0, mail: 2, goods 5, food 11
                  # keep the rest of the cargos alphabetised
                  # bump the min. compatible version if this list changes
                  cargos = ['passengers',
                            'acid',
                            'mail',
                            'alcohol',
                            'ammonia',
                            'goods',
                            'beans',
                            'building_materials',
                            'chlorine',
                            'clay',
                            'coal',
                            'food',
                            'coffee',
                            'cotton',
                            'edible_oil',
                            'electrical_machines',
                            'engineering_supplies',
                            'ethylene',
                            'farm_supplies',
                            'flour',
                            'food_additives',
                            'fruits',
                            'furniture',
                            'grain',
                            'iron_ore',
                            'livestock',
                            'limestone',
                            'lumber',
                            'lye',
                            'milk',
                            'oil',
                            'paper',
                            'petrol',
                            'phosphate',
                            'plastic',
                            'potash',
                            'potatos',
                            'recyclables',
                            'salt',
                            'sand',
                            'scrap_metal',
                            'soda_ash',
                            'steel',
                            'sugar',
                            'sugar_beet',
                            'textiles',
                            'tin',
                            'wood',
                            'wool'])
