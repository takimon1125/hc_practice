from suica import Suica

if __name__ == "__main__":
    # ステップ1
    print("----ステップ1 Suica----")
    suica = Suica()
    print(f"現在のチャージ残高:{suica.deposit}円")
    print("99円をチャージします。")
    try:
       suica.charge_deposit(99)
    except ValueError as e:
        print(e)
    print("100円をチャージします。")
    suica.charge_deposit(100)
    print(f"現在のチャージ残高:{suica.deposit}円")