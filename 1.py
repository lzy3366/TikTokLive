import base64
import gzip
from io import BytesIO

from TikTokLive.proto import WebcastResponse

d = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\x12\xb26476\xb14\xb4\xb00\xb5\xb446\x8f771541\xb4475362637\xb40\xb4\x8c7\x8c7\x80\x8a\x9b\x99\x18\x1a\x98\x9a\x98\x18\x9a\x1a\x99Y\x18\xc6\x1bH\xbc`WXx\xf3q\xe7~#-F]\x07~\x00\x00\x00\x00\xff\xff\x01\x00\x00\xff\xff\xdf\xfe\x05\xe9L\x00\x00\x00'

print(base64.b64encode(d))
with gzip.GzipFile(fileobj=BytesIO(d), mode='rb') as f:
    print(WebcastResponse().parse(f.read()))
