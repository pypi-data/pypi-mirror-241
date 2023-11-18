from base64 import b64encode,b64decode,b32hexencode,b32hexdecode,b85encode,b85decode,b16encode,b16decode,a85encode,a85decode,b32encode,b32decode
def Zenc(msg):
    message_bytes = msg.encode('utf-8')
    b64 = b64encode(message_bytes)
    b32hex = b32hexencode(b64)
    b85 = b85encode(b32hex)
    b16 = b16encode(b85)
    b32 = b32encode(b16)
    a85 = a85encode(b32)
    out = a85.decode('ascii')
    return out
def Zdec(b64BYTE):
    base64_bytes = b64BYTE.encode('utf-8')
    a85 = a85decode(base64_bytes)
    b32 = b32decode(a85)
    b16 = b16decode(b32)
    b85 = b85decode(b16)
    b32hex = b32hexdecode(b85)
    b64 = b64decode(b32hex)
    out = b64.decode('utf-8')
    return out

def NENC(msg):
    msg_bytes = msg.encode("utf-8")
    b64 = b64encode(msg_bytes)
    out = b64.decode("ascii")
    return out
def NDEC(b64B):
    b = b64B.encode("utf-8")
    b64 = b64decode(b)
    out = b64.decode("utf-8")
    return out



# b64
# b32hex
# b85
# b16
# b32
# a85

