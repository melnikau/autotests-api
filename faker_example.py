from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())

data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}

print(data)
