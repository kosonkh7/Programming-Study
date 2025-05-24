-- https://www.hackerrank.com/challenges/binary-search-tree-1

SELECT DISTINCT(B.N), CASE 
                WHEN B.P IS NULL THEN 'Root'
                WHEN C.N IS NULL THEN 'Leaf'
                ELSE 'Inner' 
            END
FROM BST AS B
LEFT JOIN BST AS C ON B.N = C.P
LEFT JOIN BST AS P ON B.P = P.N
ORDER BY B.N;