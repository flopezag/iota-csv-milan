from config.settings import CSV_FILES
from processor.ngsi import NGSI


if __name__ == '__main__':
    '''
    Main: Load file(s) and upload content to Context Broker
    '''
    ngsi = NGSI()

    # Read each file and upload their content into Context Broker
    result = [ngsi.process(file=csv_file) for csv_file in CSV_FILES]
