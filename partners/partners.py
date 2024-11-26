from openpyxl import load_workbook

if __name__ == '__main__':
    wb = load_workbook('Me & My Partner.xlsx')
    groups = []
    for row in wb.active:
        values = [cell.value for cell in row]
        pairs = (values[1], values[2])
        if None not in pairs:
            if values[2] < values[1]:
                pairs = (values[2], values[1])
            if pairs not in groups:
                groups.append(pairs)

    # prints
    for pair in groups:
        print(pair)
