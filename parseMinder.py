# coding=utf-8
import urllib.request, json

# course: Tiếng Nhật công nghệ thông tin
id_course = 104000005
limit = 50
skip = 0


def parse_subjects():
    with urllib.request.urlopen("https://minder.vn/api/subjects/subjects?id_course={0}&limit={1}&skip={2}"
                                .format(id_course, limit, skip)) as url:
        data = json.loads(url.read().decode())
        return data['Subjects']


def parse_words(subs):
    list_subjects = []
    for sub in subs:
        subject = {}
        subject.id = sub['id']
        subject.name = subject['name']
        subject.total = subject['total']
        subject.words = []
        with urllib.request.urlopen("https://minder.vn/api/words/words?id_subject={0}".format(sub['id'])) as url:
            data = json.loads(url.read().decode())
            words = data['Words']
            '''
            parse dict: word {'id', 'word', 'phonetic', 'mean'}
            '''
            subject.words.append({key: words[key] for key in words.keys() & {'id', 'word', 'phonetic', 'mean'}})

        list_subjects.append(subject)
    return list_subjects


if __name__ == '__main__':
    subjects = parse_subjects()
    parse_words(subjects)
