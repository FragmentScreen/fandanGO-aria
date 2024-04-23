from fGOaria import AriaClient
from fGOaria.utils import json
from fGOaria.field import Field
import os


def deposit_field_metadata(pid: int, json_path : str, vid = None) -> bool :

    # initiate the Aria Connector. This is the 'super class', but using this term very loosely 
    # True for login
    aria = AriaClient(True)

    # initiate a DataManager() instance. this controls Proposal buckets, records, fields etc etc.
    # Basically handles all data/methods for creating/updating MetaData in Aria.
    # The 'True' is an argument for the class to 'find' all existing data in the Aria database for that proposalID
    proposal_manager = aria.new_data_manager(pid, 'proposal', True)

    # Assuming that we only have one bucket per ID in current iteration.
    # Pointing to previous line(14) : 
    #   Buckets will be loaded into the DM instance in a dictionary if there. Structure is {bucket_id : <class>}
    if len(proposal_manager.buckets) == 0 :
        # create a bucket - need embargo period. Use this as a determiner? 
        bucket = proposal_manager.create_bucket('2050-01-01')
        
    # I'll create a method to make this a bit neater. but ok for now.
    # Note that the bucket will 
    bucket_id = next(iter(proposal_manager.buckets))

    # Returns <Record> and stores in DataManager.records. 
    # Format is same as buckets : {record_id : <class>}
    record = proposal_manager.create_record(bucket_id, 'TestSchema')


    # Attempt to load Json:
    data = None
    try:
        with open(json_path, "r") as data_dump:
            data = json.load(data_dump)
    except FileNotFoundError:
        print("File not found:", json_path)
        raise

    # Create a field with the record_id (for reference), the Schema type & the json.
    if data is not None : 
        field = proposal_manager.create_field(record.id, 'TestFieldType', data)
        if isinstance(field, Field) :
            return True

    return False

def perform_action(args):
    success = deposit_field_metadata(args['pid'], args['json_path'])
    results = {'success': success}
    return results


