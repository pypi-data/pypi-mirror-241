class ProducerModel:
    def __init__(self, key: any = None, value: any = None, headers: any = None):
        self.__key = key
        self.__value = value
        self.__headers = headers

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, headers):
        self.__headers = headers
