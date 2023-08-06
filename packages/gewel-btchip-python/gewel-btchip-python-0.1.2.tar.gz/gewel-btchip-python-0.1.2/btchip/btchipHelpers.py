"""
*******************************************************************************
*   BTChip Bitcoin Hardware Wallet Python API
*   (c) 2014 BTChip - 1BTChip7VfTnrPra5jqci7ejnMguuHogTn
*   (c) 2021 Gewel Core Developers
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
*   Unless required by applicable law or agreed to in writing, software
*   distributed under the License is distributed on an "AS IS" BASIS,
*   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*   limitations under the License.
********************************************************************************
"""

import decimal
import re

# from pycoin
ADAMS_PER_COIN = decimal.Decimal(1e8)
COIN_PER_ADAM = decimal.Decimal(1)/ADAMS_PER_COIN

def adams_to_gwl(adams_count):
    if adams_count == 0:
        return decimal.Decimal(0)
    r = adams_count * COIN_PER_ADAM
    return r.normalize()

def gwl_to_adams(gwl):
    return int(decimal.Decimal(gwl) * ADAMS_PER_COIN)
# /from pycoin

def writeUint32BE(value, buffer):
	buffer.append((value >> 24) & 0xff)
	buffer.append((value >> 16) & 0xff)
	buffer.append((value >> 8) & 0xff)
	buffer.append(value & 0xff)
	return buffer

def writeUint32LE(value, buffer):
	buffer.append(value & 0xff)
	buffer.append((value >> 8) & 0xff)
	buffer.append((value >> 16) & 0xff)
	buffer.append((value >> 24) & 0xff)
	return buffer

def writeHexAmount(value, buffer):
	buffer.append(value & 0xff)
	buffer.append((value >> 8) & 0xff)
	buffer.append((value >> 16) & 0xff)
	buffer.append((value >> 24) & 0xff)
	buffer.append((value >> 32) & 0xff)
	buffer.append((value >> 40) & 0xff)
	buffer.append((value >> 48) & 0xff)
	buffer.append((value >> 56) & 0xff)
	return buffer

def writeHexAmountBE(value, buffer):
	buffer.append((value >> 56) & 0xff)
	buffer.append((value >> 48) & 0xff)
	buffer.append((value >> 40) & 0xff)
	buffer.append((value >> 32) & 0xff)
	buffer.append((value >> 24) & 0xff)
	buffer.append((value >> 16) & 0xff)
	buffer.append((value >> 8) & 0xff)
	buffer.append(value & 0xff)
	return buffer

def parse_bip32_path(path):
	if len(path) == 0:
		return bytearray([ 0 ])
	result = []
	elements = path.split('/')
	if len(elements) > 10:
		raise BTChipException("Path too long")
	for pathElement in elements:
		element = re.split('\'|h|H', pathElement)
		if len(element) == 1:
			writeUint32BE(int(element[0]), result)
		else:
			writeUint32BE(0x80000000 | int(element[0]), result)
	return bytearray([ len(elements) ] + result)
