#
# Copyright (c) 2019 UAVCAN Development Team
# This software is distributed under the terms of the MIT License.
# Author: Pavel Kirienko <pavel.kirienko@zubax.com>
#

"""
This module contains implementations of various CRC algorithms used by the transport implementations.
"""

from ._base import CRCAlgorithm as CRCAlgorithm
from ._crc16_ccitt import CRC16CCITT as CRC16CCITT
from ._crc32c import CRC32C as CRC32C
