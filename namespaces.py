def test_func():
    def inner_func():
        print('Я в области видимости test_func')

    inner_func() # вне 'inner_func' is not defined


test_func()
