from rhetoric.adt import adt
from .models import Order, Cancel, CancelReplace

class Instruction(adt):
    ORDER = Order
    CANCEL = Cancel
    CANCEL_REPLACE = CancelReplace
