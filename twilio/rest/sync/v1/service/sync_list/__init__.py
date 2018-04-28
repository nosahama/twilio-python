# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.sync.v1.service.sync_list.sync_list_item import SyncListItemList
from twilio.rest.sync.v1.service.sync_list.sync_list_permission import SyncListPermissionList


class SyncListList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the SyncListList

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service Instance that hosts this List object.

        :returns: twilio.rest.sync.v1.service.sync_list.SyncListList
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListList
        """
        super(SyncListList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Lists'.format(**self._solution)

    def create(self, unique_name=values.unset, ttl=values.unset):
        """
        Create a new SyncListInstance

        :param unicode unique_name: Human-readable name for this list
        :param unicode ttl: Time-to-live of this List in seconds, defaults to no expiration.

        :returns: Newly created SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        """
        data = values.of({'UniqueName': unique_name, 'Ttl': ttl, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return SyncListInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams SyncListInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_list.SyncListInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_list.SyncListInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SyncListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SyncListPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SyncListPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SyncListContext

        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.sync_list.SyncListContext
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListContext
        """
        return SyncListContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a SyncListContext

        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.sync_list.SyncListContext
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListContext
        """
        return SyncListContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncListList>'


class SyncListPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SyncListPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The unique SID identifier of the Service Instance that hosts this List object.

        :returns: twilio.rest.sync.v1.service.sync_list.SyncListPage
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListPage
        """
        super(SyncListPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncListInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        """
        return SyncListInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncListPage>'


class SyncListContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the SyncListContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.sync_list.SyncListContext
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListContext
        """
        super(SyncListContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Lists/{sid}'.format(**self._solution)

        # Dependents
        self._sync_list_items = None
        self._sync_list_permissions = None

    def fetch(self):
        """
        Fetch a SyncListInstance

        :returns: Fetched SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the SyncListInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, ttl=values.unset):
        """
        Update the SyncListInstance

        :param unicode ttl: The ttl

        :returns: Updated SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        """
        data = values.of({'Ttl': ttl, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    @property
    def sync_list_items(self):
        """
        Access the sync_list_items

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemList
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemList
        """
        if self._sync_list_items is None:
            self._sync_list_items = SyncListItemList(
                self._version,
                service_sid=self._solution['service_sid'],
                list_sid=self._solution['sid'],
            )
        return self._sync_list_items

    @property
    def sync_list_permissions(self):
        """
        Access the sync_list_permissions

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_permission.SyncListPermissionList
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_permission.SyncListPermissionList
        """
        if self._sync_list_permissions is None:
            self._sync_list_permissions = SyncListPermissionList(
                self._version,
                service_sid=self._solution['service_sid'],
                list_sid=self._solution['sid'],
            )
        return self._sync_list_permissions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncListContext {}>'.format(context)


class SyncListInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the SyncListInstance

        :returns: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        """
        super(SyncListInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'url': payload['url'],
            'links': payload['links'],
            'revision': payload['revision'],
            'date_expires': deserialize.iso8601_datetime(payload['date_expires']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'created_by': payload['created_by'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SyncListContext for this SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListContext
        """
        if self._context is None:
            self._context = SyncListContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique 34-character SID identifier of the List.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: The unique and addressable name of this List.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Twilio Account.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The unique SID identifier of the Service Instance that hosts this List object.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL for this List.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: A dictionary of URL links to nested resources of this List.
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def revision(self):
        """
        :returns: Contains the current revision of this List, represented by a string identifier.
        :rtype: unicode
        """
        return self._properties['revision']

    @property
    def date_expires(self):
        """
        :returns: Contains the date this List expires and gets deleted automatically.
        :rtype: datetime
        """
        return self._properties['date_expires']

    @property
    def date_created(self):
        """
        :returns: The date this List was created, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: Specifies the date this List was last updated, given in UTC ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: The identity of the List creator.
        :rtype: unicode
        """
        return self._properties['created_by']

    def fetch(self):
        """
        Fetch a SyncListInstance

        :returns: Fetched SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SyncListInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, ttl=values.unset):
        """
        Update the SyncListInstance

        :param unicode ttl: The ttl

        :returns: Updated SyncListInstance
        :rtype: twilio.rest.sync.v1.service.sync_list.SyncListInstance
        """
        return self._proxy.update(ttl=ttl, )

    @property
    def sync_list_items(self):
        """
        Access the sync_list_items

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemList
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_item.SyncListItemList
        """
        return self._proxy.sync_list_items

    @property
    def sync_list_permissions(self):
        """
        Access the sync_list_permissions

        :returns: twilio.rest.sync.v1.service.sync_list.sync_list_permission.SyncListPermissionList
        :rtype: twilio.rest.sync.v1.service.sync_list.sync_list_permission.SyncListPermissionList
        """
        return self._proxy.sync_list_permissions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncListInstance {}>'.format(context)
