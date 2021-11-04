def fetch_columns_options(data, table=False):
    """Handle creating column options based on the data

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component
        table: bool (def. False)
            Flag for returning table list

    Returns
    ----------
        options: list of dict
            Options for each of the dropdowns in the form of
            {'label': 'Example', 'value': 'example'}
    """

    if table:
        return [{"name": i, "id": i} for i in data[0]]
    else:
        return [{"label": i, "value": i} for i in data[0]]


def validate_store_data(data):
    """
    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        data_in: bool
            Determine if there is dataframe data in the data diction
    """

    if data and "df" in data and data["df"] is not None:
        return True
    return False
