import random
# ユーザの手
U_hand = -1
# PCの手
P_hand = [1,2,3]
win = 0
lose = 0
Tie = 0

print("【最終結果】")
if win > lose:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの総合勝利です!")
elif win < lose:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nコンピューターの総合勝利です!")
else:
    print(f"あなた:{win}勝\nコンピュータ:{lose}勝\nあなたの引き分けです!")
