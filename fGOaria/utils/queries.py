from collections import namedtuple

GQLQuery = namedtuple('GQLQuery', ['query', 'return_key'])

CREATE_DATA_BUCKET = GQLQuery(
    query = """
        mutation($input: CreateBucketInput!) {
            createDataBucket(input: $input) {
                id,
                embargoed_until,
                owner,
                created,
                updated,
                aria_entity_type,
                aria_id
            }
        }""",
    return_key = "createDataBucket"
)

CREATE_DATA_RECORD = GQLQuery(
    query= """
        mutation($input: CreateRecordInput!) {
            createDataRecord(input: $input) {
                id,
                bucket,
                created,
                updated,
                schema
            }
        }""",
    return_key = "createDataRecord"
)

CREATE_DATA_FIELD = GQLQuery(
    query = """
        mutation($input: CreateFieldInput!) {
            createDataField(input: $input) {
                id,
                record,
                options,
                content,
                type
            }
        }""",
    return_key = "createDataField"
)


BUCKET_ITEMS = GQLQuery(
    query = """
        query($filters: BucketFilters) {
            bucketItems(filters: $filters) {
                id,
                embargoed_until,
                aria_id,
                aria_entity_type,
                owner,
                created,
                updated
            }
        }""",
    return_key = "bucketItems"
)

RECORD_ITEMS = GQLQuery(
    query = """
        query($filters: RecordFilters) {
            recordItems(filters: $filters) {
                id,
                bucket,
                schema,
                owner,
                created,
                updated
            }
        }""",
    return_key = "recordItems"
)

FIELD_ITEMS = GQLQuery(
    query = """
        query($filters: FieldFilters) {
            fieldItems(filters: $filters) {
                id,
                record,
                content,
                options,
                order,
                type
            }
        }""",
    return_key = "fieldItems"
)

PULL_VISITS = GQLQuery(
    query="""
        query($filters: VisitFilters) {
            visitItems(filters: $filters) {
                id,
                cid,
                order, 
                status,     
                plid, 
                proposal_id,
                access_id
            }
        }""",
    return_key = "visitItems"
)


TECHNICAL_REVIEW_FIELDS = GQLQuery(
    query= """
        query($filters: Access_technical_review_fieldsFilters) {
            access_technical_review_fieldsItems(filters: $filters) {
                fid,
                ref,
                title,
                type,
                alttitle,
                required,
                options
            }
        }""",
    return_key='access_technical_review_fieldsItems'
)

SAVE_TECH_EVAL =  """
    mutation($input: SaveTechnicalEvaluationInputType!) {
      saveTechnicalEvaluation(input: $input) {
        vid
      }
    }
    """

# TODO: separate queries and mutations
# TODO: use graphQL queries/mutations
# GET_STORAGE_PROVIDERS - GQLQuery(
#     query = """""",
#     return_key = "storageProviderItems"
# )
#
# FETCH_STORAGE_TOKENS = GQLMutation(
#     mutation = """""",
#     return_key = "storageTokenItems"
# )
#
# CHECK_STORAGE_VALIDITY = GQLMutation(
#     mutation = """""",
#     return_key = "storageTokenItems"
# )