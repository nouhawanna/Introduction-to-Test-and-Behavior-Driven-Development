from behave import when, then
import requests

# Base URL for API calls (adjust it to your actual API URL)
BASE_URL = 'http://localhost:5000/products'


@when('I send a GET request to "{url}"')
def step_impl(context, url):
    """Send a GET request to the specified URL."""
    context.response = requests.get(f'{BASE_URL}{url}')


@when('I send a PUT request to "{url}" with the updated data')
def step_impl(context, url):
    """Send a PUT request to the specified URL with the updated data."""
    context.response = requests.put(f'{BASE_URL}{url}', json=context.table.rows[0])


@when('I send a DELETE request to "{url}"')
def step_impl(context, url):
    """Send a DELETE request to the specified URL."""
    context.response = requests.delete(f'{BASE_URL}{url}')


@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    """Check if the response status code matches the expected value."""
    assert context.response.status_code == int(status_code)


@then('the response should contain {num} products')
def step_impl(context, num):
    """Verify that the response contains the specified number of products."""
    products = context.response.json()
    assert len(products) == int(num)


@then('the response should contain the product "{product_name}"')
def step_impl(context, product_name):
    """Check if the response contains a product with the given name."""
    products = context.response.json()
    product_names = [product['name'] for product in products]
    assert product_name in product_names


@then('the response should contain the updated product "{product_name}"')
def step_impl(context, product_name):
    """Verify that the response contains the updated product."""
    product = context.response.json()
    assert product['name'] == product_name


@then('the product with ID {product_id} should no longer exist')
def step_impl(context, product_id):
    """Verify that the product with the given ID no longer exists."""
    response = requests.get(f'{BASE_URL}/{product_id}')
    assert response.status_code == 404


@then('the response should contain 1 product')
def step_impl(context):
    """Check that the response contains exactly 1 product."""
    products = context.response.json()
    assert len(products) == 1


@then('the products should include "{product_name}"')
def step_impl(context, product_name):
    """Verify that the list of products includes the specified product."""
    products = context.response.json()
    product_names = [product['name'] for product in products]
    assert product_name in product_names
