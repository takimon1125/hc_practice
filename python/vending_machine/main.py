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
       suica.charge_deposit(99)
    except ValueError as e:
        print(e)
    print("100円をチャージします。")
    suica.charge_deposit(100)
    print(f"現在のチャージ残高:{suica.deposit}円")

    # ステップ2
    print("----ステップ2 ジュースの管理----")
    pepsi = Juice("ペプシ", 150)
    print(f"ジュースの名前:{pepsi.name}, ジュースの値段:{pepsi.price}円")
    vending_machine = VendingMachine(pepsi, 5)
    juice_stock = vending_machine.juices_stock
    print(f"juice_stockを出力:{juice_stock}")
    print(f"在庫は{juice_stock["name"]}: {juice_stock["count"]}個")

    # ステップ3　購入処理
    print("----ステップ3 購入処理----")
    print("ペプシを購入できるのかチェック")
    if vending_machine.check_purchase_juice():
        print("ペプシを購入できます")
    else:
        print("ペプシを購入できない")
    vending_machine.purchase(suica)
    print(f"自販機の売上：{vending_machine.sales}円")
    for _ in range(3):
        vending_machine.purchase(suica)
    print(f"自販機の売上：{vending_machine.sales}円")
    try:
        vending_machine.purchase(suica)
    except PurchaseError as e:
        print(e)
    if vending_machine.check_purchase_juice():
        print("ペプシを購入できます。")
    else:
        print("ペプシを購入できない。")