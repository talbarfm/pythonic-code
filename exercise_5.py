def end_other_v1(a, b):
    a = a.lower()
    b = b.lower()
    if len(a) < len(b):
        if b[-1 * len(a):] == a:
            return True
        else:
            return False
    else:
        if a[-1 * len(b):] == b:
            return True
        else:
            return False
