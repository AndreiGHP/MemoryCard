from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout
)
from random import shuffle

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo Card')

window.total = 0
window.points = 0


# ---------------- КЛАСС ----------------

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

# ---------------- ВОПРОС ----------------

lb_Question = QLabel('Вопрос')
lb_Question.setAlignment(Qt.AlignCenter)

# ---------------- КНОПКА ----------------

btn_OK = QPushButton('Ответить')

# ---------------- ОТВЕТЫ ----------------

RadioGroupBox = QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

layout_ans_h = QHBoxLayout()
layout_ans_v1 = QVBoxLayout()
layout_ans_v2 = QVBoxLayout()

layout_ans_v1.addWidget(rbtn_1)
layout_ans_v1.addWidget(rbtn_2)

layout_ans_v2.addWidget(rbtn_3)
layout_ans_v2.addWidget(rbtn_4)

layout_ans_h.addLayout(layout_ans_v1)
layout_ans_h.addLayout(layout_ans_v2)

RadioGroupBox.setLayout(layout_ans_h)

# ---------------- РЕЗУЛЬТАТ ----------------

AnsGroupBox = QGroupBox("Результат")

lb_Result = QLabel('')
lb_Result.setAlignment(Qt.AlignCenter)

lb_Correct = QLabel('')
lb_Correct.setAlignment(Qt.AlignCenter)

layout_res = QVBoxLayout()

layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)

AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# ---------------- ЛЭЙАУТЫ ----------------

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question)

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)

window.setLayout(layout_card)

# ---------------- ФУНКЦИИ ----------------

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')

    for btn in answers:
        btn.setChecked(False)


def ask(q: Question):

    lb_Question.setText(q.question)

    variants = [
        q.right_answer,
        q.wrong1,
        q.wrong2,
        q.wrong3
    ]

    shuffle(variants)

    for i in range(4):
        answers[i].setText(variants[i])

    lb_Correct.setText(q.right_answer)

    show_question()


def show_correct(result):
    lb_Result.setText(result)
    show_result()


def check_answer():

    if lb_Correct.text() == "":
        return

    for btn in answers:

        if btn.isChecked():

            if btn.text() == lb_Correct.text():
                show_correct("Правильно!")
                window.points += 1
                print(window.points)
            else:
                show_correct("Неверно!")
            break


# ---------------- СПИСОК ВОПРОСОВ ----------------

questions = []

questions.append(
    Question(
        'Какой национальности не существует?',
        'Смурфы',
        'Энцы',
        'Чулымцы',
        'Алеуты'
    )
)

questions.append(
    Question(
        'Сколько дней в неделе?',
        '7',
        '5',
        '6',
        '8'
    )
)

questions.append(
    Question(
        'Столица Франции?',
        'Париж',
        'Лондон',
        'Берлин',
        'Рим'
    )
)

# ---------------- СЧЁТЧИК ----------------

window.cur_question = -1


# ---------------- СЛЕДУЮЩИЙ ВОПРОС ----------------

def next_question():
    window.cur_question += 1
    window.total += 1
    print(window.points / window.total * 100)

    if window.cur_question >= len(questions):
        window.cur_question = 0

    q = questions[window.cur_question]

    ask(q)


# ---------------- ПОСРЕДНИК ----------------

def click_ok():

    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


# ---------------- СОБЫТИЕ ----------------

btn_OK.clicked.connect(click_ok)

# ---------------- ПЕРВЫЙ ВОПРОС ----------------

next_question()

# ---------------- ЗАПУСК ----------------

window.show()
app.exec()