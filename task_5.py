class TestCase:

    def __init__(self):
        self.steps = {}
        self.result = None

    def set_step(self, step_number: int, step_text: str):
        self.steps[step_number] = step_text
        
    def delete_step(self, step_number: int):
        self.steps.pop(step_number)

    def set_result(self, result: str):
        self.result = result

    def get_test_case(self):
        result_step_info = {
            "Шаги": self.steps,
            "Ожидаемый результат": self.result
        }
        print(result_step_info)

test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 