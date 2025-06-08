from juice import Juice
from purchase_error import PurchaseError

class VendingMachine:
    """
    VendingMachine(自販機)を表すクラスです。

    Attribute:
        __stock: ジュースの在庫
        __sales: 売上金額
    """
    def __init__(self):
        """
        VendingMachineを初期化する。

        :param juice(Juice): Juiceクラス
        :param count(str): 個数
        """
        self.__stock = []
        # 初期在庫を設定
        for _ in range(5):
            self.__stock.append(Juice("ペプシ", 150))
            # step4 3種類管理のために追加
            self.__stock.append(Juice("モンスター", 230))
            self.__stock.append(Juice("いろはす", 120))
        self.__sales = 0

    @property
    def stock(self):
        """
        [getter]在庫を取得する。

        Returns:
            int: 値段
        """ 
        return self.__stock
    
    @stock.setter
    def stock(self, stock):
        """
        [setter]在庫をセットする

        :param stock(list): 在庫
        """
        self.__stock = stock

    @property
    def sales(self):
        """
        [getter]売上金額を取得する。

        Returns:
            int: 売上金額
        """ 
        return self.__sales
    
    @sales.setter
    def sales(self, sales):
        """
        [setter]売上金額をセットする

        :param sales(int): 売上金額
        """
        self.__sales = sales

    def get_stock_list(self):
        """
        自動販売機の在庫を表示

        Returns:
            list[dict]: 各ジュースの {"name": str, "count": int} 形式の辞書のリスト。
        """
        # juiceの名前を取得後にsetで重複を削除
        juice_names = set([juice.name for juice in self.__stock])
        # 名前から在庫の辞書型のリストを生成
        vending_machin_stock_list = [{"name": name, "count": len(list(filter(lambda x: x.name == name, self.__stock)))} for name in juice_names]
        return vending_machin_stock_list
    
    def get_can_purchase_list(self):
        """
        購入可能なジュースのリスト

        Returns:
            list(str)
        """
        # juiceの名前を取得後にsetで重複を削除。その後にリストに変換
        juice_names = list(set([juice.name for juice in self.__stock]))
        return juice_names

    def check_purchase_juice(self, juice_name):
        """
        ジュースの名前から購入できるか判定。

        :param juice_name(str): ジュースの名前

        Returns:
            bool
        """
        return len(list(filter(lambda x: x.name == juice_name, self.__stock))) > 0
    
    def purchase(self, juice_name, suica):
        """
        Suicaを使って自販機からジュースを購入する。
        ジュースの在庫を減らす
        売り上げ金額を増やす
        Suicaのチャージ残高を減らす

        :param suica(Suica): Suicaインスタンス
        
        raise: 
        PurchaseError: チャージ残高が足りない場合もしくは在庫がない場合。
        """
        # juiceの名前から該当するリストを抽出
        juice_stock = list(filter(lambda x: x.name == juice_name, self.__stock))
        if not len(juice_stock) > 0:
            raise PurchaseError("在庫が足りません。") 
        if juice_stock[0].price <= suica.deposit:
            # 名前から抽出したジュースを在庫から削除
            juice = juice_stock.pop(0)
            self.__stock.remove(juice)
            self.__sales += juice.price
            suica.pay(juice.price)
        else:
            raise PurchaseError("チャージ残高が足りません。")
    
    def add_stock(self, juice):
        """
        ジュースの在庫を追加

        :param juice(Juice): Juiceインスタンス
        """
        self.__stock.append(juice)