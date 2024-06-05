import requests


class Test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    def test_new_random_joke(self):
        """Создание случайной шутки"""
        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        assert result.status_code == 200
        print("Статус-код: " + str(result.status_code))
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        assert check_info == []
        print(check_info)



random_joke = Test_new_joke()
random_joke.test_new_random_joke()
