#CPUとユーザーの手を比較して勝敗判定。
if U_hand == 1:
    if P_hand == 1:
        print('引き分けです。')
        Tie += 1
    elif P_hand == 2:
        print('あなたの勝ちです。')
        win += 1
    else :
        print('CPUの勝ちです。')
        lose += 1
elif U_hand == 2:
    if P_hand == 1:
        print('CPUの勝ちです。')
        lose += 1
    elif P_hand == 2:
        print('引き分けです。')
        Tie += 1
    else :
        print('あなたの勝ちです。')
        win += 1
else:
    if P_hand == 1:
        print('あなたの勝ちです。')
        win += 1
    elif P_hand == 2:
        print('CPUの勝ちです。')
        lose += 1
    else :
        print('引き分けです。')
        Tie += 1