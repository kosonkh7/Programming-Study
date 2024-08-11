"""
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.

처음엔 dp테이블을 2개의 열 [최소합, 인덱스]로 구성하고, 인덱스를 통해 구하고자 했는데 도저히 모르겠더라

힌트 참고하고 나서, 별도의 dp 테이블 없이 입력값을 넣은 그래프 자체를 갱신하는 방법으로 문제를 푸는 것을 알게 되었다. 

풀이는 간단하지만 혼자 고민해서 풀기 어려웠을 것.
"""

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n): 
    n_list[i][0] = n_list[i][0] + min(n_list[i-1][1], n_list[i-1][2])
    n_list[i][1] = n_list[i][1] + min(n_list[i-1][0], n_list[i-1][2])
    n_list[i][2] = n_list[i][2] + min(n_list[i-1][0], n_list[i-1][1])

print(min(n_list[n-1]))


#print(min(n_list[0]), n_list[0].index(min(n_list[0])))