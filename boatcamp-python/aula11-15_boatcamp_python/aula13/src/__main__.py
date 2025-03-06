import schedule
import time
from lib.classes.FilesSources import FilesSources
from lib.classes.CsvSource import CsvSource
from lib.classes.TxtSource import TxtSource
from lib.classes.JsonSource import JsonSource


def check_for_new_file():
    csv_source.check_for_new_files()
    txt_source.check_for_new_files()
    json_source.check_for_new_files()

schedule.every(10).seconds.do(check_for_new_file)

csv_source = CsvSource()
txt_source = TxtSource()
json_source = JsonSource()


while True:
    schedule.run_pending()
    time.sleep(1)  # Aguarda 1 segundo para que o loop não consuma muito processamento
