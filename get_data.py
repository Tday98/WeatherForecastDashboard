def get_data(days):
    dates = ["10-25-2023", "10-26-2023", "10-27-2023"]
    temperatures = [50, 55, 60]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures