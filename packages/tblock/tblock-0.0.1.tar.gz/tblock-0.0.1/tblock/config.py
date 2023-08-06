# TBlock - An anticapitalist ad-blocker that uses the hosts file
# Copyright (C) 2021 Twann <twann@ctemplar.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

########################################################################################################################
# This module is the base configuration for TBlock. It contains paths to files and url of repo index. It also creates  #
# files and directories needed by TBlock automatically when TBlock is launched.                                        #
########################################################################################################################

# Standard libraries
import os
import sqlite3


def setup_database(db_path: str) -> None:
    """Setup the SQLite3 database

    Args:
        db_path (str): The path to the database to setup
    """
    with sqlite3.connect(os.path.realpath(db_path)) as db:
        db.cursor().execute('''CREATE TABLE IF NOT EXISTS "rules" (
            "domain"	TEXT NOT NULL UNIQUE,
            "policy"	TEXT NOT NULL,
            "filter_id"	TEXT NOT NULL,
            "priority"	INTEGER NOT NULL,
            "ip"	TEXT
        );''')
        db.cursor().execute('''CREATE TABLE IF NOT EXISTS "filters" (
            "id"	TEXT NOT NULL UNIQUE,
            "source"	TEXT NOT NULL UNIQUE,
            "metadata"	TEXT NOT NULL,
            "subscribing"	INTEGER NOT NULL,
            "on_rfr"	INTEGER NOT NULL,
            "permissions"   TEXT
        );''')
        db.commit()


database = '/var/lib/tblock/storage.sqlite'
default_hosts = '/var/lib/tblock/hosts'
hosts = '/etc/hosts'
tmp_dir = '/tmp/tblock/'
remote_repo = 'https://codeberg.org/tblock/remote-filters-repository/raw/branch/main/index.xml'
remote_repo_mirror = 'https://0xacab.org/twann/remote-filters-repository-mirror/-/raw/main/index.xml'
default_ip = '127.0.0.1'
remote_repo_version_db = '/var/lib/tblock/repo'
lib_dir = '/var/lib/tblock/'

try:
    if not os.path.isdir(tmp_dir):
        os.mkdir(tmp_dir)

    if not os.path.isdir(lib_dir):
        os.mkdir(lib_dir)

    if not os.path.isfile(database):
        setup_database(database)
except PermissionError:
    pass
