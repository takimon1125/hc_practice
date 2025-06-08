from purchase_error import PurchaseError

class VendingMachine:
    """
    VendingMachine(自販機)を表すクラスです。

    Attribute:
        __juices_stock: ジュースの在庫
        __sales: 売上金額
    """
    def __init__(self, juice, count):
        """
        VendingMachineオブジェクトを初期化する。

        :param juice(Juice): Juiceクラス
        :param count(str): 個数
        """
        self.__juices_stock = {"name": juice.name, "price": juice.price, "count": count}
        self.__sales = 0

    @property
    def juices_stock(self):
        """
        [getter]在庫を取得する。

        Returns:
            int: 値段
        """ 
        return self.__juices_stock
    
    @juices_stock.setter
    def juices_stock(self, juices_stock):
        """
        [setter]在庫をセットする

        :param juices_stock(dictionary): 在庫
        """
        self.__juices_stock = juices_stock

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


    def check_purchase_juice(self):
        """
        juiceが購入できるか判定。

        Returns:
            bool
        """
        return self.__juices_stock["count"] > 0
    
    def purchase(self, suica):
        """
        スイカを使って自販機からジュースを購入する。
        ジュースの在庫を減らす
        売り上げ金額を増やす
        Suicaのチャージ残高を減らす

        :param suica(Suica): Suicaインスタンス
        
        raise: 
        PurchaseError: チャージ残高が足りない場合もしくは在庫がない場合。
        """
        if self.__juices_stock["price"] <= suica.deposit and self.__juices_stock["count"] > 0:
            self.__juices_stock["count"] -= 1
            self.__sales += self.__juices_stock["price"]
            suica.deposit -= self.__juices_stock["price"]
        else:
            raise PurchaseError("チャージ残高が足りないもしくは在庫が足りません。")