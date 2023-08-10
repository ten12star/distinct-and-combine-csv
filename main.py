import csv

def distinct_and_combine(input_file, distinct_column, combine_columns, output_file):
    distinct_values = set()
    combined_values = {}

    with open(input_file, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            distinct_value = row[distinct_column]
            distinct_values.add(distinct_value)
            
            combined_value = ' '.join([row[col] for col in combine_columns])
            if distinct_value in combined_values:
                combined_values[distinct_value].append(combined_value)
            else:
                combined_values[distinct_value] = [combined_value]

    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)

        for distinct_value in distinct_values:
            combined_value = ';'.join(combined_values[distinct_value])
            writer.writerow([distinct_value, combined_value])
            

distinct_and_combine('./input.csv', 'Pcode', ['ImageURL'], './output.csv')