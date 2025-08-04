score = 0


# 3등까지의 최고 기록을 저장하는 함수
def save_score():

    with open("ranking.txt", "r") as f:

        ranking = sorted([int(line.strip()) for line in f] + [score], reverse=True)
        ranking[3:] = []

    with open("ranking.txt", "w") as f:
        for e in ranking:
            f.write(str(e) + "\n")


# 랭킹을 읽고 정해진 형식의 문자열 반환
def read_ranking():

    with open("ranking.txt", "r") as f:

        ranking = [int(line.strip()) for line in f]

    labels = ["1st", "2nd", "3rd"]
    return "   |   ".join(f"{labels[i]} : {ranking[i]}" for i in range(len(ranking)))
