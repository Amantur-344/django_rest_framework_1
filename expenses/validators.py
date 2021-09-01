class TopUpValidator:

    @classmethod
    def validator_balance(cls, balance: float) -> bool:
        return False if not balance else True
