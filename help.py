from typing import Any, Sequence, Optional
import discord
from discord.ext.commands import DefaultHelpCommand, Command


class MyHelpCommand(DefaultHelpCommand):
    def add_indented_commands(
        self, commands: Sequence[Command[Any, Any, Any]], /, *,
            heading: str, max_size: Optional[int] = None
    ) -> None:
        """ Almost a carbon copy of the original implementation, except for
        some formatting adjustments to make the output look better

        ---

        Indents a list of commands after the specified heading.

        The formatting is added to the :attr:`paginator`.

        The default implementation is the command name indented by
        :attr:`indent` spaces, padded to ``max_size`` followed by
        the command's :attr:`Command.short_doc` and then shortened
        to fit into the :attr:`width`.

        .. versionchanged:: 2.0

            ``commands`` parameter is now positional-only.

        Parameters
        -----------
        commands: Sequence[:class:`Command`]
            A list of commands to indent for output.
        heading: :class:`str`
            The heading to add to the output. This is only added
            if the list of commands is greater than 0.
        max_size: Optional[:class:`int`]
            The max size to use for the gap between indents.
            If unspecified, calls :meth:`~HelpCommand.get_max_size` on the
            commands parameter.
        """

        if not commands:
            return

        self.paginator.add_line(heading)
        max_size = max_size or self.get_max_size(commands)

        get_width = discord.utils._string_width
        for command in commands:
            name = command.name
            width = max_size - (get_width(name) - len(name))
            entry = f'{self.indent * " "} {name:<{width}}:\n' \
                    f'{2 * self.indent * " "} {command.short_doc}'
            self.paginator.add_line(self.shorten_text(entry))
