def ask_user():
    question = input('Введите вопрос: ')
    question_answer_dict = {
        'Как дела?': 'Хорошо',
        'Что делаешь?': 'Программирую'
    }

    return question_answer_dict.get(question, 'Давай другой вопрос!')


while True:
    print(ask_user(), '\n')
