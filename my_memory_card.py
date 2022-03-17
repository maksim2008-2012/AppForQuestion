from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle, randint

class Question() :
   def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
       self.question = question
       self.right_answer = right_answer
       self.wrong1 = wrong1
       self.wrong2 = wrong2
       self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Какой хлеб пекут во Франции?', 'батон', 'черный хлеб', 'белый хлеб', 'пица'))
questions_list.append(Question('В каком месте на Земле самая жаркая погода?', 'Экватор',  'северный полюс', 'тропики', 'умереный пояс'))
questions_list.append(Question('В каком поясе расположена Россия?', 'умереный', 'тропический', 'экваториальный', 'антарктический'))
questions_list.append(Question('Где находится Южная Америка?', 'на востоке', 'на севере', 'на юге', 'на западе'))
questions_list.append(Question('Кто президент России?', 'Путин', 'Трамп', 'Байден', 'Сталин'))
questions_list.append(Question('Какого цвета нет на флаге Франции?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Какого цвета нет на флаге Германии', 'синий', 'черный', 'красный', 'желтый'))
app = QApplication([])
btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!')
 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
 
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
 
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
 
def ask(q: Question):
   ''' функция записывает значения вопроса и ответов в соответствующие виджеты,
   при этом варианты ответов распределяются случайным образом'''
   shuffle(answers) # перемешали список из кнопок, теперь на первом месте списка какая-то непредсказуемая кнопка
   answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
   answers[1].setText(q.wrong1)
   answers[2].setText(q.wrong2)
   answers[3].setText(q.wrong3)
   lb_Question.setText(q.question) # вопрос
   lb_Correct.setText(q.right_answer) # ответ
   show_question() # показываем панель вопросов
def show_correct(res):
   ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
   lb_Result.setText(res)
   show_result()
def check_answer():
   ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
   if answers[0].isChecked():
       # правильный ответ!
       show_correct('Правильно!')
       window.score += 1
       print ('Всего вопросов: ', window.total, '\n Правильных ответов: ', window.score)
       print('Рейтинг :', (window.score / window.total)*100, '%')
   else:
       if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
           # неправильный ответ!
           show_correct('Неверно!')
           print('Рейтинг :', (window.score / window.total)*100, '%')
def next_question():
   ''' задает следующий вопрос из списка '''
   # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
   # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
   # мы заведем (ниже) свойство window.cur_question.
   window.total += 1
   cur_question = randint(0, len(questions_list)-1 )# переходим к следующему вопросу
 
   q = questions_list[cur_question] # взяли вопрос
   ask(q) # спросили
def click_OK():
   ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
   if btn_OK.text() == 'Ответить':
       check_answer() # проверка ответа
   else:
       next_question() # следующий вопрос
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
# текущий вопрос из списка сделаем свойством объекта "окно", так мы сможем спокойно менять его из функции:
window.cur_question = -1    # по-хорошему такие переменные должны быть свойствами,
                           # только надо писать класс, экземпляры которого получат такие свойства,
                           # но python позволяет создать свойство у отдельно взятого экземпляра
btn_OK.clicked.connect(click_OK) # по нажатии на кнопку выбираем, что конкретно происходит
# все настроено, осталось задать вопрос и показать окно:
window.total = 0
window.score = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
 
