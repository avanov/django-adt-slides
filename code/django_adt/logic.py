from .types import Instruction

@Instruction.ORDER('filter_by_oid')
def filter_order_by_oid(order, oid):
    return order.tid == oid

@Instruction.CANCEL('filter_by_oid')
def filter_cancel_by_oid(cancel, oid):
    return cancel.xtid == oid

@Instruction.CANCEL_REPLACE('filter_by_oid')
def filter_cancel_replace_by_oid(cr, oid):
    return cr.xr_tid == oid

def filter_by_oid(instructions, oid):
    return list(filter(
        lambda i: Instruction.match(i)['filter_by_oid'](i, oid),
        instructions))
