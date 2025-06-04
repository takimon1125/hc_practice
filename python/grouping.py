import random
group = ["A","B","C","D","E","F"]
# グループ内の順番をシャッフルする
group_shuffled = random.sample(group, len(group)) 
# グループの人数を区切る位置をランダムで出力
random_split = random.choice([2, 3])
# グループに分けてからソートする
group_1, group_2 = sorted(group_shuffled[:random_split]), sorted(group_shuffled[random_split:])
# 結果を出力
print(group_1)
print(group_2)