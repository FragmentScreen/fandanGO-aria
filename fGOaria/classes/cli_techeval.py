from .technical_review import TechEvaluation
from ..utils.utility_functions import command_with_options, pretty_print, print_with_spaces, print_created_message
import click

class TechEvalCLI:
    def __init__(self, token):
        """
        Initiate TechEvalCLI instance.

        :param token: Token for authentication.
        """
        self.tech_eval = TechEvaluation(token)

    def menu(self) -> None:
        """
        Display the main menu and handle user input for menu navigation.
        """
        action = command_with_options('What would you like to do?', ['Retrieve Visit Fields', 'Submit Visit Evaluation', 'Exit'])
        if action == 'Exit':
            print('Closing Menu...')
            return
        if action == 'Retrieve Visit Fields':
            self.retrieve_fields_cli()
        elif action == 'Submit Visit Evaluation':
            self.submit_evaluation_cli()

    # RETRIEVE FIELDS

    def retrieve_fields_cli(self) -> None:
        """
        CLI to retrieve fields based on ACID.
        """
        vid = click.prompt('Enter Visit ID')
        fields = self.tech_eval.retrieve_tech_fields(vid)
        if fields:
            pretty_print(fields)
        else:
            print(f"No fields found for Visit: {vid}")
        self.menu()

    # SUBMIT EVALUATION

    def submit_evaluation_cli(self) -> None:
        """
        CLI to submit a technical evaluation.
        """
        vid = click.prompt('Enter VID')
        tech_eval = click.confirm('Do you accept this evaluation?')
        if tech_eval:
            tech_eval = 1
        else: tech_eval = 0
        
        fields = self.tech_eval.retrieve_tech_fields(vid)
        if not fields:
            print(f"No fields found for VID: {vid}, returning to menu.")
            return self.menu()
        
        print_with_spaces("Retrieved Fields:")
        pretty_print(fields)

        review_data = {}
        for field in fields:
            value = click.prompt(f"Enter value for field '{field['ref']}' (type: {field['type']})", default='')
            review_data[field['fid']] = value

        result = self.tech_eval.submit_evaluation(vid, tech_eval, review_data)
        if result:
            print("Evaluation submitted successfully!")
        else:
            print("Failed to submit evaluation.")
        
        self.menu()
