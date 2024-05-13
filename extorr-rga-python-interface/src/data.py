def process_data(data):
    """
    Processes the data acquired from the Extorr RGA.

    Args:
        data (tuple): A tuple containing the mass-to-charge ratios and partial pressures of the detected gas species.

    Returns:
        dict: A dictionary containing the processed RGA data, with mass-to-charge ratios as keys and partial pressures as
        values.
    """
    mass_to_charge_ratios, partial_pressures = data
    processed_data = {}
    for mass, pressure in zip(mass_to_charge_ratios, partial_pressures):
        processed_data[mass] = pressure
    return processed_data
