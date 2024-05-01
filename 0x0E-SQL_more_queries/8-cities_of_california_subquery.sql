-- Lists all the cities of California that can be found in the database

SELECT cities.id, cities.name FROM cities WHERE cities.state_id = 1;
