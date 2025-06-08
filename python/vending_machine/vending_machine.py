from juice import Juice

class VendingMachine:
    """
    VendingMachine(自販機)を表すクラスです。

    Attribute:
        __juices_stock: ジュースの在庫
    """
    def __init__(self, juice, count):
        """
        VendingMachineオブジェクトを初期化する。

        :param juice(Juice): Juiceクラス
        :param count(str): 個数
        """
        self.__juices_stock = {"name": juice.name, "price": juice.price, "count": count}

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