from cargo import Cargo

cargo = Cargo(id = 'copper_ore',
              number = '8',
              type_name = 'TTD_STR_CARGO_PLURAL_COPPER_ORE',
              unit_name = 'TTD_STR_CARGO_SINGULAR_COPPER_ORE',
              type_abbreviation = 'TTD_STR_ABBREV_COPPER_ORE',
              sprite = 'NEW_CARGO_SPRITE',
              weight = '1.0',
              station_list_colour = '186',
              cargo_payment_list_colour = '186',
              is_freight = '1',
              cargo_classes = 'bitmask(CC_BULK)',
              cargo_label = '"CORE"',
              town_growth_effect = 'TOWNGROWTH_NONE',
              town_growth_multiplier = '1.0',
              units_of_cargo = 'TTD_STR_TONS',
              items_of_cargo = 'TTD_STR_QUANTITY_COPPER_ORE',
              penalty_lowerbound = '30',
              single_penalty_length = '255',
              price_factor = '75.4852294922',
              capacity_multiplier = '1',
              icon_indices = (1, 2))

cargo.economy_variations['FIRS']['disabled'] = True
cargo.economy_variations['BASIC_ARCTIC']['disabled'] = True
cargo.economy_variations['BASIC_TROPIC']['disabled'] = True
cargo.economy_variations['BASIC_TEMPERATE']['disabled'] = True