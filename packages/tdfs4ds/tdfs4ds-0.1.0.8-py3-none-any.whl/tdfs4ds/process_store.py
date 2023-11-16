import teradataml as tdml
from tdfs4ds import feature_store
from tdfs4ds.utils import execute_query_wrapper,execute_query


import uuid
import json

process_catalog_name    = 'FS_PROCESS_CATALOG'

def process_store_catalog_creation(if_exists='replace', comment='this table is a process catalog'):
    """
    This function creates a feature store catalog table in Teradata database.
    The catalog table stores information about features such as their names, associated tables, databases, validity periods, etc.

    Parameters:
    - schema: The schema name in which the catalog table will be created.
    - if_exists (optional): Specifies the behavior if the catalog table already exists. The default is 'replace', which means the existing table will be replaced.
    - table_name (optional): The name of the catalog table. The default is 'FS_FEATURE_CATALOG'.

    Returns:
    The name of the created or replaced catalog table.

    """

    # SQL query to create the catalog table
    query = f"""
    CREATE MULTISET TABLE {feature_store.schema}.{process_catalog_name},
            FALLBACK,
            NO BEFORE JOURNAL,
            NO AFTER JOURNAL,
            CHECKSUM = DEFAULT,
            DEFAULT MERGEBLOCKRATIO,
            MAP = TD_MAP1
            (

                PROCESS_ID VARCHAR(36) NOT NULL,
                PROCESS_TYPE VARCHAR(255) CHARACTER SET LATIN NOT CASESPECIFIC NOT NULL,
                VIEW_NAME   VARCHAR(255) CHARACTER SET LATIN NOT CASESPECIFIC,
                ENTITY_ID JSON(32000),
                FEATURE_NAMES VARCHAR(1024) CHARACTER SET LATIN NOT CASESPECIFIC,
                FEATURE_VERSION VARCHAR(255) CHARACTER SET LATIN NOT CASESPECIFIC,
                METADATA JSON(32000),
                ValidStart TIMESTAMP(0) WITH TIME ZONE NOT NULL,
                ValidEnd TIMESTAMP(0) WITH TIME ZONE NOT NULL,
                PERIOD FOR ValidPeriod  (ValidStart, ValidEnd) AS VALIDTIME
            )
            PRIMARY INDEX (PROCESS_ID);
    """

    # SQL query to create a secondary index on the feature name
    query2 = f"CREATE INDEX (PROCESS_TYPE) ON {feature_store.schema}.{process_catalog_name};"

    # SQL query to comment the table
    query3 = f"COMMENT ON TABLE {feature_store.schema}.{process_catalog_name} IS '{comment}'"

    try:
        # Attempt to execute the create table query
        execute_query(query)
        if tdml.display.print_sqlmr_query:
            print(query)
        if feature_store.display_logs: print(f'TABLE {feature_store.schema}.{process_catalog_name} has been created')
        execute_query(query3)
    except Exception as e:
        # If the table already exists and if_exists is set to 'replace', drop the table and recreate it
        if feature_store.display_logs: print(str(e).split('\n')[0])
        if str(e).split('\n')[0].endswith('already exists.') and (if_exists == 'replace'):
            execute_query(f'DROP TABLE  {feature_store.schema}.{process_catalog_name}')
            print(f'TABLE {feature_store.schema}.{process_catalog_name} has been dropped')
            try:
                # Attempt to recreate the table after dropping it
                execute_query(query)
                if feature_store.display_logs: print(f'TABLE {feature_store.schema}.{process_catalog_name} has been re-created')
                if tdml.display.print_sqlmr_query:
                    print(query)
                execute_query(query3)
            except Exception as e:
                print(str(e).split('\n')[0])

    try:
        # Attempt to create the secondary index
        execute_query(query2)
        if tdml.display.print_sqlmr_query:
            print(query)
        if feature_store.display_logs: print(f'SECONDARY INDEX ON TABLE {feature_store.schema}.{process_catalog_name} has been created')
    except Exception as e:
        print(str(e).split('\n')[0])

    return process_catalog_name

