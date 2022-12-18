class LoggerSingleton:
    __instance: 'LoggerSingleton' = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def log(self, data: str):
        print(data)
