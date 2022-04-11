import greeting as gr
import model as sum
import model_mult as m
import model_division as d
import model_subtracting as sub

import view

def button_click():
    print(gr.greet())
    number = gr.type_selection()
    if number == 1:
        value_a = view.get_complex_value()
        value_b = view.get_complex_value()
    elif number == 2:
        value_a = view.get_value()
        value_b = view.get_value()
    else:
        print('некорректный выбор: выберетe 1 или 2')
    action = view.get_action()
    if action == '+':
        sum.init(value_a, value_b)
        result = sum.result()
    elif action == '*':
        m.init(value_a, value_b)
        result = m.result()
    elif action == '-':
        sub.init(value_a, value_b)
        result = sub.result()
    elif action == '/':
        d.init(value_a, value_b)
        result = d.result()
    else:
        return 'ошибка'
    view.view_data(result)