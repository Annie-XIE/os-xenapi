# Copyright (c) 2014 Rackspace Hosting
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import errno
import socket

import mock

from os_xenapi.client import session
from os_xenapi.tests import test


class SessionTestCase(test.NoDBTestCase):
    @mock.patch('eventlet.timeout.Timeout')
    @mock.patch.object(session.XenAPISession, '_create_session')
    @mock.patch.object(session.XenAPISession, '_get_product_version_and_brand')
    @mock.patch.object(session.XenAPISession, '_verify_plugin_version')
    def test_session_login_with_timeout(self, mock_verify, mock_version,
                                        create_session, mock_timeout):
        pass

    @mock.patch('eventlet.timeout.Timeout')
    @mock.patch.object(session.XenAPISession, '_create_session')
    @mock.patch.object(session.XenAPISession, '_get_product_version_and_brand')
    @mock.patch.object(session.XenAPISession, '_verify_plugin_version')
    @mock.patch.object(session.XenAPISession, '_get_host_uuid')
    @mock.patch.object(session.XenAPISession, '_get_host_ref')
    def test_session_raises_exception(self, mock_ref, mock_uuid,
                                      mock_verify, mock_version,
                                      create_session, mock_timeout):
        pass


class ApplySessionHelpersTestCase(test.NoDBTestCase):
    def setUp(self):
        super(ApplySessionHelpersTestCase, self).setUp()
        self.session = mock.Mock()
        session.apply_session_helpers(self.session)

    def test_apply_session_helpers_add_VM(self):
        self.session.VM.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("VM.get_X", "ref")

    def test_apply_session_helpers_add_SR(self):
        self.session.SR.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("SR.get_X", "ref")

    def test_apply_session_helpers_add_VDI(self):
        self.session.VDI.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("VDI.get_X", "ref")

    def test_apply_session_helpers_add_VIF(self):
        self.session.VIF.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("VIF.get_X", "ref")

    def test_apply_session_helpers_add_VBD(self):
        self.session.VBD.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("VBD.get_X", "ref")

    def test_apply_session_helpers_add_PBD(self):
        self.session.PBD.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("PBD.get_X", "ref")

    def test_apply_session_helpers_add_PIF(self):
        self.session.PIF.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("PIF.get_X", "ref")

    def test_apply_session_helpers_add_VLAN(self):
        self.session.VLAN.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("VLAN.get_X", "ref")

    def test_apply_session_helpers_add_host(self):
        self.session.host.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("host.get_X", "ref")

    def test_apply_session_helpers_add_network(self):
        self.session.network.get_X("ref")
        self.session.call_xenapi.assert_called_once_with("network.get_X",
                                                         "ref")


class CallPluginTestCase(test.NoDBTestCase):
    def _get_fake_xapisession(self):
        class FakeXapiSession(session.XenAPISession):
            def __init__(self, **kwargs):
                "Skip the superclass's dirty init"
                self.XenAPI = mock.MagicMock()

        return FakeXapiSession()

    def setUp(self):
        super(CallPluginTestCase, self).setUp()
        self.session = self._get_fake_xapisession()

    def test_serialized_with_retry_socket_error_conn_reset(self):
        pass

    def test_serialized_with_retry_socket_error_reraised(self):
        exc = socket.error()
        exc.errno = errno.ECONNREFUSED
        plugin = 'glance'
        fn = 'download_vhd'
        num_retries = 1
        callback = None
        retry_cb = mock.Mock()
        with mock.patch.object(self.session, 'call_plugin_serialized',
                spec=True) as call_plugin_serialized:
            call_plugin_serialized.side_effect = exc
            self.assertRaises(socket.error,
                    self.session.call_plugin_serialized_with_retry, plugin, fn,
                    num_retries, callback, retry_cb)
            call_plugin_serialized.assert_called_once_with(plugin, fn)
            self.assertEqual(0, retry_cb.call_count)

    def test_serialized_with_retry_socket_reset_reraised(self):
        pass
