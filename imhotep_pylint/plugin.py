from imhotep.tools import Tool
import os
import re

class PyLint(Tool):
    response_format = re.compile(r'(?P<filename>.*):(?P<line_num>\d+):'
                                 '(?P<message>.*)')
    pylintrc_filename = '.pylintrc'

    def get_file_extensions(self):
        return ['.py']

    def process_line(self, dirname, line):
        match = self.response_format.search(line)
        if match is not None:
            if len(self.filenames) != 0:
                if match.group('filename') not in self.filenames:
                    return
            filename, line, messages = match.groups()
            # If you run pylint on /foo/bar/baz and you are in the /foo/bar
            # directory, it will spit out paths that look like: ./baz To fix
            # this, we run it through `os.path.abspath` which will give it a
            # full, absolute path.
            filename = os.path.abspath(filename)
            return filename, line, messages

    def get_command(self, dirname):
        cmd = 'pylint --output-format=parseable -rn'
        if os.path.exists(os.path.join(dirname, self.pylintrc_filename)):
            cmd += " --rcfile=%s" % os.path.join(
                dirname, self.pylintrc_filename)
        return cmd
