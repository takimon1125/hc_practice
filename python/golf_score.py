# スコアに対応するスコア名
SCORE_NAMES_MAP = {
    -2: "イーグル",
    -1: "バーディ",
    0: "パー",
    1: "ボギー",
}


def calculate_golf_score_name(regulation_number, player_count):
    """
    規定打数とプレイヤーの打数からスコアを計算して名称を返す
    """
    if regulation_number == 5 and player_count == 1:
        return "コンドル"

    if player_count == 1:
        return "ホールインワン"

    if regulation_number == 5 and player_count == 2:
        return "アルバトロス"

    score_diff = player_count - regulation_number

    # スコアーが2以上の場合は「数字」+「ボギー」で出力する
    if score_diff >= 2:
        return f"{score_diff}{SCORE_NAMES_MAP[1]}"
    
    return SCORE_NAMES_MAP[score_diff]


if __name__ == "__main__":
    # 規定打数、プレイヤーの打数
    regulation_numbers, player_counts = [list(map(int, input().split(","))) for _ in range(2)]
    golf_scores = []
    # 規定打数とプレイヤーの打数からスコアを計算して名称を配列に作成
    for regulation_number, player_count in zip(regulation_numbers, player_counts):
        golf_scores.append(calculate_golf_score_name(regulation_number, player_count)) 
    # スコアを出力
    print(",".join(golf_scores))