class Calculator():
    def __init__(self,*a) -> None:
        pass
    def __enter__(self):
        self.error = None
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.error = exc_type
        return True

with Calculator() as c:
    print(1-1)
    print(2/0)

print(c.error,"t")