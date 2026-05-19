import json
from types import MappingProxyType

from fGOaria.classes.client_provider import ProviderClient
from fGOaria.utils import utility_functions as utils
from fGOaria.utils.imports_config import click
from fGOaria.classes.aria_manager import ARIA

ACTION_UPLOAD = ProviderClient.upload.__name__
ACTION_DOWNLOAD = ProviderClient.download.__name__
ACTION_LOCATE = ProviderClient.locate.__name__
ACTION_DELETE = ProviderClient.delete.__name__
ACTION_DEPOSIT_METADATA = "deposit metadata to ARIA"

PROVIDER_ACTIONS = MappingProxyType({
    0: ACTION_UPLOAD,
    1: ACTION_DOWNLOAD,
    2: ACTION_LOCATE,
    3: ACTION_DELETE,
    4: ACTION_DEPOSIT_METADATA
})

# @click.command()
# def view_storage_options():
#     """Display the available storage options"""
#     cli = ARIA()
#     entity_details = utils.get_entity()
#     manager = cli.new_storage_manager(entity_details.get('id'), entity_details.get('type'))
#     print(manager.providers)

@click.command()
def provision_storage_option():
    """Select a storage provider, provision storage and perform actions within the provider's data space"""
    cli = ARIA()
    entity_details = utils.get_entity()
    entity_type = entity_details.get('type')
    entity_id = entity_details.get('id')
    manager = cli.new_storage_manager(str(entity_id), entity_type)

    utils.print_with_spaces(f"Finding available storage options in ARIA for {entity_type} ID {entity_id}...")
    selected = utils.command_with_options("Select a storage option", manager.providers)
    manager.select(selected)

    utils.print_with_spaces(f"Provisioning storage from {selected}...")
    manager.provision()
    print("Successfully provisioned")

    file_id = None
    while True:
        if file_id is not None:
            utils.print_with_spaces(f"Current File ID: {file_id}\n\n")

        action = utils.command_with_options(f"Which action do you want to perform?",
                                            list(PROVIDER_ACTIONS.values()))

        print()
        if (action == ACTION_UPLOAD):
            file_location = click.prompt('File name and location', type=str)
            file_id = manager.client.upload(file_location)
            utils.print_with_spaces(f"Successfully uploaded {file_location} to {selected}")

        if (action == ACTION_DEPOSIT_METADATA):
            if (file_id is None):
                print("No file uploaded yet. Please upload a file before depositing metadata.")
                continue

            manager = cli.new_cli_data_manager(entity_id, entity_type, True)

            # package metadata from deposition into record/fields. TODO: turn this into helper func on StorageManager?

            bucket = manager.create_bucket_cli(menu_return=False)

            record = manager.create_record(bucket.id, 'ARIA_StorageUpload')
            utils.print_created_message(record)

            field = manager.create_field(bucket.id, 'JSON_ARIA_StorageUpload', json.dumps({
                "provider_id": selected,
                "file_id": file_id
            }))

            # upload to ARIA
            manager.push(record)
            manager.push(field)
