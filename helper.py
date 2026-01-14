from faker import Faker


faker =  Faker()

def generate_registration_data_invalid():
    
    password = faker.password(length = 5)
    return password