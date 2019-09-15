import sublime
import sublime_plugin


class StartTourInputHandler(sublime_plugin.ListInputHandler):
    def name(self):
        return "tour_name"

    def list_items(self):
        return ["abc", "xyz"]

class StartTourCommand(sublime_plugin.TextCommand):
    def input(self, args):
        return StartTourInputHandler()

    def run(self, edit, tour_name):
        self.view.insert(edit, 0, tour_name)
