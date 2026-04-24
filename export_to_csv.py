import csv
def export_to_csv(arr, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in arr:
            writer.writerow(row.get_array())
