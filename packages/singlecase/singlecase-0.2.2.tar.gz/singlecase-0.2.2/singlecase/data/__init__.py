from typing import Union, Dict, List
import pandas as pd


class Data:
    """
    A class used to represent single-case data in a structured format.

    This class accepts data either as a pandas DataFrame or as a dictionary and 
    stores it internally as a DataFrame for further manipulation and analysis. It 
    provides properties to manage the phase variable and dependent variables present
    in the data.

    Any variable with datatype of float is assumed to be a dependent variable. The 

    Args:
        data (Union[pd.DataFrame, Dict]): The data set. Must be either a pandas DataFrame 
        or a dictionary.
        pvar (str, optional): The name of the phase variable column in the data set. If the
        data contains a column named "phase", this will be used as the phase variable by default.
        index (str, optional): The name of the variable in the dataset to use as the index, i.e.
        the labels of each test session. If not provided, the sessions will be numbered starting at 0.
    
    Raises:
        ValueError: If the provided data is not a pandas DataFrame or a dictionary.
    """

    def __init__(self, data: Union[pd.DataFrame, Dict], pvar: str=None, index: str = None, units: Union[Dict[str, str], str] = None):
        """
        Constructs and initializes the Data object.
        """

        if isinstance(data, dict):
            self._df = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            self._df = data.copy()
        else:
            raise ValueError("data must be a pd.DataFrame or a dict")


        if index is not None:
            self._df.set_index(index, inplace=True)

        if pvar is None:
            if "phase" in self._df.columns:
                pvar = "phase"
            else:
                self._df["phase"] = "default"
                pvar = "phase"
            
        else:
            if pvar not in self._df.columns:
                raise ValueError("pvar must be the name of a column in the data frame")

        self._pvar = pvar

        # float columns are assumend to be dependent variables
        self._dvars = [col for col in self._df.columns if self._df[col].dtype == float]


        if units is None:
            units = {dvar: "" for dvar in self._dvars}
        elif isinstance(units, str):
            units = {dvar: units for dvar in self._dvars}
        elif not isinstance(units, dict):
            raise ValueError("units of dependent variables must be a dict or a str")

        self._dvar_units = units

    @property
    def index(self) -> str:
        """
        Property that gets the name of the index variable of the Data object.

        Returns:
            str: The name of the index column.
        """
        return self._df.index.name

    @property
    def pvar(self):
        """
        Property that gets the phase variable of the Data object.

        Returns:
            str: The name of the phase variable column in the data frame.
        """
        return self._pvar
    
    @pvar.setter
    def pvar(self, pvar: str):
        """
        Property that sets the phase variable of the Data object.

        Args:
            pvar (str): The name of the phase variable column to be set.

        Raises:
            ValueError: If the provided pvar is not a column name in the DataFrame.
        """
        if pvar not in self._df.columns:
            raise ValueError("pvar must be the name of a column in the data frame")
        self._pvar = pvar

    @property
    def phases(self) -> List[str]:
        """
        Property that gets the phases in the data set.

        Returns:
            List[str]: The names of the phases in the data set.
        """
        return list(self._df[self.pvar].unique())

    @property
    def dvar_units(self) -> Dict[str, str]:
        """
        Property that gets the units of the dependent variables.

        Returns:
            Dict[str, str]: A dictionary mapping the dependent variable names to their units.
        """
        return self._dvar_units
    
    @property
    def dvars(self):
        """
        Property that gets the names of the dependent variable columns.

        These are identified as any columns in the DataFrame with float datatype.

        Returns:
            List[str]: The names of the dependent variable columns.
        """
        return self._dvars


    def phase_data(self, phase: str, dvar: str) -> pd.DataFrame:
        """
        Get the data for a specific phase and dependent variable.

        Args:
            phase (str): The name of the phase.
            dvar (str): The name of the dependent variable.

        Returns:
            pd.DataFrame: The data for the specified phase and dependent variable.
        """
        return self._df.loc[self._df[self.pvar] == phase, dvar]
