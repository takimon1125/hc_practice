class Suica:
    """
    Suicaを表すクラスです。

    Attribute:
        __deposit: 預かり金

    method:
        charge(amount): 任意の金額をチャージできる。
                        100円未満の場合はエラーが出る。
        get_deposit: 現在のチャージ残高を返す
        pay(amount): 任意の金額を支払う
    """
    def __init__(self):
        """
        Suicaを初期化する。デフォルトでデポジットが500円チャージされる
        """
        self.__deposit = 500

    @property
    def deposit(self):
        """
        [getter]現在の預かり金を取得する。

        Returns:
            int: 現在の預かり金
        """ 
        return self.__deposit

    def charge(self, amount):
        """
        Suicaに金額をチャージする。

        :param amount(int): チャージする金額

        raise: 
            ValueError: チャージ金額が100円未満の場合。
        """
        if amount < 100:
            raise ValueError("100円未満をチャージできません。100円以上の金額でチャージしてください。")
        self.__deposit += amount

    def pay(self, amount):
        """
        Suicaから金額を支払う

        :param amount(int): 支払う金額

        raise: 
            ValueError: チャージ金額が100円未満の場合。
        """
        if self.__deposit < amount:
            raise ValueError("支払う金額の方が多いです。suicaをチャージしてください。")
        self.__deposit -= amount