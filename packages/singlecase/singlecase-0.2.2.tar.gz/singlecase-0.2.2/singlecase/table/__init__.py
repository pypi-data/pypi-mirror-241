from singlecase.data import Data

def show(data: Data):
    """
    Function that prints the data in a Data object.

    Args:
        data (Data): The Data object to be printed.
    """
    return data._df.T
    