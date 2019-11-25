import gspread
from oauth2client.service_account import ServiceAccountCredentials

# spreadsheet data
vocabulary = "1Y_yJ2btyxUpulpy0p-fGDaSMcRcX5abpBYqpIAPH0wY"


class Spreadsheet:
    def __init__(self):
        # use creds to create a client to interact with the Google Drive API
        self.scope = ['https://spreadsheets.google.com/feeds']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', self.scope)
        self.client = gspread.authorize(self.creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        self.workbook = self.client.open_by_key(vocabulary)

    def list_worksheets(self):
        return self.workbook.worksheets()

    def create_worksheet(self, title="A worksheet", rows="100", cols="20"):
        if title not in self.list_worksheets():
            return self.workbook.add_worksheet(title=title, rows=rows, cols=cols)

    @staticmethod
    def update_cells(worksheet, subject):
        cell_list = worksheet.range('A1:C7')
        for cell in cell_list:
            cell.value = 'O_o'

        # Update in batch
        worksheet.update_cells(cell_list)


if __name__ == '__main__':
    spreadsheet = Spreadsheet()
    spreadsheet.list_worksheets()