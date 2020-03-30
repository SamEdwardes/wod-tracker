import boto3
import dash_bootstrap_components as dbc
import pandas as pd


def refresh_aws_table(aws_table, n=5):
    """Refresh table from AWS
    
    Parameters
    ----------
    aws_table : DynamoDB.Table
        boto3 table. For example:
        `import boto3`
        `dynamodb = boto3.resource('dynamodb')`
        `table = dynamodb.Table('name')`
    n : int, optional
        Number of rows to display, by default 5
    
    Returns
    -------
    (pandas.DataFrame, dash_bootstrap_components.Table.from_dataframe)
        A tubple containing refreshed pandas DataFrame and the a version of
        the dataframe for displaying in Dash.
    """    
    df = pd.DataFrame(data=aws_table.scan()['Items'])
    df = df.sort_values(by='date', ascending=False)
    df_ordered = df[['user', 'date', 'name', 'sets', 'reps', 'weight']]
    dbc_df = dbc.Table.from_dataframe(df_ordered.head(n), 
                                      id="wod-log-df", size="sm", striped=True,
                                      hover=True),
    return df, dbc_df
