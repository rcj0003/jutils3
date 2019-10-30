def format_results(columns, results):
    for column in columns:
        print("{:^18}".format(format_column_value(column)), "|", end = "")
    print()
    print("-" * (20 * len(columns)))

    for entry in results:
        for column in columns:
            print("{:^18}".format(format_column_value(format_column_value(entry[column]))), "|", end = "")
        print()

def format_column_value(value):
    result = f"{value}"
    return result if len(result) <= 15 else result[0:11] + "..."
