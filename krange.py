class Range:
    """
        Represents the range class for the kata.
    """

    low_limit = None
    high_limit = None

    def __init__(self, low_limit, high_limit) -> None:
        self.low_limit = low_limit
        self.high_limit = high_limit
        pass

    def contains(self, values_to_check):
        """
            Returns true if the values are contianed in the range.
        """
        
        for value in values_to_check:
            if (value in range(self.low_limit, self.high_limit, 1)):
                continue

            else:
                return False

        return True
    
    pass