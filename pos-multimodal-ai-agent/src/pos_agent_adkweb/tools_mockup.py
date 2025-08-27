import json
import random
from dotenv import load_dotenv

load_dotenv()

def get_pos_ai_analytics_transaction_data() -> str():
    """
    Retrieves current point-of-sale (POS) transaction data as a JSON string from a POS AI analytics co-companion system. The data will indicate the all items part of the transaction represented in an array. The below is an example of a transaction for 2 items recognized by the AI system:

    ### Example:
    {
        "items_recognized": [
            {
                "detected_at": "08-18-2025 13:16:05",
                "event_type": "yolox",
                "item_name": "bottle"
            },
            {
                "detected_at": "08-18-2025 13:16:10",
                "event_type": "dfine",
                "item_name": "bannana"
            }
    ]}
    """

    single_item = """{
    "items_recognized": [
        {
            "detected_at": "08-18-2025 13:16:05",
            "event_type": "yolo",
            "item_name": "bottle"
        }
    ]}"""

    two_items = """{
    "items_recognized": [
        {
            "detected_at": "08-18-2025 13:16:05",
            "event_type": "yolo",
            "item_name": "bottle"
        },
        {
            "detected_at": "08-18-2025 13:16:10",
            "event_type": "dfine",
            "item_name": "bannana"
        }
    ]}"""

    items = [ single_item, two_items ]
    item_idx = random.randint(0, 1)

    items_info = items[item_idx]
    return items_info



def get_pos_transaction_data() -> str:
    """
    Retrieves current point-of-sale (POS) transaction data as a JSON string from a POS system. The data will indicate all items part of the transaction represented in an array. The below is an example of a transaction for 2 items which were scanned and weighed:

    ### Example:
    {
        "item_checkouts": [
            {
                "transaction_at": "08-18-2025 13:16:05",
                "event_type": "scanned",
                "item_name": "bottle"
            },
            {
                "transaction_at": "08-18-2025 13:16:10",
                "event_type": "weighed",
                "item_name": "bannana"
            }
    ]}
    """

    single_item = """{
    "item_checkouts": [
        {
            "transaction_at": "08-18-2025 13:16:05",
            "event_type": "scanned",
            "item_name": "bottle"
        }
    ]}"""

    two_items = """{
    "item_checkouts": [
        {
            "transaction_at": "08-18-2025 13:16:05",
            "event_type": "scanned",
            "item_name": "bottle"
        },
        {
            "transaction_at": "08-18-2025 13:16:10",
            "event_type": "weighed",
            "item_name": "bannana"
        }
    ]}"""

    items = [ single_item, two_items ]
    item_idx = random.randint(0, 1)

    transaction_info = items[item_idx]
    return transaction_info
