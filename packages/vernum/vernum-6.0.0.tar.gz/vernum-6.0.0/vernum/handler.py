import os
from subprocess import run
from argparse import ArgumentParser
import re
from dataclasses import dataclass


FORMAT = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)(?:\.(beta|alpha)(\d+))?$")


def read_version_string(string):
    if match := FORMAT.match(string):
        v = tuple(
            (
                int(x) if ((x is not None) and x.isdigit()) else x
            ) for x in match.groups()
        )
        return v


def write_version_string(major, minor, patch, interim, count):
    if interim:
        return f"{major}.{minor}.{patch}.{interim}{count}"
    else:
        return f"{major}.{minor}.{patch}"


def git(command):
    result = run(['git'] + command.split(),
                 capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(result.stderr)
    return result.stdout.strip()


LEVELS = ['major', 'minor', 'patch']
INTERIM = ['alpha', 'beta', 'release']


@dataclass
class Handler:

    set_current: list
    level: str = ''
    interim: str = ''
    debug: bool = False

    @property
    def current(self):
        if not hasattr(self, '_current'):
            if self.set_current:
                self._current = read_version_string(
                    self.set_current[0].strip())
            else:
                branch = git("branch --show-current")
                tags = git(f"tag --merged {branch}")
                self._current = (0, 0, 0, '', 0)
                for tag in tags.split('\n'):
                    if version := read_version_string(tag):
                        if version > self._current:
                            self._current = version
        if not self._current:
            raise RuntimeError(f"Incorrect or missing current version")
        return self._current

    def update_version(self):

        # Note that self. holds the requested change

        major, minor, patch, interim, count = self.current

        # Figure out what level we are on

        if patch == 0:
            if minor == 0:
                level = 'major'
            else:
                level = 'minor'
        else:
            level = 'patch'

        # First figure out the alpha and beta situation

        increment = False
        if self.interim == 'release':        # We want to release something
            if interim:                      # Current is alpha or beta
                interim = ''
                count = 0
            else:                            # Current is numbered so increment
                increment = True
        else:                                # We want to push an alpha or beta
            if level == self.level:      # Special case when keeping our level
                if interim == self.interim:  # Inc the current alpha or beta
                    count += 1
                elif self.interim == 'beta':  # From alpha to beta
                    interim = 'beta'
                    count = 1
                else:                        # From beta to alpha, so increment
                    increment = True
                    interim = 'alpha'
                    count = 1
            else:                        # Changing levels with alpha or beta
                increment = True
                interim = self.interim
                count = 1

        # Increment the actual version number if appropriate

        if increment:
            if self.level == 'patch':
                patch += 1
            elif self.level == 'minor':
                minor += 1
                patch = 0
            elif self.level == 'major':
                major += 1
                minor = patch = 0

        return major, minor, patch, interim, count

    def do(self):
        version = self.update_version() if self.level else self.current
        return write_version_string(*version)


def main():
    parser = ArgumentParser()
    parser.add_argument('level', choices=LEVELS, nargs='?', default='patch')
    parser.add_argument('interim', choices=INTERIM,
                        nargs='?', default='release')
    parser.add_argument('--set-current', '-s', action='store', nargs=1)
    namespace = parser.parse_args()
    handler = Handler(**vars(namespace))
    print(handler.do())
