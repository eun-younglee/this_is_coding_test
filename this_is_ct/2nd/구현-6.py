# Ch 12 - 기출문제 11. 뱀

# 사과를 먹으면 뱀 길이가 늘어남
# 벽이나 자기 자신의 몸에 부딪히면 게임 오버
# n * n 보드에서 게임이 진행되고, 뱀의 초기 길이는 1이고 맨 위 맨 좌측에 위치
# 뱀은 몸길이를 늘여 머리를 다음 칸에 위치시키고, 사과가 있으면 꼬리 움직이지 않고 없으면 몸길이 줄이기
# 게임이 몇 초에 끝나는지 출력하기

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