@execute_query_wrapper
def register_process_view( view_name, entity_id, feature_names, feature_version, metadata = {}):

    if type(view_name) == tdml.dataframe.dataframe.DataFrame:
        try:
            view_name = view_name._table_name
        except:
            print('create your teradata dataframe using tdml.DataFrame(<view name>). Crystallize your view if needed')
            return []

    # generate a process id
    process_id = str(uuid.uuid4())

    feature_names = ','.join(feature_names)



    if feature_store.date_in_the_past == None:

        # check if the view already exists:
        query_ = f"CURRENT VALIDTIME SEL * FROM {feature_store.schema}.{process_catalog_name} WHERE view_name = '{view_name}'"
        print(query_)
        df = tdml.DataFrame.from_query(query_)

        if df.shape[0] == 0:
            # CURRENT VALIDTIME
            query_insert = f"""
                CURRENT VALIDTIME INSERT INTO {feature_store.schema}.{process_catalog_name} (PROCESS_ID, PROCESS_TYPE, VIEW_NAME, ENTITY_ID, FEATURE_NAMES, FEATURE_VERSION, METADATA)
                    VALUES ('{process_id}',
                    'denormalized view',
                    '{view_name}',
                    '{json.dumps(entity_id).replace("'", '"')}',
                    '{feature_names}',
                    '{feature_version}',
                    '{json.dumps(metadata).replace("'", '"')}'
                    )
                """
        else:
            query_insert = f"""
                            CURRENT VALIDTIME UPDATE {feature_store.schema}.{process_catalog_name} 
                            SET 
                               PROCESS_TYPE = 'denormalized view'
                            ,   ENTITY_ID = '{json.dumps(entity_id).replace("'", '"')}'
                            ,   FEATURE_NAMES = '{feature_names}'
                            ,   FEATURE_VERSION = '{feature_version}'
                            ,   METADATA = '{json.dumps(metadata).replace("'", '"')}'
                            WHERE VIEW_NAME = '{view_name}'
                            """
    else:

        # check if the view already exists:
        df = tdml.DataFrame.from_query(f"VALIDTIME AS OF TIMESTAMP '{date_in_the_past_}' SEL * FROM {feature_store.schema}.{process_catalog_name} WHERE view_name = '{view_name}'")

        if feature_store.end_period == 'UNTIL_CHANGED':
            end_period_ = '9999-01-01 00:00:00'
        else:
            end_period_ = feature_store.end_period

        if df.shape[0] == 0:
            query_insert = f"""
            INSERT INTO {feature_store.schema}.{process_catalog_name} (PROCESS_ID, PROCESS_TYPE, VIEW_NAME,  ENTITY_ID, FEATURE_NAMES, FEATURE_VERSION, METADATA, ValidStart, ValidEnd)
                VALUES ('{process_id}',
                'denormalized view',
                '{view_name}',
                '{json.dumps(entity_id).replace("'", '"')}'
                ,'{feature_names}',
                '{feature_version}',
                '{json.dumps(metadata).replace("'", '"')}',
                TIMESTAMP '{feature_store.date_in_the_past}',
                TIMESTAMP '{end_period_}'
                )
            """
        else:
            query_insert = f"""VALIDTIME AS OF TIMESTAMP '{date_in_the_past_}'
                            UPDATE {feature_store.schema}.{process_catalog_name} 
                            SET 
                                PROCESS_TYPE = 'denormalized view'
                            ,   ENTITY_ID = '{json.dumps(entity_id).replace("'", '"')}'
                            ,   FEATURE_NAMES = '{feature_names}'
                            ,   FEATURE_VERSION = '{feature_version}'
                            ,   METADATA = '{json.dumps(metadata).replace("'", '"')}'
                            WHERE VIEW_NAME = '{view_name}'
                            """

    print(f'register process with id : {process_id}')

    return query_insert

@execute_query_wrapper
def register_process_tdstone( model,  metadata = {}):

    # generate a process id
    process_id = str(uuid.uuid4())

    # get the parameters

    if feature_store.date_in_the_past == None:
        # CURRENT VALIDTIME
        query_insert = f"""
            CURRENT VALIDTIME INSERT INTO {feature_store.schema}.{process_catalog_name} (PROCESS_ID, PROCESS_TYPE, ENTITY_ID, FEATURE_VERSION, METADATA)
                VALUES ('{process_id}',
                'tdstone2 view',
                '{model.mapper_scoring.id_row}',
                '{model.id}',
                '{json.dumps(metadata).replace("'", '"')}'
                )
            """
    else:
        if feature_store.end_period == 'UNTIL_CHANGED':
            end_period_ = '9999-01-01 00:00:00'
        else:
            end_period_ = feature_store.end_period
        query_insert = f"""
        INSERT INTO {feature_store.schema}.{process_catalog_name} (PROCESS_ID, PROCESS_TYPE, ENTITY_ID, FEATURE_VERSION, METADATA, ValidStart, ValidEnd)
            VALUES ('{process_id}',
            'tdstone2 view',
            '{model.mapper_scoring.id_row}',
            '{model.id}',
            '{json.dumps(metadata).replace("'", '"')}',
            TIMESTAMP '{feature_store.date_in_the_past}',
            TIMESTAMP '{end_period_}')
        """

    print(f'register process with id : {process_id}')

    return query_insert

def list_processes():

    query = f"""
    CURRENT VALIDTIME
    SELECT 
        PROCESS_ID ,
        PROCESS_TYPE ,
        VIEW_NAME ,
        ENTITY_ID ,
        FEATURE_NAMES ,
        FEATURE_VERSION ,
        METADATA
    FROM {feature_store.schema}.{process_catalog_name}
    """
    if tdml.display.print_sqlmr_query: print(query)

    return tdml.DataFrame.from_query(query)

def run(process_id, as_date_of = None):

    query = f"""
    CURRENT VALIDTIME
    SEL * FROM {feature_store.schema}.{process_catalog_name}
    WHERE PROCESS_ID = '{process_id}'
    """

    df = tdml.DataFrame.from_query(query).to_pandas()

    if df.shape[0] != 1:
        print('error - there is ', df.shape[0], f' records. Check table {feature_store.schema}.{process_catalog_name}')
        return

    process_type = df['PROCESS_TYPE'].values[0]

    if process_type == 'denormalized view':
        # it is a basic view
        view_name       = df['VIEW_NAME'].values[0]
        entity_id       = eval(df['ENTITY_ID'].values[0])
        feature_names   = df['FEATURE_NAMES'].values[0].split(',')
        feature_version = df['FEATURE_VERSION'].values[0]

        df_data   = tdml.DataFrame(tdml.in_schema(view_name.split('.')[0],view_name.split('.')[1]))

        feature_store.upload_features(
            df_data,
            entity_id,
            feature_names,
            feature_version)
    elif process_type == 'tdstone2 view':
        # it is a tdstone2 view
        print('not implemented yet')
    return

@execute_query_wrapper
def remove_process(process_id):

    query = f"DELETE FROM {feature_store.schema}.{process_catalog_name} WHERE process_id = '{process_id}'"

    return query