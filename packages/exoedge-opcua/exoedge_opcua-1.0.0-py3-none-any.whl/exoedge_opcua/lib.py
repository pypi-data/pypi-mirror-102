import logging
import time

from opcua import Client, ua

LOG = logging.getLogger('exoedge.' + __name__)


class OpcuaClient(object):
    def __init__(self, url):
        self.count = 1
        self.connected = False
        try:
            self.client = Client(url)

        except Exception:
            raise

    def reconnect(self):
        if not self.connected:
            try:
                self.client.connect()
            except IOError as error:
                time.sleep(1)
                LOG.info(error)
                self.reconnect()
            else:
                self.connected = True

    def get_children(self, node_id=None):
        if node_id:
            obj = self.client.get_node(node_id)
            return obj.get_children()
        else:
            root = self.client.get_root_node()
            return root.get_children()

    def poll(self, node_id):
        node = self.client.get_node(node_id)
        val = node.get_value()

        return val

    def subscribe(self, put_channel_error, node_id, event_id, callback):
        self.subscribing = True
        try:
            self._subscribe(node_id, event_id, callback)
            while self.subscribing:
                time.sleep(1)
        except Exception as err:
            put_channel_error(err)

    def _subscribe(self, node_id, event_id, callback):
        args = []
        try:
            self.sub = self.client.create_subscription(100, callback)
            if node_id:
                args.append(str(node_id))
            if event_id:
                args.append(str(event_id))

            self.handle = self.sub.subscribe_events(*args)
        except Exception:
            raise

    def unsubscribe(self):
        if hasattr(self, 'sub') and hasattr(self, 'handle'):
            self.subscribing = False
            self.sub.unsubscribe(self.handle)
            self.sub.delete()

    def call_method(self, call_method_args, put_channel_error, put_sample, sample_rate=1000):
        while self.connected:
            try:
                res = self._call_method(**call_method_args)
                put_sample(res)
            except ua.UaStatusCodeError as err:
                put_channel_error(err)
            except Exception as err:
                put_channel_error(err)
            time.sleep(sample_rate/1000)

    def _call_method(self, node_id, path, method=None, method_name=None, args=None):
        try:
            node = self.get_node(node_id, path)
            methods = node.get_methods()
            method_id = None

            if (method_name is not None):
                method_id = str(method_name)
            elif (method is None):
                if (len(methods) == 0):
                    raise ValueError(
                        "No methods in selected node and no method given")
                elif (len(methods) == 1):
                    method_id = methods[0]
                else:
                    raise ValueError(
                        "Selected node has {0:d} methods but no method given. Provide one of {1!s}".format(*(methods)))
            else:
                for m in methods:
                    if (m.nodeid.Identifier == method):
                        method_id = m.nodeid
                        break

            if (method_id is None):
                method_id = ua.NodeId(identifier=method)

            if args:
                res = node.call_method(method_id, *args)
            else:
                res = node.call_method(method_id)
            return res
        except Exception:
            raise

    def get_node(self, nodeid='i=84', path=None):
        node = self.client.get_node(nodeid)
        if path:
            path_array = path.split(",")
            if node.nodeid == ua.NodeId(84, 0) and path_array[0] == "0:Root":
                # let user specify root if not node given
                path_array = path_array[1:]
            node = node.get_child(path_array)
        return node

    def disconnect(self):
        self.unsubscribe()
        try:
            # calling client.disconnect creates exception when client is not connected to server
            # https://github.com/FreeOpcUa/python-opcua/issues/522
            self.client.disconnect()
        except Exception:
            pass

        self.connected = False
        LOG.critical("NETWORK HAS BEEN DISCONNECTED.")
