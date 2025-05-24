-- https://www.hackerrank.com/challenges/weather-observation-station-20
-- 피지컬로 풀은 코드. 윈도우 함수 (특히 ROW_NUMBER)에 익숙해지자

WITH tmp AS (SELECT LAT_N
FROM STATION
ORDER BY LAT_N
LIMIT 250)

SELECT ROUND(LAT_N, 4)
FROM tmp
ORDER BY LAT_N DESC
LIMIT 1