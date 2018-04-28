# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class MessageInteractionList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, session_sid, participant_sid):
        """
        Initialize the MessageInteractionList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param session_sid: Session Sid.
        :param participant_sid: Participant Sid.

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionList
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionList
        """
        super(MessageInteractionList, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'session_sid': session_sid,
            'participant_sid': participant_sid,
        }
        self._uri = '/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions'.format(**self._solution)

    def create(self, body=values.unset, media_url=values.unset):
        """
        Create a new MessageInteractionInstance

        :param unicode body: Message body
        :param unicode media_url: The media_url

        :returns: Newly created MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance
        """
        data = values.of({'Body': body, 'MediaUrl': serialize.map(media_url, lambda e: e), })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return MessageInteractionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            participant_sid=self._solution['participant_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams MessageInteractionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists MessageInteractionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of MessageInteractionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return MessageInteractionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInteractionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MessageInteractionPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MessageInteractionContext

        :param sid: The sid

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionContext
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionContext
        """
        return MessageInteractionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            participant_sid=self._solution['participant_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a MessageInteractionContext

        :param sid: The sid

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionContext
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionContext
        """
        return MessageInteractionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            participant_sid=self._solution['participant_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.MessageInteractionList>'


class MessageInteractionPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the MessageInteractionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.
        :param session_sid: Session Sid.
        :param participant_sid: Participant Sid.

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionPage
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionPage
        """
        super(MessageInteractionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInteractionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance
        """
        return MessageInteractionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            participant_sid=self._solution['participant_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.MessageInteractionPage>'


class MessageInteractionContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, session_sid, participant_sid, sid):
        """
        Initialize the MessageInteractionContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param session_sid: The session_sid
        :param participant_sid: The participant_sid
        :param sid: The sid

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionContext
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionContext
        """
        super(MessageInteractionContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'session_sid': session_sid,
            'participant_sid': participant_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Sessions/{session_sid}/Participants/{participant_sid}/MessageInteractions/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a MessageInteractionInstance

        :returns: Fetched MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return MessageInteractionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            participant_sid=self._solution['participant_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.MessageInteractionContext {}>'.format(context)


class MessageInteractionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Type(object):
        MESSAGE = "message"
        VOICE = "voice"
        UNKNOWN = "unknown"

    class ResourceStatus(object):
        ACCEPTED = "accepted"
        ANSWERED = "answered"
        BUSY = "busy"
        CANCELED = "canceled"
        COMPLETED = "completed"
        DELETED = "deleted"
        DELIVERED = "delivered"
        DELIVERY_UNKNOWN = "delivery-unknown"
        FAILED = "failed"
        IN_PROGRESS = "in-progress"
        INITIATED = "initiated"
        NO_ANSWER = "no-answer"
        QUEUED = "queued"
        RECEIVED = "received"
        RECEIVING = "receiving"
        RINGING = "ringing"
        SCHEDULED = "scheduled"
        SENDING = "sending"
        SENT = "sent"
        UNDELIVERED = "undelivered"
        UNKNOWN = "unknown"

    def __init__(self, version, payload, service_sid, session_sid, participant_sid,
                 sid=None):
        """
        Initialize the MessageInteractionInstance

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance
        """
        super(MessageInteractionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'session_sid': payload['session_sid'],
            'service_sid': payload['service_sid'],
            'account_sid': payload['account_sid'],
            'data': payload['data'],
            'type': payload['type'],
            'participant_sid': payload['participant_sid'],
            'inbound_participant_sid': payload['inbound_participant_sid'],
            'inbound_resource_sid': payload['inbound_resource_sid'],
            'inbound_resource_status': payload['inbound_resource_status'],
            'inbound_resource_type': payload['inbound_resource_type'],
            'inbound_resource_url': payload['inbound_resource_url'],
            'outbound_participant_sid': payload['outbound_participant_sid'],
            'outbound_resource_sid': payload['outbound_resource_sid'],
            'outbound_resource_status': payload['outbound_resource_status'],
            'outbound_resource_type': payload['outbound_resource_type'],
            'outbound_resource_url': payload['outbound_resource_url'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'session_sid': session_sid,
            'participant_sid': participant_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MessageInteractionContext for this MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionContext
        """
        if self._context is None:
            self._context = MessageInteractionContext(
                self._version,
                service_sid=self._solution['service_sid'],
                session_sid=self._solution['session_sid'],
                participant_sid=self._solution['participant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Message Interaction.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def session_sid(self):
        """
        :returns: Session Sid.
        :rtype: unicode
        """
        return self._properties['session_sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def data(self):
        """
        :returns: Message body
        :rtype: unicode
        """
        return self._properties['data']

    @property
    def type(self):
        """
        :returns: The Type of this Message Interaction
        :rtype: MessageInteractionInstance.Type
        """
        return self._properties['type']

    @property
    def participant_sid(self):
        """
        :returns: Participant Sid.
        :rtype: unicode
        """
        return self._properties['participant_sid']

    @property
    def inbound_participant_sid(self):
        """
        :returns: Inbound Participant Sid.
        :rtype: unicode
        """
        return self._properties['inbound_participant_sid']

    @property
    def inbound_resource_sid(self):
        """
        :returns: Inbound message resource Sid.
        :rtype: unicode
        """
        return self._properties['inbound_resource_sid']

    @property
    def inbound_resource_status(self):
        """
        :returns: The Inbound Resource Status of this Message Interaction
        :rtype: MessageInteractionInstance.ResourceStatus
        """
        return self._properties['inbound_resource_status']

    @property
    def inbound_resource_type(self):
        """
        :returns: Message
        :rtype: unicode
        """
        return self._properties['inbound_resource_type']

    @property
    def inbound_resource_url(self):
        """
        :returns: The URL of the Twilio message resource.
        :rtype: unicode
        """
        return self._properties['inbound_resource_url']

    @property
    def outbound_participant_sid(self):
        """
        :returns: Outbound Participant Sid.
        :rtype: unicode
        """
        return self._properties['outbound_participant_sid']

    @property
    def outbound_resource_sid(self):
        """
        :returns: Outbound message resource Sid.
        :rtype: unicode
        """
        return self._properties['outbound_resource_sid']

    @property
    def outbound_resource_status(self):
        """
        :returns: The Outbound Resource Status of this Message Interaction
        :rtype: MessageInteractionInstance.ResourceStatus
        """
        return self._properties['outbound_resource_status']

    @property
    def outbound_resource_type(self):
        """
        :returns: Message
        :rtype: unicode
        """
        return self._properties['outbound_resource_type']

    @property
    def outbound_resource_url(self):
        """
        :returns: The URL of the Twilio message resource.
        :rtype: unicode
        """
        return self._properties['outbound_resource_url']

    @property
    def date_created(self):
        """
        :returns: The date this Message Interaction was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Message Interaction was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a MessageInteractionInstance

        :returns: Fetched MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.MessageInteractionInstance {}>'.format(context)
