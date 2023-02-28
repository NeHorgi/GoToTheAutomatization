import requests
import pytest
from dataclasses import dataclass
from bs4 import BeautifulSoup
from typing import List

parameters_for_test = [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9]


@pytest.fixture
def parsing_a_table() -> List:

    url = requests.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')
    soup = BeautifulSoup(url.text, "html.parser")
    wiki_table = soup.table

    parsed_table_from_wiki = []

    for table_row in wiki_table.find_all('tr'):
        string_from_table = []
        for table_row_column in table_row.find_all('td'):
            while True:
                if table_row_column.select_one('sup'):
                    table_row_column.select_one('sup', class_='reference').decompose()
                else:
                    break
            string_from_table.append(table_row_column.get_text(strip=True))
        if string_from_table:
            parsed_table_from_wiki.append(string_from_table)

    for table_row in parsed_table_from_wiki:
        popularity_in_row = table_row[1].split(' ')
        popularity_in_row = popularity_in_row[0].replace(',', '')
        popularity_in_row = popularity_in_row.replace('.', '')
        table_row[1] = int(popularity_in_row)

    @dataclass
    class CompanyInfo:
        name: str
        popularity: int
        front: str
        back: str
        database: str
        notes: str

    data_from_parsed_table = []

    for table_row in parsed_table_from_wiki:
        data_row_from_table = CompanyInfo(*[table_row_column for table_row_column in table_row])
        data_from_parsed_table.append(data_row_from_table)

    return data_from_parsed_table


@pytest.mark.parametrize('parameter', parameters_for_test)
def test_parametrize_task_1(parameter, parsing_a_table):

    error = []

    for table_row in parsing_a_table:

        if parameter > table_row.popularity:
            error.append(table_row)

    assert not error, '\n'.join([f'{table_row.name} (Frontend:{table_row.front}|Backend:{table_row.back}) has {table_row.popularity} unique visitors per month. (Expected less than {parameter})' for table_row in error])


