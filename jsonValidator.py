import json
from typing import Any, Dict, List, Union


class JSONValidatorService:
    @staticmethod
    def validate_json(
        data: Union[Dict, List, Any], ignore_fields: List[str] = None
    ) -> List[str]:
        """
        Validate a JSON object for null values recursively, with optional fields to ignore.

        Args:
            data (Union[Dict, List, Any]): The JSON object to validate.
            ignore_fields (List[str], optional): A list of paths to ignore for null checks.

        Returns:
            List[str]: A list of paths where null values are found.
        """
        null_paths = []
        ignore_fields = set(ignore_fields or [])

        def _validate(obj: Union[Dict, List, Any], path: str):
            if path in ignore_fields:
                return

            if obj is None:
                null_paths.append(path if path else "root")
            elif isinstance(obj, dict):
                for key, value in obj.items():
                    new_path = f"{path}.{key}" if path else key
                    _validate(value, new_path)
            elif isinstance(obj, list):
                for index, item in enumerate(obj):
                    new_path = f"{path}[{index}]"
                    _validate(item, new_path)

        _validate(data, "")
        return null_paths

    @staticmethod
    def is_valid_json(json_string: str) -> bool:
        """
        Check if a string is a valid JSON.

        Args:
            json_string (str): The JSON string to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            json.loads(json_string)
            return True
        except json.JSONDecodeError:
            return False


# Main()
if __name__ == "__main__":
    json_input = input("Enter JSON string without qoutes in single line: ")
    ignore_fields_input = input("Enter fields to ignore (comma-separated): ")

    ignore_fields = [
        field.strip() for field in ignore_fields_input.split(",") if field.strip()
    ]

    if JSONValidatorService.is_valid_json(json_input):
        data = json.loads(json_input)
        null_values = JSONValidatorService.validate_json(
            data, ignore_fields=ignore_fields
        )
        if null_values:
            print({"status": "error", "invalid_fields": null_values})
        else:
            print({"status": "success"})
    else:
        print({"status": "error, invalid input"})
