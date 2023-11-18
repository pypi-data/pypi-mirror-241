import os
import json
import base64
from cryptography.fernet import Fernet

class FileDatabase:
    def __init__(self, base_path):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def create_table(self, table_name, columns):
        table_path = os.path.join(self.base_path, table_name)
        os.makedirs(table_path, exist_ok=True)

        structure = {table_name: columns}
        with open(os.path.join(self.base_path, "structure.json"), "w") as structure_file:
            json.dump(structure, structure_file)

    def insert_row(self, table_name, row_data):
        table_path = os.path.join(self.base_path, table_name)

        row_number = len(os.listdir(table_path)) + 1
        row_folder = os.path.join(table_path, f"{row_number}.row")
        os.makedirs(row_folder)

        # Ensure row_data is a string, if it's a list, convert it to a string
        if isinstance(row_data, list):
            row_data = ",".join(row_data)  # Convert list to a string using comma as delimiter

        # Encode and store row data
        encoded_data = base64.b64encode(row_data.encode())
        with open(os.path.join(row_folder, "row_content"), "wb") as row_file:
            row_file.write(encoded_data)

    def retrieve_rows(self, table_name):
        table_path = os.path.join(self.base_path, table_name)
        rows = []
        for folder in os.listdir(table_path):
            row_folder = os.path.join(table_path, folder)
            if os.path.isdir(row_folder):
                with open(os.path.join(row_folder, "row_content"), "rb") as row_file:
                    encoded_data = row_file.read()
                    decoded_data = base64.b64decode(encoded_data).decode()
                    rows.append(decoded_data)
        return rows
