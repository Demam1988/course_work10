from utils import load_data, filter_sort, prepare_data, conv_date

filename = 'operations.json'

all_data = load_data(filename)
sorted_data = filter_sort(all_data)
operations = prepare_data(sorted_data)

for operation in operations:
    operation["date"] = conv_date(operation["date"])
    print(f"{operation['date']} {operation['description']}")
    print(f"{operation['from_account']} -> {operation['to_account']}")
    print(f"{operation['amount']} руб.\n")