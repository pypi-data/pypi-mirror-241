import boto3
import botocore
from enum import Enum
from dotenv import load_dotenv
import requests
import json
import time
import logging
from botocore.exceptions import ClientError
import os
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum


load_dotenv()
SMS_MESSAGE_AWS_SNS_LOCAL_PYTHON_PACKAGE_COMPONENT_ID = 208
SMS_MESSAGE_AWS_SNS_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME = "sms_message_aws_sns_local_python_package"
DEVELOPER_EMAIL = "emad.a@circ.zone"
logger = logging.getLogger(__name__)


class SnsWrapper:
    def __init__(self, sns_resource):
        self.sns_resource = sns_resource

    def create_topic(self, name):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: The newly created topic.
        """
        try:
            topic = self.sns_resource.create_topic(Name=name)
            logger.info("Created topic %s with ARN %s.", name, topic.arn)
        except ClientError:
            logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return topic

    def publish_text_message(self, phone_number, message):
        try:
            response = self.sns_resource.meta.client.publish(
                PhoneNumber=phone_number, Message=message
            )
            message_id = response["MessageId"]
            logger.info("Published message to %s.", phone_number)
        except ClientError:
            logger.exception("Couldn't publish message to %s.", phone_number)
            raise
        else:
            return message_id

    @staticmethod
    def publish_message(topic, message, attributes):
        """
        Publishes a message, with attributes, to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.

        :param topic: The topic to publish to.
        :param message: The message to publish.
        :param attributes: The key-value attributes to attach to the message. Values
                           must be either `str` or `bytes`.
        :return: The ID of the message.
        """
        try:
            att_dict = {}
            for key, value in attributes.items():
                if isinstance(value, str):
                    att_dict[key] = {
                        "DataType": "String", "StringValue": value}
                elif isinstance(value, bytes):
                    att_dict[key] = {
                        "DataType": "Binary", "BinaryValue": value}
            response = topic.publish(
                Message=message, MessageAttributes=att_dict)
            message_id = response["MessageId"]
            logger.info(
                "Published message with attributes %s to topic %s.",
                attributes,
                topic.arn,
            )
        except ClientError:
            logger.exception(
                "Couldn't publish message to topic %s.", topic.arn)
            raise
        else:
            return message_id


# local test
def usage_demo():
    print("-" * 88)
    print("Welcome to the Amazon Simple Notification Service (Amazon SNS) demo!")
    print("-" * 88)

    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s: %(message)s")

    sns_client = boto3.client("sns")
    sns_resource = boto3.resource("sns")

    topic_name = 'arn:aws:sns:us-east-1:676237613168:SendSMS'
    print(f"Creating topic {topic_name}.")

    phone_number = input(
        "Enter a phone number (in E.164 format) that can receive SMS messages: "
    )
    if phone_number != "":
        print(f"Sending an SMS message directly from SNS to {phone_number}.")
        sns_client.publish(PhoneNumber=phone_number,
                           Message="Hello from the SNS demo!")

    phone_sub = None
    if phone_number != "":
        print(
            f"Subscribing {phone_number} to {topic_name}. Phone numbers do not "
            f"require confirmation."
        )
        topic = sns_resource.Topic(topic_name)
        phone_sub = topic.subscribe(Protocol="sms", Endpoint=phone_number)

    if phone_number != "":
        mobile_key = "mobile"
        friendly = "friendly"
        print(
            f"Adding a filter policy to the {phone_number} subscription to send "
            f"only messages with a '{mobile_key}' attribute of '{friendly}'."
        )
        # Add your filter policy logic here using sns_client
        print(
            f"Publishing a message with a {mobile_key}: {friendly} attribute.")
        sns_client.publish(
            PhoneNumber=phone_number,
            Message="Hello! This message is mobile-friendly.",
            MessageAttributes={mobile_key: {
                "DataType": "String", "StringValue": friendly}},
        )
        not_friendly = "not-friendly"
        print(
            f"Publishing a message with a {mobile_key}: {not_friendly} attribute.")
        sns_client.publish(
            PhoneNumber=phone_number,
            Message="Hey. This message is not mobile-friendly, so you shouldn't get "
                    "it on your phone.",
            MessageAttributes={mobile_key: {
                "DataType": "String", "StringValue": not_friendly}},
        )

    print(f"Getting subscriptions to {topic_name}.")
    topic_subs = sns_resource.Topic(topic_name).subscriptions.all()
    for sub in topic_subs:
        print(f"{sub.arn}")

    # print(f"Deleting subscriptions and {topic_name}.")
    # for sub in topic_subs:
    #     sub.delete()
    # sns_resource.Topic(topic_name).delete()

    print("Thanks for watching!")
    print("-" * 88)

# if __name__ == "__main__":
#     #usage_demo()
#     sms = SnsWrapper(boto3.resource('sns'))
#     sms.publish_text_message('+972545232179',"gfugcuf")
