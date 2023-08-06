import logging
import operator
import threading
import time
import traceback

from exoedge.sources import ExoEdgeSource
from exoedge_opcua.lib import OpcuaClient

LOG = logging.getLogger('exoedge.' + __name__)
LOG.setLevel(logging.INFO)


class OpcuaExoEdgeSource(ExoEdgeSource):
    def __init__(self):
        super(OpcuaExoEdgeSource, self).__init__()

    def get_source(self):
        return super(OpcuaExoEdgeSource, self).get_source()

    def put_data_out(self, channel, data):
        """
        TODO
        """
        try:
            pass
        except Exception as exc:
            LOG.exception("OPC UA PUT DATA OUT: {}".format(exc))

    def run(self):
        # Do not combine instantiations and connect loop function.
        # Call function stop would fail. Because stop can't get instantiations when processing connect.
        self.instantiations = self.instantiate()
        self.connect_server()
        self.run_channels()

    def run_channels(self):
        channels = self.get_channels_by_application("opcua")
        #Handle subscriptions once
        for channel in channels:
            try:
                LOG.info("POLLING OPC UA CHANNEL: {}".format(channel.name))
                app_specific_config = channel.protocol_config.app_specific_config

                if app_specific_config.get('function') == 'subscribe':
                    self.subscribe(channel)
                elif app_specific_config.get('function') == 'get_children':
                    self.get_children(channel)
                elif app_specific_config.get('function') == 'call_method':
                    self.call_method(channel)
                else:
                    self.get_children(channel)

            except Exception as exc:
                LOG.exception("OPC UA EXCEPTION: {}".format(exc))
                channel.put_channel_error(exc)

        #Handle polling
        while not self.is_stopped():
            for channel in channels:
                app_specific_config = channel.protocol_config.app_specific_config
                if app_specific_config.get('function') == 'poll' and channel.is_sample_time():
                    self.poll(channel)

            time.sleep(0.1)

    def instantiate(self):
        instantiations = {}
        for iface in self.interfaces:
            try:
                LOG.info("create OPC UA instantiation: {}".format(iface))
                opcuaClient = OpcuaClient(url=iface.get("url"))
                instantiations[iface.get("interface")] = opcuaClient
            except Exception as exc:
                LOG.exception("OPC UA EXCEPTION: {}".format(exc))

        return instantiations

    def connect_server(self):
        for instantiation in self.instantiations.values():
            try:
                instantiation.client.connect()
                instantiation.connected = True
            except IOError as error:
                LOG.error(error)
                instantiation.reconnect()

    def thread(self, target, kwargs, name):
        t = threading.Thread(target=target, kwargs=kwargs, name=name)
        t.start()

    def poll(self, channel):
        try:
            client = self.instantiations[channel.protocol_config.interface]
            app_specific_config = channel.protocol_config.app_specific_config
            parameters = app_specific_config.get('parameters')

            res = client.poll(
                    node_id=parameters.get('node_id')
                )

        except Exception as exc: #pylint: disable=W0703
            LOG.exception("Exception" .format(format_exc=exc))
            channel.put_channel_error(traceback.format_exc(exc))
        else:
            channel.put_sample(res)

    def subscribe(self, channel):
        app_specific_config = channel.protocol_config.app_specific_config
        parameters = app_specific_config.get('parameters')

        class SubHandler(object):
            def event_notification(self, event):
                object_path = parameters.get('object_path')
                if object_path:
                    try:
                        attr = operator.attrgetter(object_path)(event)
                    except AttributeError as error:
                        LOG.error(error)
                        attr = event.Message.Text
                    channel.put_sample(attr)
                else:
                    channel.put_sample(event.Message.Text)

        callback = SubHandler()
        self.thread(
            target=self.instantiations[channel.protocol_config.interface].subscribe,
            kwargs={
                'node_id': parameters.get('node_id'),
                'event_id': parameters.get('event_id'),
                'callback': callback,
                'put_channel_error': channel.put_channel_error
            },
            name='Ch:{} Fun:subscribe'.format(channel.channel_name)
        )

    def get_children(self, channel):
        try:
            app_specific_config = channel.protocol_config.app_specific_config
            parameters = app_specific_config.get('parameters')
            res = self.instantiations[channel.protocol_config.interface].get_children(
                node_id=parameters.get('node_id')
            )
        except Exception as error:
            channel.put_channel_error(error)
        else:
            channel.put_sample(res)

    def call_method(self, channel):
        app_specific_config = channel.protocol_config.app_specific_config
        parameters = app_specific_config.get('parameters')
        call_method_args = {
            'node_id': parameters.get('node_id', 'i=84'),
            'path': parameters.get('path'),
            'method': parameters.get('method'),
            'method_name': parameters.get('method_name'),
            'args': parameters.get('args'),
        }

        self.thread(
            target=self.instantiations[channel.protocol_config.interface].call_method,
            kwargs={
                'call_method_args': call_method_args,
                'put_channel_error': channel.put_channel_error,
                'put_sample': channel.put_sample,
                'sample_rate': channel.protocol_config.sample_rate
            },
            name='Ch:{} Fun:call_method'.format(channel.channel_name)
        )

    @property
    def interfaces(self):
        """
        Example:
        >>> self.interfaces
        [{
          "url" : "opc.tcp://localhost:40840/freeopcua/server/"
        }]
        """
        configured_applications = self.get_configured_applications()

        while not configured_applications:
            LOG.critical("Resource 'config_applications' not set.")
            configured_applications = self.get_configured_applications()
            time.sleep(1.0)

        applications = configured_applications.get('applications')
        opcua = applications.get('opcua')
        interfaces = opcua.get("interfaces")
        return interfaces

    def stop(self):
        for instantiation in self.instantiations.values():
            instantiation.disconnect()
        LOG.critical("exoedge.{} HAS BEEN STOPPED.".format(__name__))

    def join(self, time):
        # config_io will call source.stop_source and source.join, using stop_source is enough.
        # stop_source will call stop.
        pass
