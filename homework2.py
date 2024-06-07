def test_function():
    def inner_function():
        return "Я в области видимости функции test_function"
    inner_function()


inner_function()    # Имя infer_function не найдено потому, что оно находится в локальном пространстве имён функции test_function
