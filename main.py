from utils import load_data, prepare_data, conv_date

filename = 'operations.json'

all_data = load_data(filename)
operations = prepare_data(all_data)

for operation in operations:
    operation["date"] = conv_date(operation["date"])
    print(f"{operation['date']} {operation['description']}")
    print(f"{operation['from_account']} -> {operation['to_account']}")
    print(f"{operation['amount']} {operation['name']}\n")