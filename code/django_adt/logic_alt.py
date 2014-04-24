from .types import Instruction

inline_matcher = Instruction.inline_match(
    ORDER = (lambda o, oid: o.tid == oid),
    CANCEL = (lambda c, oid: c.xtid == oid),
    CANCEL_REPLACE = (lambda cr, oid: cr.xr_tid == oid))

def filter_by_oid_alt(instructions, oid):
    return list(filter(lambda i: inline_matcher(i)(i, oid),
                       instructions))