import boto3
from aws_org_client.modules.logger import Logger
from aws_org_client.modules.paginator import Paginator


logger = Logger(__name__)


class IdentityStore:
    def __init__(self, identity_store_id):
        """Initialise client for identity store.

        Args:
            identity_store_id (string): The globally unique identifier for the identity store.
        """
        logger.info("Init idc client...")
        self.client = boto3.client("identitystore")
        self.identity_store_id = identity_store_id
        self.paginator = Paginator(self.client)

    def list_users(self):
        """List all users in identity store.

        Returns:
            list: Collection of user objects.
        """
        logger.info("Listing users...")

        result = self.paginator.paginate(
            PaginatorName="list_users",
            ResultKey="Users",
            OperationalParameters={"IdentityStoreId": self.identity_store_id},
        )
        return result

    def describe_user(self, user_id):
        """
        Call the Identity Store to describe the user

        Returns:
            list: Description of the user.
        """
        logger.info(f"Describing user: {user_id}...")
        response = self.client.describe_user(
            IdentityStoreId=self.identity_store_id, UserId=user_id
        )

        return response

    def list_groups(self):
        """
        List all groups in identity store.

        Returns:
            list: Collection of group objects.
        """
        logger.info("Listing groups...")

        result = self.paginator.paginate(
            PaginatorName="list_groups",
            ResultKey="Groups",
            OperationalParameters={"IdentityStoreId": self.identity_store_id},
        )

        return result

    def describe_group(self, group_id):
        """
        Call the Identity Store to describe the group

        Returns:
            list: Collection of group objects.
        """
        logger.info(f"Describing group: {group_id}...")
        response = self.client.describe_group(
            IdentityStoreId=self.identity_store_id, GroupId=group_id
        )

        return response

    def list_group_memberships(self, group_id):
        """
        Call the Identity Store to list the members in the group

        Returns:
            list: Collection of group member objects.
        """
        logger.info(f"Listing group memberships: {group_id}...")

        result = self.paginator.paginate(
            PaginatorName="list_group_memberships",
            ResultKey="GroupMemberships",
            OperationalParameters={
                "IdentityStoreId": self.identity_store_id,
                "GroupId": group_id,
            },
        )

        return result
