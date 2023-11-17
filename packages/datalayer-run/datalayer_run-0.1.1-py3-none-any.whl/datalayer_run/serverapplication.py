"""The Datalayer Run Server application."""

import os

from traitlets import Unicode

from jupyter_server.utils import url_path_join
from jupyter_server.extension.application import ExtensionApp, ExtensionAppJinjaMixin

from ._version import __version__

from .handlers.index.handler import IndexHandler
from .handlers.config.handler import ConfigHandler
from .handlers.jump.handler import JumpHandler
from .handlers.content.handler import ContentHandler
from .handlers.echo.handler import WsEchoHandler
from .handlers.relay.handler import WsRelayHandler
from .handlers.proxy.handler import WsProxyHandler
from .handlers.ping.handler import WsPingHandler

from .keys.keys import setup_keys


DEFAULT_STATIC_FILES_PATH = os.path.join(os.path.dirname(__file__), "./static")

DEFAULT_TEMPLATE_FILES_PATH = os.path.join(os.path.dirname(__file__), "./templates")


class DatalayerRunExtensionApp(ExtensionAppJinjaMixin, ExtensionApp):
    """The Datalayer Run Server extension."""

    name = "datalayer_run"

    extension_url = "/datalayer_run"

    load_other_extensions = True

    static_paths = [DEFAULT_STATIC_FILES_PATH]
    template_paths = [DEFAULT_TEMPLATE_FILES_PATH]

    config_a = Unicode("", config=True, help="Config A example.")
    config_b = Unicode("", config=True, help="Config B example.")
    config_c = Unicode("", config=True, help="Config C example.")

    def initialize_settings(self):
        setup_keys(self.log)

    def initialize_templates(self):
        self.serverapp.jinja_template_vars.update({"datalayer_run_version" : __version__})

    def initialize_handlers(self):
        pod_name_regex = r"(?P<pod_name>[\w\.\-%]+)"
        handlers = [
            ("datalayer_run", IndexHandler),
            (url_path_join("datalayer_run", "config"), ConfigHandler),
            (url_path_join("datalayer_run", "content"), ContentHandler),
            (r"/datalayer_run/jump/%s" % pod_name_regex, JumpHandler),
            (url_path_join("datalayer_run", "echo"), WsEchoHandler),
            (url_path_join("datalayer_run", "relay"), WsRelayHandler),
            (url_path_join("datalayer_run", "proxy"), WsProxyHandler),
            (url_path_join("datalayer_run", "ping"), WsPingHandler),
        ]
        self.handlers.extend(handlers)


# -----------------------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------------------

main = launch_new_instance = DatalayerRunExtensionApp.launch_instance
