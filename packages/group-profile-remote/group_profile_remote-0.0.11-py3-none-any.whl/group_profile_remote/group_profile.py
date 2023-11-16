# TODO: This is an example file which you should delete after impenting
import requests
from url_local.url_circlez import OurUrl
import os
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from url_local.component_name_enum import ComponentName
from url_local.entity_name_enum import EntityName
from url_local.action_name_enum import ActionName
from user_context_remote.user_context import UserContext
from dotenv import load_dotenv
load_dotenv()


GROUP_PROFILE_COMPONENT_ID = 211
GROUP_PROFILE_COMPONENT_NAME = "Group Profile Remote Python"
COMPONENT_CATEGORY = LoggerComponentEnum.ComponentCategory.Code.value
COMPONENT_TYPE = LoggerComponentEnum.ComponentType.Remote.value
DEVELOPER_EMAIL = "yarden.d@circ.zone"

obj = {
    'component_id': GROUP_PROFILE_COMPONENT_ID,
    'component_name': GROUP_PROFILE_COMPONENT_NAME,
    'component_category': COMPONENT_CATEGORY,
    'component_type': COMPONENT_TYPE,
    "developer_email": DEVELOPER_EMAIL
}

BRAND_NAME = os.getenv("BRAND_NAME")
ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME")
GROUP_PROFILE_API_VERSION = 1


class GroupProfile:

    def __init__(self):
        self.url_circlez = OurUrl()
        self.logger = Logger.create_logger(object=obj)
        self.brand_name = BRAND_NAME
        self.env_name = ENVIRONMENT_NAME

    def create_group_profile(self, group_id: str, relationship_type_id: str, jwt_token: str):
        self.logger.start("Start create group-rofile-remote")
        user = UserContext.login_using_jwt(jwt_token)
        profile_id = str(user.get_effective_profile_id())
        try:
            url = self.url_circlez.endpoint_url(
                brand_name=self.brand_name,
                environment_name=self.env_name,
                component_name=ComponentName.GROUP_PROFILE.value,
                entity_name=EntityName.GROUP_PROFILE.value,
                version=GROUP_PROFILE_API_VERSION,
                action_name=ActionName.CREATE_GROUP_PROFILE.value,  # "createGroupProfile",
            )
            self.logger.info(
                "Endpoint group profile - createGroupProfile action: " + url)

            payload = {
                "groupId": f"{group_id}",
                "profileId": f"{profile_id}",
                "relationshipTypeId": f"{relationship_type_id}"
            }

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {jwt_token}",
            }
            response = requests.post(url=url, json=payload, headers=headers)
            # print(response.text)
            self.logger.end(
                f"End create group-profile-remote, response: {str(response)}")
            return response

        except requests.ConnectionError as e:
            self.logger.exception(
                "Network problem (e.g. failed to connect)", object=e)
        except requests.Timeout as e:
            self.logger.exception("Request timed out", e)
        except requests.RequestException as e:
            self.logger.exception(f"General error: {str(e)}", object=e)
        except Exception as e:
            self.logger.exception(
                f"An unexpected error occurred: {str(e)}", object=e)

        self.logger.end("End create group-profile-remote")

    def get_group_profile_by_group_id(self, group_id: str):
        self.logger.start("Start get group-profile-remote")
        try:
            url = self.url_circlez.endpoint_url(
                brand_name=self.brand_name,
                environment_name=self.env_name,
                component_name=ComponentName.GROUP_PROFILE.value,
                entity_name=EntityName.GROUP_PROFILE.value,
                version=GROUP_PROFILE_API_VERSION,
                # "getGroupProfileByGroupIdProfileId",
                action_name=ActionName.GET_GROUP_PROFILE.value,
                query_parameters={
                    'groupId': group_id,
                    'profileId': str(self.logger.userContext.get_effective_profile_id()),
                }
            )
            self.logger.info(
                "Endpoint group profile - getGroupProfileByGroupIdProfileId action: " + url)

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.logger.userContext.get_user_JWT()}',
            }

            response = requests.get(url, headers=headers)
            # print(response.text)
            self.logger.end(
                f"End get group-profile-remote, response: {str(response)}")
            return response

        except requests.ConnectionError as e:
            self.logger.exception(
                "Network problem (e.g. failed to connect)", object=e)
        except requests.Timeout as e:
            self.logger.exception("Request timed out", object=e)
        except requests.RequestException as e:
            self.logger.exception(f"General error: {str(e)}", object=e)
        except Exception as e:
            self.logger.exception(
                f"An unexpected error occurred: {str(e)}", object=e)

        self.logger.end("End get group-profile-remote")

    def delete_group_profile(self, group_id: str, relationship_type_id: str):
        self.logger.start("Start delete group-profile-remote")
        try:
            url = self.url_circlez.endpoint_url(
                brand_name=self.brand_name,
                environment_name=self.env_name,
                component_name=ComponentName.GROUP_PROFILE.value,
                entity_name=EntityName.GROUP_PROFILE.value,
                version=GROUP_PROFILE_API_VERSION,
                action_name=ActionName.DELETE_GROUP_PROFILE.value,  # "deleteGroupProfile",
            )

            self.logger.info(
                "Endpoint group profile - deleteGroupProfile action: " + url)

            payload = {
                'groupId': group_id,
                'profileId': str(self.logger.userContext.get_effective_profile_id()),
                'relationshipTypeId': relationship_type_id
            }

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {self.logger.userContext.get_user_JWT()}',
            }

            response = requests.put(url, json=payload, headers=headers)
            # print(response.text)
            self.logger.end(
                f"End delete group-profile-remote, response: {str(response)}")
            return response

        except requests.ConnectionError as e:
            self.logger.exception(
                "Network problem (e.g. failed to connect)", object=e)
        except requests.Timeout as e:
            self.logger.exception("Request timed out", object=e)
        except requests.RequestException as e:
            self.logger.exception(f"General error: {str(e)}", object=e)
        except Exception as e:
            self.logger.exception(
                f"An unexpected error occurred: {str(e)}", object=e)

        self.logger.end("End delete group-profile-remote")
