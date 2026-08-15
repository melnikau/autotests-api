import time

def get_random_email() -> str:
    return f"test{time.time()}@example.com"

def get_random_lastname() -> str:
    return f"lastName{time.time()}"

def get_random_firstname() -> str:
    return f"firstName{time.time()}"

def get_random_middlename() -> str:
    return f"middleName{time.time()}"

# print(time.time())