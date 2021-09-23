DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    all_python_devs = list(filter(lambda worker : worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    # print(all_python_devs) # 😎

    all_platzi_workers = list(filter(lambda worker : worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker : worker['name'], all_platzi_workers))

    # for worker in all_platzi_workers:
        # print(worker + '(★ ω ★)')

    adults = [adult for adult in DATA if adult['age'] > 18]
    # print(adults)

    old_people = [old for old in DATA if old['age'] > 70]

    for old in old_people:
        print(old['name'])


if __name__ == "__main__": # entry point o punto de entrada ---> inicia la función cuando ejecutamos el archivo
    run()