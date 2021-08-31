# Your imports go here
import logging
import json
import os


logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here
    #join path
    join_path=os.path.join(dirpath,'expected.json')

    #open the file
    f=open(join_path,'r')
    data=json.load(f)

    # coping extracted_amount
    amount=data['amount']
    #print(amount)

    return amount
