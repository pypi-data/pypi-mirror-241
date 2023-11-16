"""Message Finder to match the specific message"""
import re
from re import Pattern
import inspect
from typing import List

from wechaty_plugin_contrib.config import (
    get_logger,
    Contact,
    Wechaty
)

from .finder import Finder


logger = get_logger("ContactFinder")


class ContactFinder(Finder):
    """Contact Finder can find contacts with options"""
    async def match(self, wechaty: Wechaty) -> List[Contact]:
        """match the contact"""
        logger.info(f'ContactFinder match({Wechaty})')

        contacts: List[Contact] = []

        for option in self.options:
            if isinstance(option, Pattern):

                # search from all of the friends
                re_pattern = re.compile(option)
                # match the room with regex pattern
                all_friends = await wechaty.Contact.find_all()
                for friend in all_friends:
                    alias = await friend.alias()
                    if re.match(re_pattern, friend.name) or re.match(re_pattern, alias):
                        contacts.append(friend)

            elif isinstance(option, str):
                contact = wechaty.Contact.load(option)
                await contact.ready()
                contacts.append(contact)

            # TODO: implement callback function to find contacts
            # elif hasattr(option, '__call__'):
            #     """check the type of the function
            #     refer: https://stackoverflow.com/a/56240578/6894382
            #     """
            #     if inspect.iscoroutinefunction(option):
            #         # pytype: disable=bad-return-type
            #         targets = await option(wechaty)
            #     else:
            #
            #     if isinstance(targets, List[Contact]):
            #         contacts.extend(targets)
            else:
                raise ValueError(f'unknown type option: {option}')
        return contacts
