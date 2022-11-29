
'''                                     ////////////////////////////
                                        /    convert file from csv /
                                        /   to txt(project 3 month /
                                        /      back ago)           /
@                                        ////////////////////////////                                               '''
import colorama
from colorama import Fore as f

colorama.init()

class ConverteCSVtoTXT:

    def __init__(self, path: str, name: str):
        self._path = path
        self._name = name
        self._finish_message()

    def convert_to_txt(self) -> str:
        with open(f'conv_files\{self._name}.txt', 'w', encoding='utf-8') as txt_file:
            for i in self._parse_csv_file():
                txt_file.write(i)
        txt_file.close()
        
        return ''

    def _parse_csv_file(self) -> list:
        with open(self._path, 'r') as csv_file:
            return csv_file.readlines()

    def _finish_message(self):
        print(f.GREEN + '[*]File converted!')
        input(f.WHITE + 'Click anything button....')

