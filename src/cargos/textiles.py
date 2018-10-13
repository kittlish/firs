from cargo import Cargo

cargo = Cargo(id='textiles',
              type_name='string(STR_CARGO_NAME_TEXTILES)',
              unit_name='string(STR_CARGO_NAME_TEXTILES)',
              type_abbreviation='string(STR_CID_TEXTILES)',
              sprite='NEW_CARGO_SPRITE',
              weight='0.5',
              cargo_payment_list_colour='194',
              is_freight='1',
              cargo_classes='bitmask(CC_EXPRESS)',
              cargo_label='TEXT',
              town_growth_effect='TOWNGROWTH_WATER',
              town_growth_multiplier='1.0',
              units_of_cargo='80',
              items_of_cargo='string(STR_CARGO_UNIT_TEXTILES)',
              penalty_lowerbound='10',
              single_penalty_length='64',
              price_factor='166',
              capacity_multiplier='2',
              icon_indices=(5, 0))
