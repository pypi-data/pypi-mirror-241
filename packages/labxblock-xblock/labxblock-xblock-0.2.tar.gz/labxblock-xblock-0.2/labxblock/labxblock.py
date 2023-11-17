"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope , String


class LabXBlock(XBlock):
   
 

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the LabXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/labxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/labxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/labxblock.js"))
        frag.initialize_js('LabXBlock')
        return frag

    def studio_view(self, context):
        """
        The view for editing the AudioXBlock parameters inside Studio.
        """
        html = self.resource_string("static/html/labxblock_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/labxblock_edit.js"))
        frag.initialize_js('LabEditBlock')
        return frag   

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("LabXBlock",
             """<labxblock/>
             """),
            ("Multiple LabXBlock",
             """<vertical_demo>
                <labxblock/>
                <labxblock/>
                <labxblock/>
                </vertical_demo>
             """),
        ]
