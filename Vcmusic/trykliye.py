import asyncio

import os

from datetime import datetime, timedelta

import ffmpeg

from pyrogram import Client, filters, emoji

from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR

from pyrogram.types import Message

from pyrogram.utils import MAX_CHANNEL_ID

from pytgcalls import GroupCallFactory, GroupCallFileAction

class MusicPlayer(object):

    def __init__(self):

        self.group_call = None

        self.client = None

        self.chat_id = None

        self.start_time = None

        self.playlist = []

        self.msg = {}

async def update_start_time(self, reset=False):

        self.start_time = (

            None if reset

            else datetime.utcnow().replace(microsecond=0)

        )

async def send_playlist(self):

        playlist = self.playlist

        if not playlist:

            pl = f"{emoji.NO_ENTRY} empty playlist"

        else:

            if len(playlist) == 1:

                pl = f"{emoji.REPEAT_SINGLE_BUTTON} **Playlist**:\n"

            else:

                pl = f"{emoji.PLAY_BUTTON} **Playlist**:\n"

            pl += "\n".join([

                f"**{i}**. **[{x.audio.title}]({x.link})**"

                for i, x in enumerate(playlist)

            ])

        if mp.msg.get('playlist') is not None:

            await mp.msg['playlist'].delete()

        mp.msg['playlist'] = await send_text(pl)

