import xlsxwriter, os


def createExcel(quotes_dict):
    with xlsxwriter.Workbook('demo.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        worksheet.write(0, 0, 'Author')
        worksheet.write(0, 1, 'Quote')

        # Write dict data
        for i, (k, v) in enumerate(quotes_dict.items(), start=1):
            worksheet.write(i, 0, k)
            worksheet.write(i, 1, v)


def map_quote_data(quotes):
    texts = []
    authors = []

    for quote in quotes:
        quote_text = quote.find('span', {'class': 'text'}).text
        texts.append(quote_text)
        quote_author = quote.findAll('span')[1].find('small', {'class': 'author'}).text
        authors.append(quote_author)

    return dict(zip(authors, texts))
