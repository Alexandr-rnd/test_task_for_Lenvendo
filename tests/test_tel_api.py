from src.JsTestTask import JsTestTask


def test_get_api_check_name(telephone_filters):
    tel_list = JsTestTask.js_test_task(telephone_filters)
    JsTestTask.check_name_tel(tel_list)


def test_get_api_sort(telephone_filters):
    tel_list = JsTestTask.js_test_task(telephone_filters)
    JsTestTask.check_sort_tel(tel_list)
