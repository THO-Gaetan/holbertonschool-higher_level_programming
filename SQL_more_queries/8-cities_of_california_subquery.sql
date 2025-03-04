-- lists all the cities of california tha can be found in hbtn_0d_usa
SELECT cities.id, cities.name FROM cities where cities.state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
