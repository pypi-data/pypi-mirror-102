import lzma
from hashlib import md5

import lzham
import zstandard

from sc_compression.signatures import Signatures
from sc_compression.utils.writer import Writer


class Compressor(Writer):
    lzham_filters = {
        'dict_size_log2': 18
    }
    lzma_filters = [
        {
            "id": lzma.FILTER_LZMA1,
            "dict_size": 256 * 1024,
            "lc": 3,
            "lp": 0,
            "pb": 2,
            "mode": lzma.MODE_NORMAL
        },
    ]

    def __init__(self):
        super().__init__('little')

    def compress(self, data, signature: int) -> bytes:
        uncompressed_size = len(data)

        if signature is Signatures.NONE:
            return data
        elif (Signatures.LZMA | Signatures.SIG) & signature:
            compressed = lzma.compress(data, format=lzma.FORMAT_ALONE, filters=self.lzma_filters)

            self.write(compressed[:5])

            self.writeInt32(uncompressed_size)

            self.write(compressed[13:])

            compressed = self.buffer
        elif Signatures.SCLZ & signature:
            compressed = lzham.compress(data, filters=self.lzham_filters)

            self.write(b'SCLZ')
            self.writeUByte(18)
            self.writeInt32(uncompressed_size)
            self.write(compressed)

            compressed = self.buffer
        elif (Signatures.SC | Signatures.ZSTD) & signature:
            compressor = zstandard.ZstdCompressor()
            compressed = compressor.compress(data)
        else:
            raise TypeError('Unknown Signature!')

        super().__init__('big')
        if (Signatures.SC | Signatures.SCLZ | Signatures.ZSTD) & signature:
            data_hash = md5(data)

            self.write(b'SC')
            self.writeInt32(1)
            self.writeInt32(16)
            compressed = self.buffer + data_hash.digest() + compressed
        elif signature == Signatures.SIG:
            self.write(b'Sig:')
            self.write(b'\x00' * 64)  # sha64
            compressed = self.buffer + compressed

        return compressed
