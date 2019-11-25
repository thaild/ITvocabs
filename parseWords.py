# coding=utf-8
import urllib.request, json

from spreadsheet import Spreadsheet
from utils import readDataFromFile


def parse_words():
    data = readDataFromFile('data/subjects.json')
    subjects = data['Subjects']
    for sub in subjects:
        subject = {'id': sub['id'], 'name': sub['name'], 'total': sub['total'], 'words': []}
        subject_data = readDataFromFile('data/subject-{}.json'.format(sub['id']))
        words = subject_data['Words']
        '''
        parse dict: word {'id', 'word', 'phonetic', 'mean'}
        '''
        for word in words:
            subject['words'].append({key: word[key] for key in word.keys() & {'id', 'word', 'phonetic', 'mean'}})

        worksheet = spreadsheet.create_worksheet(subject['name'])
        spreadsheet.update_cells(worksheet, subject)


if __name__ == '__main__':
    spreadsheet = Spreadsheet()
    parse_words()
    # parse_words()
