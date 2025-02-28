from datetime import datetime

def convert_datetime(timestamp):
    """Converts ISO datetime (YYYY-MM-DDTHH:MM:SSZ) to YYYY-MM-DD HH:MM:SS."""
    try:
        return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError):
        return None  # Return None if conversion fails
