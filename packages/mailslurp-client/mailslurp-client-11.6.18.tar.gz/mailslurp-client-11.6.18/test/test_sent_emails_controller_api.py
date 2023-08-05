# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import mailslurp_client
from mailslurp_client.api.sent_emails_controller_api import SentEmailsControllerApi  # noqa: E501
from mailslurp_client.rest import ApiException


class TestSentEmailsControllerApi(unittest.TestCase):
    """SentEmailsControllerApi unit test stubs"""

    def setUp(self):
        self.api = mailslurp_client.api.sent_emails_controller_api.SentEmailsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sent_email(self):
        """Test case for get_sent_email

        Get sent email receipt  # noqa: E501
        """
        pass

    def test_get_sent_emails(self):
        """Test case for get_sent_emails

        Get all sent emails in paginated form  # noqa: E501
        """
        pass

    def test_get_sent_organization_emails(self):
        """Test case for get_sent_organization_emails

        Get all sent organization emails in paginated form  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
