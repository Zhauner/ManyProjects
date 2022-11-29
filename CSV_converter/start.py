from CSV_module import ConverteCSVtoTXT
import colorama
from colorama import Fore as f

colorama.init()

print(f.CYAN + '''  ///////////////////////////////////
 //     INPUT  FILE  PATH         //
///////////////////////////////////\n''')



path = str(input('[PATH]:>')).replace('\\', '/')
name = str(input('[Name of file]:>'))

cnvrt = ConverteCSVtoTXT(path, name)

cnvrt.convert_to_txt()
