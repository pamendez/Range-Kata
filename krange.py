from __future__ import annotations

ALLOWED_CHARACTERS = { "[", "]", "(", ")", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", " ", "," }

class Range:
    """
        Serves as the range class for operations using interval inputs.
    """
    
    endpoints = None
    allpoints = None
    endpoint_symbols = None

    def __init__(self, input_range: str) -> None:
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
        
        lower_bound = input_range[0] 
        upper_bound = input_range[-1]
        input_range = input_range.replace(lower_bound, "", 1)
        input_range = input_range.replace(upper_bound, "", 1)
        limits = input_range.split(",");

        if not (len(limits) == 2):
            raise IndexError("The range has more or less than two components.")
        
        self.endpoints = []
        for limit in limits:
            limit = limit.strip()
            if not (limit.isdigit()):
                raise Exception("The range has invalid numbers.")
            
            numberLimit = int(limit)
            self.endpoints.append(numberLimit)

        # Validate intervals symbols
        if(lower_bound == "("):
           self.endpoints[0] += 1
       
        if(upper_bound == ")"):
            self.endpoints[1] -= 1

        if(self.endpoints[0] > self.endpoints[1]):
          raise ValueError("The lower limit cant be greater than the upper limit in the range");

        self.endpoint_symbols = [lower_bound, upper_bound]
        self.allpoints = self.getAllPoints()

        pass

    def to_string(self):
        """
            Returns the range as a formatted string.
        """       
        return f"{self.endpoint_symbols[0]}{self.endpoints[0]},{self.endpoints[1]}{self.endpoint_symbols[1]}"

    def getAllPoints(self):
      index = self.endpoints[0]
      interval = []
      while index <= self.endpoints[1]:
         interval.append(index)
         index += 1
         pass 

      return interval

    def contains(self, range_or_elements: set | Range):
        """
            Given the type of the input:

            a. If the input is a set of elements:
                Returns True if the values are contained on range.
                Otherwise, it returns False.

            b. If the input is range:
                Returns True if the range is contained inside another range.
                Otherwise, it returns False.

            Arguments
            ----------
            elements - A set of the elements.

            Exceptions
            -----------
            TBA.
        """

        is_contained = True
        if (type(range_or_elements) is set):            
            elements = range_or_elements
            if not (len(elements) > 0):
                raise ValueError("The input set is empty.")

            for value in elements:
                if not (value in self.allpoints):
                    is_contained = False
                    break

                else:
                    continue
                pass

        elif (type(range_or_elements) is Range):
            range_ = range_or_elements
            if not (self.endpoints[0] <= range_.endpoints[0] and range_.endpoints[1] <= self.endpoints[1]):
                is_contained = False
                pass
            pass

        else:
            pass

        return is_contained