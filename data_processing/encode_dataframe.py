from sklearn.preprocessing import OrdinalEncoder

def encoder_dataframe(dataset, category):
    """encoder_dataframe

    Args:
        dataset (dataframe): dataframe where categories are
        category (string): name of columnd which will be encode

    Returns:
        dataframe with encoder category column
    """
    encoder = OrdinalEncoder()
    encoder.fit(dataset[[category]])
    var_id = str(category) + '_ID'
    dataset[[var_id]] = encoder.transform(dataset[[category]])
    dataset[var_id] = dataset[var_id].astype(int)
    return dataset
