import requests


class JsTestTask():
    MODEL_PHONE_FOR_TEST = "Alcatel"

    def __init__(self, name1):
        self.name = name1['name']
        self.image = name1['image']
        self.price = name1['price']

    def __str__(self):
        return f"phone[{self.name}:{self.image}:{self.price}]"

    __repr__ = __str__

    def js_test_task(self):
        response = requests.get("https://www.lenvendo.ru/api/js-test-task/",
                                params=self).json()
        tel_list = []
        for i in response['products']:
            tel_list.append(JsTestTask(i))
        return tel_list

    def check_name_tel(self):
        for i in self:
            assert JsTestTask.MODEL_PHONE_FOR_TEST in i.name

    def sort_by_name(self):
        return self.name

    def sort_by_price(self):
        return self.price

    def check_sort_tel(self):
        sorted_telepnons_li = sorted(self, key=JsTestTask.sort_by_name)
        assert self == sorted_telepnons_li
