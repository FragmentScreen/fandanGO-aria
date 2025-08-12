from dotenv import load_dotenv
from fGOaria.classes.aria_client import AriaClient
from fGOaria.utils.queries import PULL_VISITS, TECHNICAL_REVIEW_FIELDS, SAVE_TECH_EVAL

load_dotenv()

class ReviewClient(AriaClient):
    def __init__(self, token):
        super().__init__(token)

    def pull_visit(self, vid: int) :
        vars = {
            "filters": {
                "id" : int(vid)
            }
        }
        response = self.gql_query(PULL_VISITS.query, vars)
        return response['data'][PULL_VISITS.return_key]


    def retrieve_fields(self, acid: int):
        params = {
            'access_id': acid
        }
        try:
            response = self.gql_query(TECHNICAL_REVIEW_FIELDS.query, params)
            return response['data'][TECHNICAL_REVIEW_FIELDS.return_key]
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def save_technical_evaluation(self, vid, tech_eval_positive, review_data):
        data_input = [
                {
                    'ref': str(key),
                    'value': value
                }
                for key, value in review_data.items()
            ]

        variables = {
            'input': {
                'vid': int(vid),
                'tech_eval_positive': tech_eval_positive,
                'data': data_input
            }
        }
        return self.gql_query(SAVE_TECH_EVAL, variables)



