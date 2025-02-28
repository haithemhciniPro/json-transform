from src.file_handler import read_json, write_json
from src.transform import transform_data

# File paths
INPUT_FILE = "data/product_data.json"
OUTPUT_FILE = "data/client_output.json"

def main():
    """Main function to execute JSON transformation."""
    try:
        # Read input JSON
        product_data = read_json(INPUT_FILE)

        if not product_data:
            print("❌ No valid data to process. Exiting.")
            return

        # Transform data
        transformed_data = transform_data(product_data)

        # Write output JSON
        write_json(OUTPUT_FILE, transformed_data)

        print(f"✅ Transformation complete. Output saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    main()
