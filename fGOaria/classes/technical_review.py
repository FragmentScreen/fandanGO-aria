from .client_review import ReviewClient
from .visit import Visit
from ..utils.constants import *
import requests

class TechEvaluation:
    def __init__(self, token):
        self.client = ReviewClient(token)
        self.fields = None  

    
    def retrieve_tech_fields(self, vid: int):
        """
        Retrieves review fields based on the given acid.
        Processes and returns the relevant fields.
        """
        try:
            visit = self.client.pull_visit(vid)
            if not visit :
                print(f'Error: No visit with ID {vid} found')
                return None
            
            visit = Visit(visit[0])
            fields = self.client.retrieve_fields(visit._acid)

            if not fields:
                print(f"No fields found for Visit ID: {vid}")
                return None

            self.fields = self._process_fields(fields)
            return self.fields
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving fields: {e}")
            return None


    def _process_fields(self, items):
        """
        Processes the fields from the retrieved items.
        """
        return [
            {
                'fid': item['fid'],
                'type': item['type'],
                'help': item['options'].get('help', ''),
                'max': item['options'].get('max', ''),
                'opts': item['options'].get('opts', ''),
                'ref': item['ref']
            }
            for item in items
        ]
    
    def validate_fields(self, review_data):
        """
        Validates the review data based on the field definitions.
        """
        errors = []
        for field in self.fields:
            fid = field['fid']
            field_type = field['type']
            max_value = field['max']
            user_input = review_data.get(fid, None)

            if user_input is None:
                errors.append(f"Field {fid} is missing input.")
                continue

            if field_type == TEXT_SHORT:
                if not isinstance(user_input, str):
                    errors.append(f"Field {fid} should be a short text.")
            
            elif field_type == TEXT_NUMBER:
                try:
                    user_input = float(user_input)
                    if max_value and user_input > float(max_value):
                        errors.append(f"Field {fid} exceeds the maximum value of {max_value}.")
                except ValueError:
                    errors.append(f"Field {fid} should be a numeric value.")
            

        is_valid = len(errors) == 0
        return is_valid, errors

    def submit_evaluation(self, vid, tech_eval_positive, review_data):
        """
        Submits the evaluation for the given visit.
        """
        is_valid, errors = self.validate_fields(review_data)
        if not is_valid:
            print("Validation failed:", errors)
            return None
        
        try:
            return self.client.save_technical_evaluation(vid, tech_eval_positive, review_data)
        except requests.exceptions.RequestException as e:
            print(f"Error submitting evaluation: {e}")
            return None
        
