# coding=utf-8
import urllib.request, json
from utils import writeDataToFile, readDataFromFile


# course: Tiếng Nhật công nghệ thông tin
id_course = 104000005
limit = 50
skip = 0


def fetch_subjects():
    with urllib.request.urlopen("https://minder.vn/api/subjects/subjects?id_course={0}&limit={1}&skip={2}"
                                .format(id_course, limit, skip)) as url:
        data = json.loads(url.read().decode())
        writeDataToFile('data/subjects.json', data)


def fetch_words_by_subjects():
    data = readDataFromFile('data/subjects.json')
    subjects = data['Subjects']
    for subject in subjects:
        with urllib.request.urlopen("https://minder.vn/api/words/words?id_subject={0}".format(subject['id'])) as url:
            data = json.loads(url.read().decode())
            writeDataToFile('data/subject-{0}.json'.format(subject['id']), data)


if __name__ == '__main__':
    fetch_subjects()
    fetch_words_by_subjects()
