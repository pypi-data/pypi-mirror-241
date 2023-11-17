from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import TERMINATE
from cleo.events.event import Event
from cleo.events.event_dispatcher import EventDispatcher
from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin


class PoetryAutoExport(ApplicationPlugin):
    def activate(self, application: Application):
        if not application.event_dispatcher:
            return
        application.event_dispatcher.add_listener(TERMINATE, self.export)
        return super().activate(application)

    def export(self, event: Event, event_name: str, dispatcher: EventDispatcher):
        if not isinstance(event, ConsoleCommandEvent):
            return

        if event.command.name not in ["lock", "update", "add"]:
            return

        event.io.output.write_line("Poetry Auto Export Activated")
