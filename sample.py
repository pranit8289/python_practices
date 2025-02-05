def decorator(func):
    def wrapper():
        print("Payment initiated...!")
        func()
        print("Payment process completed..!")
    return wrapper


@decorator
def start_payment():
    print("Moving payment from one location to another ...!")
    print("Payment received to destination...!")


start_payment()

# how can we validate using pydantic in fast api
# 