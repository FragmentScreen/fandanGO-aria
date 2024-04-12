from .imports_config import *

#  PRINTING

def space() : click.echo('')

def print_with_spaces(str) :
    """Print a str with a space above and below in the terminal"""
    click.echo('')
    click.echo(str)
    click.echo('')

def pretty_print(obj) :
    """Print an object with indentation to represent nesting""" 
    print(json.dumps(obj, indent=4))

def print_created_message(obj) :
    """Specific to new Class Creation. Will take the class name and new ID to print a message."""
    print(f'New {obj.__class__.__name__} created with ID: {obj.id}')

# FORMATTING

def get_formatted_datetime(input_datetime=None, format_str='%Y-%m-%d %H:%M:%S'):
    """Forms datetime of either a datetime given or the current time. 
        The format is able to be manipulated by setting the format_str variable
    """
    if input_datetime is None:
        input_datetime = datetime.now()

    formatted_datetime = input_datetime.strftime(format_str)
    return formatted_datetime

# OAUTH


def check_headers(json):
    """Checks all the properties of an ARIA token exist before attempting to store"""
    required_headers = ['access_token', 'expires_in', 'refresh_expires_in', 'refresh_token', 'token_type', 'not_before_policy', 'session_state', 'scope', 'timestamp']
    for header in required_headers:
        if header not in json:
            return False
    return True

def set_headers(token) :
    """Return a variable that holds a token to be used in a request"""
    return  {'Authorization': f'Bearer {token}'}



# CONFIG

def get_config(config_file='config.yml'):
    """Get the path to the config.yml file"""
    fandango_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    config_path = os.path.join(fandango_dir, "config", config_file)
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config


# CLI

def command_with_options(prompt_message, options, json_param=False, json_fields=None):
    """Create a 'questionary' selection tool in the commands line
        Can accept strings or lists as an argument.
    """

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
            
def get_dicts_from_objects(objects) -> list :
    """Returns the properties of each object in a list."""
    return [obj.__dict__ for obj in objects]

def format_datetime_to_json_serializable(date):
    """
    Converts a datetime object to a string in the format 'dd-mm-yyyy 00:00:00'.
    
    Args:
        dt (datetime): The datetime object to be formatted.
        
    Returns:
        str: The formatted datetime string.
    """
    return date.strftime('%d-%m-%Y 00:00:00')

def get_entity() -> dict :
    aria_id = click.prompt('Set ARIA ID', type=int)
    aria_entity_type = command_with_options('aria entity', ['proposal', 'visit'])
    return {
        'id': aria_id,
        'type': aria_entity_type
    }

def options_manager(options = {}) -> dict :
        """CLI Tool for creating Key-Value pairs."""
        if click.confirm('Would you like to add an option key-value?'):
            key = click.prompt('Enter Key Name')
            value = click.prompt(f'Enter Value for {key}')
            options[key] = value
            return options_manager(options)
        else:
            return options