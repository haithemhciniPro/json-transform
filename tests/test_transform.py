import pytest
from src.transform import transform_data

@pytest.fixture
def sample_product_view():
    """Fixture for a valid product_view event."""
    return [{
        "product_id": "P12345",
        "user_info": {
            "username": "alice123",
            "user_email": "alice@example.com"
        },
        "event_type": "product_view",
        "event_details": {
            "product_name": "Awesome Gadget X",
            "view_timestamp": "2024-07-26T14:30:00Z",
            "location": "New York"
        }
    }]

@pytest.fixture
def sample_purchase():
    """Fixture for a valid purchase event."""
    return [{
        "product_id": "P67890",
        "user_info": {
            "username": "bob.smith",
            "user_email": "bob@work-email.com"
        },
        "event_type": "purchase",
        "event_details": {
            "order_id": "ORD-987",
            "purchase_date": "2024-07-25T18:00:00Z",
            "items": ["Awesome Gadget X", "Cool Thing Y"],
            "total_amount": 150.00
        }
    }]

def test_transform_product_view(sample_product_view):
    transformed = transform_data(sample_product_view)
    expected = [{
        "userId": "alice123",
        "userEmail": "alice@example.com",
        "activityType": "view",
        "productName": "Awesome Gadget X",
        "eventTime": "2024-07-26 14:30:00",
        "userLocation": "New York"
    }]
    assert transformed == expected

def test_transform_purchase(sample_purchase):
    transformed = transform_data(sample_purchase)
    expected = [{
        "userId": "bob.smith",
        "userEmail": "bob@work-email.com",
        "activityType": "purchase",
        "orderId": "ORD-987",
        "purchaseDate": "2024-07-25 18:00:00",
        "purchasedItems": ["Awesome Gadget X", "Cool Thing Y"],
        "orderTotal": 150.00
    }]
    assert transformed == expected

def test_missing_fields():
    """Test when some fields are missing."""
    incomplete_data = [{
        "event_type": "product_view",
        "event_details": {
            "view_timestamp": "2024-07-26T14:30:00Z"
        }
    }]
    
    transformed = transform_data(incomplete_data)
    assert transformed == [{
        "userId": None,  # Missing user_info
        "userEmail": None,  # Missing user_email
        "activityType": "view",
        "productName": None,  # Missing product_name
        "eventTime": "2024-07-26 14:30:00",
        "userLocation": None  # Missing location
    }]