# -*- coding: utf-8 -*-
"""Test suite for the community-developed Python SDK for the Webex Teams APIs.

Copyright (c) 2016-2020 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import webexsdk


class Testwebexsdk:
    """Test the package-level code."""

    def test_package_contents(self):
        """Ensure the package contains the correct top-level objects."""
        # Webex Teams API Wrapper
        assert hasattr(webexsdk, "WebexTeamsAPI")

        # Exceptions
        assert hasattr(webexsdk, "ApiError")
        assert hasattr(webexsdk, "AccessTokenError")
        assert hasattr(webexsdk, "RateLimitError")
        assert hasattr(webexsdk, "RateLimitWarning")
        assert hasattr(webexsdk, "webexsdkException")

        # Data Models
        assert hasattr(webexsdk, "dict_data_factory")
        assert hasattr(webexsdk, "AccessToken")
        assert hasattr(webexsdk, "AttachmentAction")
        assert hasattr(webexsdk, "Event")
        assert hasattr(webexsdk, "License")
        assert hasattr(webexsdk, "Membership")
        assert hasattr(webexsdk, "Message")
        assert hasattr(webexsdk, "Organization")
        assert hasattr(webexsdk, "Person")
        assert hasattr(webexsdk, "Role")
        assert hasattr(webexsdk, "Room")
        assert hasattr(webexsdk, "Team")
        assert hasattr(webexsdk, "TeamMembership")
        assert hasattr(webexsdk, "Webhook")
        assert hasattr(webexsdk, "WebhookEvent")
        assert hasattr(webexsdk, "Recording")
        assert hasattr(webexsdk, "immutable_data_factory")
        assert hasattr(webexsdk, "SimpleDataModel")
        assert hasattr(webexsdk, "simple_data_factory")
