import json
import random
from datetime import timedelta, datetime
from dotenv import load_dotenv

load_dotenv()

def get_pos_ai_analytics_transaction_data() -> str:
    """
    Retrieves current AI point-of-sale (POS) transaction data as a JSON string from a POS AI analytics co-companion system. The data will indicate all items part of the transaction in an array. 
    """
    seconds_delta = timedelta(seconds=65)
    start = "\"" + str(datetime.now().strftime("%m-%d-%Y %H:%M:%S")) + "\""
    end = "\"" + str((datetime.now() + seconds_delta).strftime("%m-%d-%Y %H:%M:%S")) + "\""
    
    single_item = """{
    "items_recognized": [
        {
            "detected_at": """ + f"{start}" + """,
            "event_type": "yolo",
            "item_name": "bottle"
        }
    ]}"""

    two_items = """{
    "items_recognized": [
        {
            "detected_at": """ + f"{start}" + """,
            "event_type": "yolo",
            "item_name": "bottle"
        },
        {
            "detected_at": """ + f"{end}" + """,
            "event_type": "dfine",
            "item_name": "bannana"
        }
    ]}"""

    items = [ single_item, two_items ]
    item_idx = random.randint(0, 1)

    items_info = items[item_idx]
    print("DEBUG AI: ", item_idx, items_info)
    return items_info



def get_pos_transaction_data() -> str:
    """
    Retrieves current traditional point-of-sale (POS) transaction data as a JSON string from a POS system. The data will indicate all items part of the transaction in an array. 
    """
    seconds_delta = timedelta(seconds=65)
    start = "\"" + str(datetime.now().strftime("%m-%d-%Y %H:%M:%S")) + "\""
    end = "\"" + str((datetime.now() + seconds_delta).strftime("%m-%d-%Y %H:%M:%S")) + "\""

    single_item = """{
    "item_checkouts": [
        {
            "transaction_at": """ + f"{start}" + """,
            "event_type": "scanned",
            "item_name": "bottle"
        }
    ]}"""

    two_items = """{
    "item_checkouts": [
        {
            "transaction_at": """ + f"{start}" + """,
            "event_type": "scanned",
            "item_name": "bottle"
        },
        {
            "transaction_at": """ + f"{end}" + """,
            "event_type": "weighed",
            "item_name": "bannana"
        }
    ]}"""

    items = [ single_item, two_items ]
    item_idx = random.randint(0, 1)

    transaction_info = items[item_idx]
    print("DEBUG POS: ", item_idx, transaction_info)
    return transaction_info


#get_pos_ai_analytics_transaction_data(datetime.now())
#get_pos_transaction_data(datetime.now())
