import argparse
import json
import os
import pylast
import requests
import subprocess
import time

from .config_helper import FipibarConfig
from datetime import datetime


class FipibarClient():

    def __init__(self):
        '''
        TODO: Add args/kwargs here.
        '''
        self.config = FipibarConfig()
        self.unique_fip_process_string = 'fipibar_magic_constant'

        # Thanks to Zopieux for the gist this came from:
        # https://gist.github.com/Zopieux/ccb8d29437765083e4c80da52f2145b2
        # URL for Fip Groove.
        self.details_url = 'https://api.radiofrance.fr/livemeta/pull/66'

        self.currently_playing_trunclen = int(
            self.config.get('currently_playing_trunclen', 45)
        )

        self.lastfm_client = self.get_lastfm_client()

    def get_lastfm_client(self):
        if any(
            [
                self.config.get('lastfm_should_heart', False),
                self.config.get('lastfm_should_scrobble', False),
            ]
        ):
            try:
                return pylast.LastFMNetwork(
                    api_key=self.config.get('lastfm_api_key', None),
                    api_secret=self.config.get('lastfm_api_secret', None),
                    username=self.config.get('lastfm_username', None),
                    password_hash=self.config.get('lastfm_password_hash', None),
                )
            except Exception as e:
                print("Please configure ~/.fipibar_config.json with last.fm details.")
                print(e)

    def is_currently_playing(self):
        '''
        Returns True if there is a currently playing song, False otherwise.
        '''
        try:
            return int(subprocess.check_output('ps aux | grep ' + self.unique_fip_process_string + ' | grep -v grep | grep -v python | wc -l', shell=True)) >= 1
        except Exception:
            return False

    def play(self):
        if not self.is_currently_playing():
            subprocess.check_output('bash -c "exec -a ' + self.unique_fip_process_string + ' ffplay -nodisp https://stream.radiofrance.fr/fipgroove/fipgroove_hifi.m3u8\?id\=radiofrance > /dev/null 2>&1 &"', shell=True)

    def pause(self):
        if self.is_currently_playing():
            subprocess.check_output('kill $(ps aux | grep ' + self.unique_fip_process_string + ' | grep -v grep | awk -e \'{printf $2}\')', shell=True)

    def toggle_playback(self):
        '''
        Plays the current track if currently paused. Pauses current track if
        currently playing.
        '''
        if self.is_currently_playing():
            self.pause()
        else:
            self.play()

    def get_currently_playing_string(self):
        '''
        Returns the string displayed in Polybar for currently playing
        track/artist.
        '''
        try:
            data = requests.get(self.details_url).json()

            level = data['levels'][0]
            uid = level['items'][level['position']]
            step = data['steps'][uid]

            currently_playing_string = f"{step['title']} - {step['authors']}"

            if self.config.get('current_track', '') != currently_playing_string:
                if self.config.get('should_notify', False):
                    subprocess.check_call(
                        [
                            'notify-send',
                            '-i',
                            'applications-multimedia',
                            'FIP radio',
                            currently_playing_string
                        ]
                    )

                if self.config.get('lastfm_should_scrobble', False):
                    self.lastfm_client.update_now_playing(
                        artist=step['authors'],
                        title=step['title']
                    )

                    self.lastfm_client.scrobble(
                        artist=step['authors'],
                        title=step['title'],
                        timestamp=datetime.utcnow()
                    )

                self.config.set('current_track', currently_playing_string)

            if len(currently_playing_string) > self.currently_playing_trunclen:
                return currently_playing_string[:self.currently_playing_trunclen - 3] + '...'
            else:
                return currently_playing_string

            return msg
        except:
            return 'Can\'t find details...'


def main():
    fipibar_client = FipibarClient()

    parser = argparse.ArgumentParser(
        description='Entrypoint for Fip Radio/Polybar integration.'
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--get-currently-playing", action="store_true")
    group.add_argument("--toggle-playback", action="store_true")

    args = parser.parse_args()

    if args.get_currently_playing:
        print(fipibar_client.get_currently_playing_string())
    elif args.toggle_playback:
        fipibar_client.toggle_playback()


if __name__ == '__main__':
    main()
