class Range:
    """
        Represents the range class for the kata.
    """

    low_limit = None
    high_limit = None

    def __init__(self, input_range: str) -> None:
        values = input_range.strip().split(",")

        if (values[0][0] == "["):
            self.low_limit = int(values[0][1])
            pass

        else:
            self.low_limit = int(values[0][1]) + 1
            pass

        if (values[1][1] == "]"):
            self.high_limit = int(values[1][1])
            pass

        else:
            self.high_limit = int(values[1][1]) - 1
            pass
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
    

    def getAllPoints(self):
        pass
    pass