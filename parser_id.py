import requests
from bs4 import BeautifulSoup


def get_id_caf(kyrs: str, formob: str):
    """
    Параметры:
        kyrs (str): Номер курса.
        formob (str): Форма обучения. Может принимать следующие значения:
            - 'Д' - дневная
            - 'В' - вечерняя
            - 'З' - заочная
            - '2' - второе высшее
            - 'М' - магистратура
            - 'У' - дистанционная
        """

    params = {
        'formob': formob,
        'kyrs': kyrs,
    }
    url = 'https://raspis.rggu.ru/rasp/2.php'
    response = requests.post(url=url, data=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    options = soup.find_all('option')
    groups_dict = {}
    for option in options:
        value = int(option['value'])
        text = option.get_text().split(' (')[0]
        groups_dict[value] = text

    dict_name = f"dict_{kyrs}kyrs{formob}"
    filename = f"{kyrs}kyrs{formob}.py"

    file_content = f"{dict_name} = {groups_dict}"

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(file_content)


if __name__ == '__main__':
    get_id_caf('3', 'Д')
