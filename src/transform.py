from src.utils import convert_datetime
from src.logger import logger

def transform_data(product_data):
    """Transforms product JSON into the client's expected format."""
    transformed_data = []

    for record in product_data:
        try:
            user_info = record.get("user_info", {})
            event_details = record.get("event_details", {})

            transformed_record = {
                "userId": user_info.get("username"),
                "userEmail": user_info.get("user_email"),
                "activityType": "view" if record.get("event_type") == "product_view" else record.get("event_type"),
            }

            if record.get("event_type") == "product_view":
                transformed_record.update({
                    "productName": event_details.get("product_name"),
                    "eventTime": convert_datetime(event_details.get("view_timestamp")),
                    "userLocation": event_details.get("location"),
                })
            
            elif record.get("event_type") == "purchase":
                transformed_record.update({
                    "orderId": event_details.get("order_id"),
                    "purchaseDate": convert_datetime(event_details.get("purchase_date")),
                    "purchasedItems": event_details.get("items", []),
                    "orderTotal": event_details.get("total_amount", 0.0),
                })

            transformed_data.append(transformed_record)
        except Exception as e:
            logger.error(f"Error transforming record: {record} | Exception: {e}")

    return transformed_data