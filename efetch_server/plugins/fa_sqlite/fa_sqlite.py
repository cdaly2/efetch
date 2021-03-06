"""
Lazy loading SQLite viewer
"""

from yapsy.IPlugin import IPlugin
import os


class FaSqlite(IPlugin):
    def __init__(self):
        self.display_name = 'SQLite Viewer'
        self.popularity = 7
        self.cache = True
        self.fast = False
        self.action = False
        self.icon = 'fa-database'
        IPlugin.__init__(self)

    def activate(self):
        IPlugin.activate(self)
        return

    def deactivate(self):
        IPlugin.deactivate(self)
        return

    def check(self, evidence, path_on_disk):
        """Checks if the file is compatible with this plugin"""
        allowed_mimetype = ['application/octet-stream']
        allowed_extensions = ['sqlite', 'QuarantineEvents', 'QuarantineEventsV2']
        return str(evidence['mimetype']).lower() in allowed_mimetype and evidence['extension'].lower() in allowed_extensions

    def mimetype(self, mimetype):
        """Returns the mimetype of this plugins get command"""
        return "text/plain"

    def get(self, evidence, helper, path_on_disk, request):
        """Returns the result of this plugin to be displayed in a browser"""
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        template = open(curr_dir + '/sqlite_template.html', 'r')
        html = str(template.read())
        html = html.replace("<!-- Query -->", evidence['url_query'])
        template.close()

        return html
