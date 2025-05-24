-- https://www.hackerrank.com/challenges/weather-observation-station-5

WITH max_long AS(
    SELECT CITY, LENGTH(CITY)
    FROM STATION
    ORDER BY LENGTH(CITY), CITY
    LIMIT 1
), min_long AS(
    SELECT CITY, LENGTH(CITY)
    FROM STATION
    ORDER BY LENGTH(CITY) DESC, CITY
    LIMIT 1
)

SELECT *
FROM max_long
UNION
SELECT *
FROM min_long