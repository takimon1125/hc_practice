from juice import Juice
from purchase_error import PurchaseError
from suica import Suica
from vending_machine import VendingMachine

if __name__ == "__main__":
    # ステップ1
    print("----ステップ1 Suica----")
    suica = Suica()
    print(f"現在のチャージ残高:{suica.deposit}円")
    print("99円をチャージします。")
    try:
       suica.charge(99)
    except ValueError as e:
        print(e)
    print("100円をチャージします。")
    suica.charge(100)
    print(f"現在のチャージ残高:{suica.deposit}円")


    # ステップ2
    print("----ステップ2 ジュースの管理----")
    # クラスが使用できるのかチェック
    pepsi = Juice("ペプシ", 150)
    print(f"ジュースの名前:{pepsi.name}, ジュースの値段:{pepsi.price}円")
    # 自販機インスタンスを作成(ペプシ,150円)
    vending_machine = VendingMachine()
    # 自動販売機の在庫のリスト[Juice()]
    juice_stocks = vending_machine.stock


    # ステップ3　購入処理
    print("----ステップ3 購入処理----")
    print("ペプシを購入できるのかチェック")
    try:
        vending_machine.check_purchase_juice("ペプシ")
        print("ペプシを購入できる")
    except PurchaseError as e:
        print(e)
    # チャージ残高が足りないエラーを出す
    try:
        for _ in range(5):
            print("ぺプシを一本買います。")
            vending_machine.purchase("ペプシ", suica)
            print(f"自販機の売上：{vending_machine.sales}円")
            print(f"現在のチャージ残高:{suica.deposit}円")
    except PurchaseError as e:
        print(e)


    # ステップ4　購入処理
    print("----ステップ4 機能拡張----")
    vending_machine2 = VendingMachine()
    print(f"購入可能なドリンクのリスト：{vending_machine2.get_can_purchase_list()}")
    print("レッドブルーを追加")
    pepsi2 = Juice("レッドブルー", 150)
    vending_machine2.add_stock(pepsi2)
    print(f"購入可能なドリンクのリスト：{vending_machine2.get_can_purchase_list()}")

    # モンスターを購入
    print("1000円をチャージします。")
    suica.charge(900)
    print("モンスターを購入できるのかチェック")
    try:
        vending_machine2.check_purchase_juice("モンスター")
        print("モンスターを購入できる")
    except PurchaseError as e:
        print(e)

    # 残高が足りなくなるエラーを発生
    try:
        for _ in range(4):
            print("モンスターを一本買います。")
            vending_machine2.purchase("モンスター", suica)
            print(f"自販機の売上：{vending_machine2.sales}円")
            print(f"現在のチャージ残高:{suica.deposit}円")
    except PurchaseError as e:
        print(e)

    # いろはすを購入
    print("1300円をチャージします。")
    suica.charge(1300)
    print("いろはすを購入できるのかチェック")
    try:
        vending_machine2.check_purchase_juice("いろはす")
        print("いろはすを購入できる")
    except PurchaseError as e:
        print(e)

    # 在庫が足りなくなるエラーを発生
    try:
        for _ in range(6):
            print("いろはすを一本買います。")
            vending_machine2.purchase("いろはす", suica)
            print(f"自販機の売上：{vending_machine2.sales}円")
            print(f"現在のチャージ残高:{suica.deposit}円")
    except PurchaseError as e:
        print(e)

    try:
        vending_machine2.check_purchase_juice("いろはす")
        print("いろはすを購入できる")
    except PurchaseError as e:
        print(e)