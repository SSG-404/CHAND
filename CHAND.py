# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))