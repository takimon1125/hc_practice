class Juice:
    """
    Juiceを表すクラスです。

    Attribute:
        __name: 名前
        __price: 値段
    """
    def __init__(self, name, price):
        """
        Juiceオブジェクトを初期化する。

        :param name(str): 名前
        :param price(int): 値段
        """
        self.__name = name
        self.__price = price

    @property
    def name(self):
        """
        [getter]名前を取得する。

        Returns:
            str: 名前
        """ 
        return self.__name
    
    @name.setter
    def name(self, name):
        """
        [setter]名前ををセットする

        :param name(str): 名前
        """
        self.__name = name

    @property
    def price(self):
        """
        [getter]値段を取得する。

        Returns:
            int: 値段
        """ 
        return self.__price
    
    @price.setter
    def price(self, price):
        """
        [setter]値段をセットする

        :param price(int): 値段
        """
        self.__price = price