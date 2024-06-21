def as_int(v):
    return int(v)

def from_int(v):
    return v

def as_int32(v):
    return as_int(v)

def from_int32(v):
    return from_int(v)

def as_int64(v):
    return as_int(v)

def from_int64(v):
    return from_int(v)

def as_string(v):
    return str(v)

def from_string(v):
    return v

def as_bool(v):
    return str(v).lower() in ['true', '1', 't', 'y', 'yes']

def from_bool(v):
    return v

def as_float(v):
    return float(v)

def from_float(v):
    return v

def as_float32(v):
    return as_float(v)

def from_float32(v):
    return from_float(v)

def as_float64(v):
    return as_float(v)

def from_float64(v):
    return from_float(v)
