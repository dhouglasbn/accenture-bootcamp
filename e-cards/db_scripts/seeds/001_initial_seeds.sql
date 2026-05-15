INSERT INTO tbl_collections (collectionSetName, releaseDate, totalCardsInCollection)
VALUES 
('Base Set', '1999-01-09', 102),
('Jungle', '1999-06-16', 64),
('Fossil', '1999-10-10', 62);

INSERT INTO tbl_types (typeName)
VALUES 
('Grass'),
('Fire'),
('Water'),
('Lightning'),
('Psychic'),
('Fighting'),
('Colorless');

INSERT INTO tbl_stages (stageName)
VALUES 
('Basic'),
('Stage 1'),
('Stage 2');

INSERT INTO tbl_cards (
    hp, name, info, attack, damage, weak, resis, retreat,
    cardNumberInCollection, collection_id, type_id, stage_id
)
VALUES
(60, 'Bulbasaur', 'Seed Pokémon', 'Leech Seed', '20', 'Fire', NULL, '1',1, 1, 1, 1),
(50, 'Charmander', 'Lizard Pokémon', 'Ember', '30', 'Water', NULL, '1', 4, 1, 2, 1),
(50, 'Squirtle', 'Tiny Turtle Pokémon', 'Bubble', '10', 'Lightning', NULL, '1', 7, 1, 3, 1),
(40, 'Pikachu', 'Mouse Pokémon', 'Thunder Jolt', '30', 'Fighting', NULL, '1', 58, 1, 4, 1),
(40, 'Gastly', 'Gas Pokémon', 'Lick', '10', 'Psychic', NULL, '1', 33, 1, 5, 1),
(70, 'Machop', 'Superpower Pokémon', 'Low Kick', '20', 'Psychic', NULL, '1', 52, 1, 6, 1),
(120, 'Snorlax', 'Sleeping Pokémon', 'Body Slam', '30', 'Fighting', 'Psychic', '4', 11, 2, 7, 1);
