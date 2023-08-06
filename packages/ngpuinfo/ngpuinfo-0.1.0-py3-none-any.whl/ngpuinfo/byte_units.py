

class ByteUnits(object):

    PREFIX_SEQUENCE = "-KMGTPEZY"

    def __init__(self, prefix, is_binary, is_byte):
        super(ByteUnits, self).__init__()
        self.is_byte = is_byte
        self.is_binary = is_binary
        self.prefix = prefix

    def __repr__(self):
        s0 = self.PREFIX_SEQUENCE[self.prefix]
        if s0 == '-':
            s0 = ''
        s1 = 'i' if self.is_binary else ''
        s2 = 'B' if self.is_byte else 'b'
        return s0 + s1 + s2

    def from_unit(self, number, unit):
        middle_number = self.__from_unit(number, unit)
        return self.__to_unit(middle_number, self)

    def to_unit(self, number, unit):
        middle_number = self.__from_unit(number, self)
        return self.__to_unit(middle_number, unit)

    @classmethod
    def __from_unit(cls, number, unit):
        ret = 1
        for _ in range(unit.prefix):
            ret = ret * (1024 if unit.is_binary else 1000)
        if unit.is_byte:
            ret *= 8
        return number * ret

    @classmethod
    def __to_unit(cls, number, unit):
        ret = number
        if unit.is_byte:
            ret /= 8
        for _ in range(unit.prefix):
            ret = ret / (1024 if unit.is_binary else 1000)
        return ret

    @classmethod
    def parse_unit(cls, unit_str: str):
        unit_str = unit_str.strip()
        if unit_str == '':
            return ByteUnits(0, 0, 0)
        pos = 1
        if unit_str[-pos] == 'b':
            is_byte = 0
        elif unit_str[-pos] == 'B':
            is_byte = 1
        else:
            raise ValueError("Illegal unit: %s" % unit_str)
        pos += 1
        if pos > len(unit_str):
            return ByteUnits(0, 0, is_byte)
        if unit_str[-pos] == 'i':
            is_binary = 1
            pos += 1
        else:
            is_binary = 0
        if pos > len(unit_str):
            return ByteUnits(0, is_binary, is_byte)
        prefix = cls.PREFIX_SEQUENCE.find(unit_str[-pos])
        if prefix == -1 or pos < len(unit_str):
            raise ValueError("Illegal unit: %s" % unit_str)
        return ByteUnits(prefix, is_binary, is_byte)

    @classmethod
    def parse_value(cls, value: str):
        try:
            return int(value)
        except:
            number = 0
            pos = 0
            value = value.strip()
            while pos < len(value):
                if '0' <= value[pos] <= '9':
                    number = 10 * number + ord(value[pos]) - ord('0')
                else:
                    break
                pos += 1
            return ByteUnits.B.from_unit(number, cls.parse_unit(value[pos:]))


for p in range(len(ByteUnits.PREFIX_SEQUENCE)):
    for i in range(2):
        for b in range(2):
            bu = ByteUnits(p, i, b)
            setattr(ByteUnits, bu.__repr__(), bu)
