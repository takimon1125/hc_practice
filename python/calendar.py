import datetime
import sys

def get_month(now_date):
    """
    コマンドライン引数から月を取得するか、現在の月を返す。
    """
    option = "-m"
    month = -1
    if option in sys.argv:
        # -mオプションのindex
        idx = sys.argv.index(option)
        # -m引数の値を取得
        value = sys.argv[idx + 1]
        try:
            month = int(value) 
        except:
            return f"{value} is neither a month number (1..12) nor a name"
        else:
            # 1月~12月の範囲かを判別 
            if not (1 <= month <= 12):
                return f"{month} is neither a month number (1..12) nor a name"
    else:
        month = now_date.month
    return month


def print_calendar(year, month):
    """
    指定された月と年のカレンダーを出力する
    """
    # 年月と曜日を出力
    print(f"{month}月 {year}".center(20))
    print("月 火 水 木 金 土 日")
    # 月初の曜日を取得(0=月曜, 6=日曜)
    start_weekday_index = datetime.date(year = year, month=month, day=1).weekday()
    # 月末の日を取得
    # 翌月の1日の前日を計算することで、月末日を取得
    next_month = (month % 12) + 1 # 12月の場合は1月に戻す
    next_month_year = year + (1 if month == 12 else 0)
    last_day_of_month = datetime.date(year=next_month_year, month=next_month, day=1) - datetime.timedelta(days=1)
    end_date_day = last_day_of_month.day
    # 日付部分を出力する
    # 月初までの空白を初期値に
    current_weekdays = ["  "] * start_weekday_index
    now_date = datetime.datetime.today()
    now_year, now_month, now_day = now_date.year, now_date.month, now_date.day
    for day in range(1, end_date_day + 1):
        # 本日の場合は色を反転させて出力
        if year == now_year and month == now_month and day == now_day:
            current_weekdays.append("\033[7m" + str(day).rjust(2, ' ') + "\033[0m") 
        else:
            current_weekdays.append(str(day).rjust(2, ' '))
        # 日曜日または月末日の場合は出力
        if len(current_weekdays) == 7 or day == end_date_day:
            print(" ".join(current_weekdays))
            current_weekdays = []

if __name__ == "__main__":
    # 今年の年のデータを取得
    now_date = datetime.datetime.today()
    target_year = now_date.year
    # 今年の月のデータを取得
    target_month = get_month(now_date)
    # 月の取得結果がエラーメッセージ (文字列) の場合
    if isinstance(target_month, str):
        print(target_month)
        exit()
    print_calendar(target_year, target_month)