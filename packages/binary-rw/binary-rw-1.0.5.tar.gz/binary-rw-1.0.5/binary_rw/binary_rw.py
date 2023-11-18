import struct


class BinaryReader:
	def __init__(self, path: str):
		if not isinstance(path, str):
			raise TypeError(f"path must be an string.")
		self.file = open(path, 'rb')

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, tb):
		self.file.close()

	def close(self):
		self.file.close()

	def read_sbyte(self):
		return struct.unpack('b', self.file.read(1))[0]

	def read_byte(self):
		return self.file.read(1)[0]

	def read_bool(self):
		return bool(self.file.read(1)[0])

	def read_int16(self):
		return struct.unpack('h', self.file.read(2))[0]

	def read_uint16(self):
		return struct.unpack('H', self.file.read(2))[0]

	def read_int32(self):
		return struct.unpack('i', self.file.read(4))[0]

	def read_uint32(self):
		return struct.unpack('I', self.file.read(4))[0]

	def read_int64(self):
		return struct.unpack('q', self.file.read(8))[0]

	def read_uint64(self):
		return struct.unpack('Q', self.file.read(8))[0]

	def read_single(self):
		return struct.unpack('f', self.file.read(4))[0]

	def read_double(self):
		return struct.unpack('d', self.file.read(8))[0]

	def read_7bit_encoded_int32(self):
		count = 0
		shift = 0
		while True:
			if shift >= 35:
				raise Exception("Can't read from file. 7 bit encoded int may not be longer than 5 bytes")
			byte = self.read_byte()
			count |= (byte & 0x7F) << shift
			shift += 7
			if byte & 0x80 == 0:
				break

		if count < 2147483648:
			return count
		if count < 4294967296:
			return count - 4294967296
		raise Exception("Can't read from file. 7 bit encoded int may not be larger than 2147483647 "
						"nor smaller than -2147483648")

	def read_string(self):
		length = self.read_7bit_encoded_int32()
		if length < 0:
			raise Exception("Can't read from file. Length of string may not be negative number")
		return self.file.read(length).decode("utf-8")


class BinaryWriter:
	def __init__(self, path: str):
		if not isinstance(path, str):
			raise TypeError(f"path must be an string.")
		self.file = open(path, 'wb')

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, tb):
		self.file.close()

	def close(self):
		self.file.close()

	def write_sbyte(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 127:
			raise ValueError(f"data may not be above 127.")
		if data < -128:
			raise ValueError(f"data may not be below -128.")
		self.file.write(struct.pack("b", data))

	def write_byte(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 255:
			raise ValueError(f"data may not be above 255.")
		if data < 0:
			raise ValueError(f"data may not be below 0.")
		self.file.write(struct.pack("B", data))

	def write_bool(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data != 0 and data != 1:
			raise ValueError(f"data must be true or false")
		self.write_byte(data)

	def write_int16(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 32767:
			raise ValueError(f"data may not be above 32767.")
		if data < -32768:
			raise ValueError(f"data may not be below -32768.")
		self.file.write(struct.pack("h", data))

	def write_uint16(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 65535:
			raise ValueError(f"data may not be above 65535.")
		if data < 0:
			raise ValueError(f"data may not be below 0.")
		self.file.write(struct.pack("H", data))

	def write_int32(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 2147483647:
			raise ValueError(f"data may not be above 2147483647.")
		if data < -2147483648:
			raise ValueError(f"data may not be below -2147483648.")
		self.file.write(struct.pack("i", data))

	def write_uint32(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 4294967295:
			raise ValueError(f"data may not be above 4294967295.")
		if data < 0:
			raise ValueError(f"data may not be below 0.")
		self.file.write(struct.pack("I", data))

	def write_int64(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 9223372036854775807:
			raise ValueError(f"data may not be above 9223372036854775807.")
		if data < -9223372036854775808:
			raise ValueError(f"data may not be below -9223372036854775808.")
		self.file.write(struct.pack("q", data))

	def write_uint64(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 18446744073709551615:
			raise ValueError(f"data may not be above 18446744073709551615.")
		if data < 0:
			raise ValueError(f"data may not be below 0.")
		self.file.write(struct.pack("Q", data))

	def write_single(self, data: float):
		if not isinstance(data, float):
			raise TypeError(f"data must be an float.")
		self.file.write(struct.pack("f", data))

	def write_double(self, data: float):
		if not isinstance(data, float):
			raise TypeError(f"data must be an float.")
		self.file.write(struct.pack("d", data))

	def write_7bit_encoded_int32(self, data: int):
		if not isinstance(data, int):
			raise TypeError(f"data must be an integer.")
		if data > 2147483647:
			raise ValueError(f"data may not be above 2147483647.")
		if data < -2147483648:
			raise ValueError(f"data may not be below -2147483648.")
		if data < 0:
			data += 4294967296
		while data >= 0x80:
			self.write_byte(data & 0x7F | 0x80)
			data >>= 7
		self.write_byte(data)

	def write_string(self, data: str):
		if not isinstance(data, str):
			raise TypeError(f"data must be an string.")
		data = data.encode("utf-8")
		if len(data) > 2147483647:
			raise ValueError("data mey not be longer than 2147483647 bytes")
		self.write_7bit_encoded_int32(len(data))
		self.file.write(data)
