import boto3
from aws_org_client.modules.logger import Logger


logger = Logger(__name__)


class SSOAdmin:
    def __init__(self, instance_arn):
        logger.info("Init sso-admin client...")
        self.sso_admin_client = boto3.client("sso-admin")
        self.instance_arn = instance_arn

    def list_permission_sets(self):
        logger.info("Listing permission sets...")
        permission_sets = []
        next_token = None

        # [TODO: use paginator]
        while True:
            if next_token:
                response = self.sso_admin_client.list_permission_sets(
                    InstanceArn=self.instance_arn, NextToken=next_token
                )
            else:
                response = self.sso_admin_client.list_permission_sets(
                    InstanceArn=self.instance_arn
                )

            permission_sets.extend(response.get("PermissionSets", []))
            next_token = response.get("NextToken")

            if not next_token:
                break

        return permission_sets

    def list_account_permission_sets(self, account_id):
        logger.info(f"Listing permission sets provisioned to {account_id}...")
        response = self.sso_admin_client.list_permission_sets_provisioned_to_account(
            InstanceArn=self.instance_arn, AccountId=account_id
        )

        return response.get("PermissionSets", [])

    def list_account_assignments(self, account_id, permission_set_arn):
        logger.info(f"Listing {account_id} assignee...")
        response = self.sso_admin_client.list_account_assignments(
            InstanceArn=self.instance_arn,
            AccountId=account_id,
            PermissionSetArn=permission_set_arn,
        )

        return response.get("AccountAssignments", [])

    def describe_permission_set(self, permission_set_arn):
        logger.info(f"Describing permission set {permission_set_arn}...")
        response = self.sso_admin_client.describe_permission_set(
            InstanceArn=self.instance_arn, PermissionSetArn=permission_set_arn
        )

        return response.get("PermissionSet")

    def list_accounts_for_provisioned_permission_set(self, permission_set_arn):
        response = self.sso_admin_client.list_accounts_for_provisioned_permission_set(
            InstanceArn=self.instance_arn, PermissionSetArn=permission_set_arn
        )

        return response.get("AccountIds")

    def list_managed_policies_in_permission_set(self, permission_set_arn):
        response = self.sso_admin_client.list_managed_policies_in_permission_set(
            InstanceArn=self.instance_arn, PermissionSetArn=permission_set_arn
        )

        return response.get("AttachedManagedPolicies", [])

    def get_inline_policy_for_permission_set(self, permission_set_arn):
        response = self.sso_admin_client.get_inline_policy_for_permission_set(
            InstanceArn=self.instance_arn, PermissionSetArn=permission_set_arn
        )

        return response

    def list_customer_managed_policy_references_in_permission_set(
        self, permission_set_arn
    ):
        response = self.sso_admin_client.list_customer_managed_policy_references_in_permission_set(
            InstanceArn=self.instance_arn, PermissionSetArn=permission_set_arn
        )

        return response.get("CustomerManagedPolicyReferences", [])
