"""
.. todo:: Document this.
"""

from __future__ import annotations
import royalnet.royaltyping as t

import logging
import math
import royalnet.engineer as engi
import click
import datetime

from . import bullets

log = logging.getLogger(__name__)


class ConsolePDAImplementation(engi.ConversationListImplementation):
    def _partialcommand_pattern(self, partial) -> str:
        if partial.syntax:
            return r"^{name}\s+{syntax}$"
        else:
            return r"^{name}$"

    @property
    def namespace(self):
        return "console"

    async def run(self, cycles: int = math.inf) -> t.NoReturn:
        """
        Run the main loop of the :class:`.ConsolePDA` for ``cycles`` cycles, or unlimited cycles if the parameter is
        :data:`True`.
        """

        while cycles > 0:
            message = click.prompt("", type=str, prompt_suffix=">>> ", show_default=False)
            log.debug(f"Received a new input: {message!r}")

            log.debug(f"Creating ConsoleMessageReceived from: {message!r}")
            projectile = bullets.ConsoleMessageReceived(_text=message, _timestamp=datetime.datetime.now())

            log.debug(f"Putting projectile: {projectile!r}")
            await self.put_projectile(key="TERMINAL", projectile=projectile)

            if isinstance(cycles, int):
                cycles -= 1

    async def _handle_conversation_exc(
            self,
            dispenser: engi.Dispenser,
            conv: engi.ConversationProtocol,
            exception: Exception,
    ) -> None:
        self.log.error(f"ERROR: {exception}")


__all__ = (
    "ConsolePDAImplementation",
)
