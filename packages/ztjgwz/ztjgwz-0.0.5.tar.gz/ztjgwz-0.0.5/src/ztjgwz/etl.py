import abc


class ETLBase:
    def __enter__(self):
        # Code to be executed when entering the 'with' block
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()

    @abc.abstractmethod
    def save(self):
        pass
