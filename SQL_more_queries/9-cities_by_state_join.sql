-- lists all cities contained in hbtn_0d_usa
Select cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
