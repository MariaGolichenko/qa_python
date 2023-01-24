from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # tests def __init__
    # books_rating
    def test_books_rating_true(self):
        collector = BooksCollector()
        assert collector.books_rating == {}

    # favorites
    def test_favorites_true(self):
        collector = BooksCollector()
        assert collector.favorites == []

    # tests def add_new_book
    # нельзя добавить книги с одинаковыми названиями
    def test_add_new_book_add_identical_names_books_false(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')

        assert len(collector.get_books_rating()) == 1

    # рейтинг добавленной книги = 1
    def test_add_new_book_books_rating_is_1(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')

        assert collector.books_rating['Гордость и предубеждение'] == 1

    # tests def set_book_rating
    # установка рейтинга 5 для книги
    def test_set_book_rating_add_rating_5_add(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', 5)

        assert collector.books_rating['Гордость и предубеждение'] == 5

    # не устанавливается рейтинг 0 (меньше 1)
    def test_set_book_rating_add_rating_less_1_not_add(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', 0)

        assert collector.books_rating['Гордость и предубеждение'] != 0 \
               and collector.books_rating['Гордость и предубеждение'] == 1

    # не устанавливается рейтинг 11 (больше 10)
    def test_set_book_rating_add_rating_more_10_not_add(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', 11)

        assert collector.books_rating['Гордость и предубеждение'] != 11 \
               and collector.books_rating['Гордость и предубеждение'] == 1


    # не устанавливается рейтинг "пять" (нельзя передать строку)
    def test_set_book_rating_add_rating_str_not_add(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', "пять")

        assert collector.books_rating['Гордость и предубеждение'] != "пять" \
               and collector.books_rating['Гордость и предубеждение'] == 1


    # tests def get_book_rating
    # получение рейтинга книги по имени
    def test_get_book_rating_get_book_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', 7)

        assert collector.get_book_rating('Гордость и предубеждение') == 7

    # tests get_books_with_specific_rating
    # выводим список книг с опреденеленным рейтингом
    def test_get_books_with_specific_rating_is_5(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Война и мир')
        collector.add_new_book('Книжный вор')
        collector.add_new_book('Самый богатый человек в Вавилоне')
        collector.set_book_rating('Гордость и предубеждение', 5)
        collector.set_book_rating('Книжный вор', 5)
        collector.set_book_rating('Самый богатый человек в Вавилоне', 7)

        assert 'Гордость и предубеждение' and 'Книжный вор' in collector.get_books_with_specific_rating(5)

    # tests get_books_rating
    # получить словарь books_rating
    def test_get_books_rating_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')

        assert collector.books_rating == {'Гордость и предубеждение': 1}

    # tests add_book_in_favorites
    # добавление книги в избранное
    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')

        assert collector.favorites == ['Гордость и предубеждение']

    # нельзя добавить в избранное книгу, которой нет в списке
    def test_add_book_in_favorites_not_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Книжный вор')
        collector.add_book_in_favorites('Гордость и предубеждение')

        assert 'Гордость и предубеждение' not in collector.favorites

    # tests delete_book_from_favorites
    # удаление книги из избранного
    def test_delete_book_from_favorites_del(self):
        collector = BooksCollector()

        collector.add_new_book('Книжный вор')
        collector.add_book_in_favorites('Книжный вор')
        collector.delete_book_from_favorites('Книжный вор')

        assert 'Книжный вор' not in collector.get_list_of_favorites_books()

    # tests get_list_of_favorites_books
    # получение пустого списка избранных книг
    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Книжный вор')
        collector.add_new_book('Война и мир')

        assert collector.get_list_of_favorites_books() == []

    # получение списка избранных книг из 3 книг
    def test_get_list_of_favorites_books_trie_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книжный вор')
        collector.add_new_book('Война и мир')
        collector.add_new_book('Преступление и наказание')
        collector.add_book_in_favorites('Книжный вор')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Преступление и наказание')

        assert collector.get_list_of_favorites_books() == ['Книжный вор', 'Война и мир', 'Преступление и наказание']




