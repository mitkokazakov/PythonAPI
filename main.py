import json
import xlsxwriter
import requests
from datetime import date

response = requests.get("https://api.baubuddy.de/dev/index.php/v1/vehicles/select/active")

response_text = response.text

data = json.loads(response_text)

filtered_arr = [data[i] for i in range(len(data)) if data[i]['hu'] != None]
#filtered_arr.sort(key= lambda x: x.gruppe)

print(len(filtered_arr))

inp = input('Enter parameters separated with coma: ')

def create_xlsx_file(input,filtered_arr):

    current_date = date.today()

    current_date_iso = current_date.isoformat()

    name_of_generated_file = f"vehicles_{current_date_iso}.xlsx"

    workbook = xlsxwriter.Workbook(name_of_generated_file)
    worksheet = workbook.add_worksheet('Data')

    worksheet.write('A1', "Gruppe")
    worksheet.write('B1', "rnr")

    row = 2;

    for i in range(0, len(filtered_arr)):
        worksheet.write('A' + str(row + i), filtered_arr[i]['gruppe'])
        worksheet.write('B' + str(row + i), filtered_arr[i]['rnr'])

    if input == '':
        pass

    else:
        params_arr = input.split(',')
        next_column = 'C'

        for i in range(0,len(params_arr)):
            current_parameter = params_arr[i]
            worksheet.write(next_column + '1', current_parameter)

            for j in range(0, len(filtered_arr)):
                worksheet.write(next_column + str(row + j), filtered_arr[j][current_parameter])


            next_column = chr(ord(next_column) + 1)

    workbook.close()

create_xlsx_file(inp,filtered_arr)



