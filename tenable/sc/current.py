'''
current
=======

The following methods allow for interaction with the Tenable.sc
:sc-api:`CurrentOrganization <Current-Organization.html>` API and the
:sc-api:`CurrentUser <>` API.

Methods available on ``sc.current``:

.. rst-class:: hide-signature
.. autoclass:: CurrentSessionAPI

    .. automethod:: associate_cert
    .. automethod:: org
    .. automethod:: user
'''
from .base import SCEndpoint

class CurrentSessionAPI(SCEndpoint):
    def associate_cert(self):
        '''
        Associates the certificate passed to the server with the current user's
        account.  This allows for authentication via certificate in subsequent
        logins.

        Returns:
            :obj:`dict`:
                The updated user record.

        Examples:
            >>> sc.current.associate_cert()
        '''
        return self._api.post('currentUser/associateCert').json()['response']

    def org(self, fields=None):
        '''
        Returns the organization of the current session.

        :sc-api:`current-organization <Current-Organization.html>`

        Args:
            fields (list, optional):
                The list of fields that are desired to be returned.  For details
                on what fields are available, please refer to the details on the
                request within the organization list API doc.
        Returns:
            :obj:`dict`:
                The organization record.

        Examples:
            >>> org = sc.current.org()
        '''
        params = {}
        if fields:
            params['fields'] = ','.join([self._check('field', f, str)
                                         for f in fields])
        return self._api.get('currentOrganization', params=params).json()['response']

    def user(self, fields=None):
        '''
        Returns the user of the current session.

        :sc-api:`current-user </Current-User.html>`

        Args:
            fields (list, optional):
                The list of fields that are desired to be returned.  For details
                on what fields are available, please refer to the details on the
                request within the organization list API doc.
        Returns:
            :obj:`dict`:
                The user record.

        Examples:
            >>> user = sc.current.user()
        '''
        params = {}
        if fields:
            params['fields'] = ','.join([self._check('field', f, str)
                                         for f in fields])
        return self._api.get('currentUser', params=params).json()['response']
