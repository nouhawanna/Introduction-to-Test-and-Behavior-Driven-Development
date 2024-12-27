from faker import Faker

fake = Faker()

def generate_fake_product():
    """Generate a fake product with random attributes."""
    return {
        "id": fake.unique.random_int(min=1, max=1000),
        "name": fake.word().capitalize(),
        "category": fake.random_element(elements=("Electronics", "Books", "Clothing", "Toys")),
        "price": round(fake.random_number(digits=4, fix_len=True) / 100, 2),
        "quantity": fake.random_int(min=1, max=100),
        "available": fake.boolean(),
    }

# Example usage
if __name__ == "__main__":
    # Generate 5 fake products for testing
    for _ in range(5):
        print(generate_fake_product())
