from .config import *

def get_formatted_datetime(input_datetime=None, format_str='%Y-%m-%d %H:%M:%S'):
    if input_datetime is None:
        input_datetime = datetime.now()

    formatted_datetime = input_datetime.strftime(format_str)
    return formatted_datetime

def print_with_spaces(str) :
    click.echo('')
    click.echo(str)
    click.echo('')

def space() : click.echo('')

def check_headers(json):
    required_headers = ['access_token', 'expires_in', 'refresh_expires_in', 'refresh_token', 'token_type', 'not-before-policy', 'session_state', 'scope', 'TIMESTAMP']
    for header in required_headers:
        if header not in json:
            return False
    return True

def pretty_print(json_data) : 
    print(json.dumps(json_data, indent=4))


def set_headers(token) :
    return {'Authorization': f'Bearer {token}'}

def command_with_options(prompt_message, options, json_param=False, json_fields=None):

    if json_param and json_fields:
        options_display = []
        for option in options:
            display_info = " - ".join([f"{field[1:]}: {option[field]}" for field in json_fields])
            options_display.append(display_info)
        options_values = options
    else:
        options_display = options
        options_values = options


    answer = questionary.select(
        prompt_message,
        choices=options_display,
    ).ask()

    selected_option = answer

    for option in options_values:
        if json_param and json_fields:
            display_info = " - ".join([f"{field[1:]}: {option[field]}" for field in json_fields])
            if display_info == selected_option:
                return option
        else:
            if option == selected_option:
                return option
# def command_with_options(prompt_message, options, json_param=False, json_fields=None):

#     if json_param and json_fields:
#         options_display = []
#         for option in options:
#             display_info = " - ".join([f"{field}: {option[field]}" for field in json_fields])
#             options_display.append(display_info)
#         options_values = options
#     else:
#         options_display = options
#         options_values = options

#     questions = [
#         inquirer.List('option',
#                       message=prompt_message,
#                       choices=options_display,
#                       carousel=True,
#                       ),
#     ]
#     answer = inquirer.prompt(questions)
#     selected_option = answer['option']

#     for option in options_values:
#         if json_param and json_fields:
#             display_info = " - ".join([f"{field}: {option[field]}" for field in json_fields])
#             if display_info == selected_option:
#                 return option
#         else:
#             if option == selected_option:
#                 return option

def format_datetime_to_json_serializable(date):
    """
    Converts a datetime object to a string in the format 'dd-mm-yyyy 00:00:00'.
    
    Args:
        dt (datetime): The datetime object to be formatted.
        
    Returns:
        str: The formatted datetime string.
    """
    return date.strftime('%d-%m-%Y 00:00:00')

def get_entity() :
    aria_id = click.prompt('Set ARIA ID', type=int)
    aria_entity_type = command_with_options('aria entity', ['proposal', 'visit'])
    return {
        'id': aria_id,
        'type': aria_entity_type
    }