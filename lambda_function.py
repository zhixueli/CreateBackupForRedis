import json
import boto3

client = boto3.client('elasticache')

def lambda_handler(event, context):

    response = client.create_snapshot(
        ReplicationGroupId='cluster-shard',
        SnapshotName='cluster-shard-backup',
    )
