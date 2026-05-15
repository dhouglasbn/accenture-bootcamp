INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, resis, retreat,
    cardNumberInCollection, collection_id, type_id, stage_id
)
VALUES
(60, 'Bulbasaur', 'Seed Pokémon', 'Leech Seed', '20', 'Fire', NULL, '1', 1, 1, 1, 1),
(50, 'Charmander', 'Lizard Pokémon', 'Ember', '30', 'Water', NULL, '1', 4, 1, 2, 1),
(50, 'Squirtle', 'Tiny Turtle Pokémon', 'Bubble', '10', 'Lightning', NULL, '1', 7, 1, 3, 1),
(40, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', NULL, '1', 58, 1, 4, 1),
(40, 'Gastly', 'Gas Pokémon', 'Lick', '10', 'Psychic', NULL, '1', 33, 1, 5, 1),
(70, 'Machop', 'Superpower Pokémon', 'Low Kick', '20', 'Psychic', NULL, '1', 52, 1, 6, 1),
(120, 'Snorlax', 'Sleeping Pokémon', 'Body Slam', '30', 'Fighting', 'Psychic', '4', 11, 2, 7, 1),
(80, 'Ivysaur', 'Seed Pokémon', 'Vine Whip', '30', 'Fire', NULL, '2', 30, 1, 1, 2),
(90, 'Charmeleon', 'Flame Pokémon', 'Flamethrower', '50', 'Water', NULL, '2', 24, 1, 2, 2),
(70, 'Wartortle', 'Turtle Pokémon', 'Withdraw', '20', 'Lightning', NULL, '1', 42, 1, 3, 2),
(100, 'Venusaur', 'Seed Pokémon', 'Solar Beam', '60', 'Fire', NULL, '2', 15, 1, 1, 3),
(120, 'Charizard', 'Flame Pokémon', 'Fire Spin', '100', 'Water', NULL, '3', 4, 1, 2, 3),
(100, 'Blastoise', 'Shellfish Pokémon', 'Hydro Pump', '40+', 'Lightning', NULL, '3', 2, 1, 3, 3),
(60, 'Jigglypuff', 'Balloon Pokémon', 'Lullaby', '—', 'Fighting', 'Psychic', '1', 54, 2, 7, 1),
(70, 'Kangaskhan', 'Parent Pokémon', 'Comet Punch', '20x', 'Fighting', NULL, '3', 5, 2, 7, 1),
(90, 'Scyther', 'Mantis Pokémon', 'Slash', '30', 'Fire', 'Fighting', '1', 10, 2, 1, 1),
(80, 'Electrode', 'Ball Pokémon', 'Explosion', '80', 'Fighting', NULL, '1', 21, 2, 4, 2),
(60, 'Cubone', 'Lonely Pokémon', 'Bone Attack', '20', 'Grass', NULL, '1', 50, 3, 6, 1),
(70, 'Aerodactyl', 'Fossil Pokémon', 'Wing Attack', '30', 'Lightning', 'Fighting', '2', 1, 3, 6, 1),
(100, 'Lapras', 'Transport Pokémon', 'Water Gun', '10+', 'Lightning', NULL, '2', 10, 3, 3, 1);
