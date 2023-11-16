class FifthItnConverter:
    regex = '[0-9]{5}'
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)

class FloatConverter:
    regex = r'[+-]?(\d*\.)?\d+'
    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)