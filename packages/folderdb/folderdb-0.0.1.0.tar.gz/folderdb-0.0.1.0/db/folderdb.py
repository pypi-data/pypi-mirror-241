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
            row_data = ",".join(str(element) for element in row_data)  # Convert list elements to strings

        # Encode and store row data
        encoded_data = base64.b64encode(row_data.encode() if isinstance(row_data, str) else row_data)
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
    
    def delete_table(self, table_name):
        table_path = os.path.join(self.base_path, table_name)
        if os.path.exists(table_path):
            shutil.rmtree(table_path)  # Remove the table directory

            # Update structure.json after deleting the table
            with open(os.path.join(self.base_path, "structure.json"), "r") as structure_file:
                structure = json.load(structure_file)

            if table_name in structure:
                del structure[table_name]  # Remove the table entry from the structure

            with open(os.path.join(self.base_path, "structure.json"), "w") as structure_file:
                json.dump(structure, structure_file)
        else:
            raise FileNotFoundError(f"Table '{table_name}' does not exist.")
        
    def delete_row(self, table_name, row_number):
        row_folder = os.path.join(self.base_path, table_name, f"{row_number}.row")
        if os.path.exists(row_folder):
            shutil.rmtree(row_folder)  # Remove the row directory
        else:
            raise FileNotFoundError(f"Row '{row_number}' in table '{table_name}' does not exist.")

    def delete_database(self):
        if os.path.exists(self.base_path):
            shutil.rmtree(self.base_path)  # Remove the entire database directory
        else:
            raise FileNotFoundError("Database does not exist.")
