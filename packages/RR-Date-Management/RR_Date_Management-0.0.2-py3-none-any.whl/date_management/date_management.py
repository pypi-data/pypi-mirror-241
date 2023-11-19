class Date_Management:
    """
    Class containing methods to cover frequent date operations.
    """

    def __init__(self):
        """
        __init__ : constructor method.
        """
        pass

    def timestamp_to_date(dataframe):
        """
        timestamp_to_date : Method to convert all datetime values in dataframe to date values. 

        Arguments:
            dataframe : A dataframe should be passed. Preferrably pandas dataframe.

        Returns:
            dataframe : converted dataframe.
        """
        col_datatype_dict=dataframe.dtypes.to_dict()
        datetime_columns_list = {i for i in col_datatype_dict if col_datatype_dict[i]=='datetime64[ns]'}
        try:    
            for col in datetime_columns_list:
                dataframe[col]=dataframe[col].dt.date
        except Exception:
            error_msg=f"Error: Unknown Error."
            print(f"{error_msg}")
        finally:
            return dataframe