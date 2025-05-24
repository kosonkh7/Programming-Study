-- https://www.hackerrank.com/challenges/the-report/problem

SELECT IF(FLOOR(Marks/10)+1 >=8, Name, NULL) AS NAME, Marks, IF(Marks = 100, 10, IF(Marks =0, 1, FLOOR(Marks/10)+1)) AS Grade
FROM Students
ORDER BY Grade DESC, NAME, Marks DESC


-- JOIN 할 때 적절한 조건 설정이 가능하다는 걸 처음 배움
SELECT CASE WHEN Grade < 8 THEN 'NULL' ELSE Name END, Grade, Marks
FROM Students s
LEFT JOIN Grades g
ON s.Marks BETWEEN Min_Mark AND Max_Mark 
ORDER BY Grade DESC, Name, Marks