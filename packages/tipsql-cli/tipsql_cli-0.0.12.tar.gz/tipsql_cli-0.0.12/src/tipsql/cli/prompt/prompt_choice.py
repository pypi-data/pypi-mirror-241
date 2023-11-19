from typing import Sequence

from prompt_toolkit import HTML
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyPressEvent
from prompt_toolkit.key_binding.defaults import load_key_bindings
from prompt_toolkit.key_binding.key_bindings import KeyBindings, merge_key_bindings
from prompt_toolkit.layout import Layout
from prompt_toolkit.widgets import RadioList


class CoiceList(RadioList):
    open_character = "  ("


def prompt_choice[T](
    options: Sequence[tuple[T, str | HTML]] | list[T],
    value: T | None = None,
) -> T:
    if value is not None:
        return value

    new_options: list[tuple[T, str | HTML]] = []
    for option in options:
        if isinstance(option, tuple):
            new_options.append(option)  # type: ignore
        else:
            new_options.append((option, str(option)))

    radio_list = CoiceList(new_options)
    bindings = KeyBindings()

    @bindings.add("c-c")
    @bindings.add("c-d")
    def _cancel(event: KeyPressEvent):
        event.app.exit(result=None)

    @bindings.add("tab", eager=True)
    def _next(event: KeyPressEvent):
        selected_index = radio_list._selected_index
        if len(radio_list.values) == selected_index + 1:
            radio_list._selected_index = 0
        else:
            radio_list._selected_index = min(
                len(radio_list.values) - 1,
                radio_list._selected_index + 1,
            )
        radio_list._handle_enter()

    @bindings.add("enter", eager=True)
    def _select(event: KeyPressEvent):
        event.app.exit(result=radio_list.current_value)

    app = Application(
        layout=Layout(radio_list),
        key_bindings=merge_key_bindings([load_key_bindings(), bindings]),
        mouse_support=False,
        full_screen=False,
    )

    if (result := app.run()) is not None:
        return result
    else:
        raise KeyboardInterrupt()
