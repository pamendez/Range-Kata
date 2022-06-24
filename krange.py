ALLOWED_CHARACTERS = { "[", "]", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", " ", "," }

class Range:
    """
        Serves as the range class for operations using interval inputs.
    """

    def __init__(self, input_range) -> None:
        """
            Serves as the constructor of the class.

            Arguments
            -------------
            input_range: Serves as the input range.

            Exceptions
            -------------
            SyntaxError: Throws this exception if the input is not formatted properly.
        """

        if not (all(range_symbol in ALLOWED_CHARACTERS for range_symbol in input_range)):
            raise SyntaxError("The range input has invalid symbols or is not formatted properly.")

        if not (input_range.startswith(("(", "[")) and input_range.endswith((")", "]"))):
            raise SyntaxError("The range is not closed.")
        
        if not (input_range.split(",")):
            raise SyntaxError("The range is not valid")
        pass

     
        
    
