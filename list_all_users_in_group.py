#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Return sorted list of all users of group GROUP

Script 'list_all_users_in_group' return sorted list of all users of group GROUP

License: CC0 1.0 Universal or newer.
Origin sources is in https://github.com/vazhnov/list_all_users_in_group
"""

# pylint: disable=line-too-long

from __future__ import print_function
import grp
import pwd
import inspect
import argparse
import sys


def list_all_users_in_group(groupname):
    """Get list of all users of group.

    Get sorted list of all users of group GROUP,
    including users with main group GROUP.

    """
    try:
        group = grp.getgrnam(groupname)
    # On error "KeyError: 'getgrnam(): name not found: GROUP'"
    except KeyError:
        return None
    group_all_users_set = set(group.gr_mem)
    for user in pwd.getpwall():
        if user.pw_gid == group.gr_gid:
            group_all_users_set.add(user.pw_name)
    return sorted(group_all_users_set)


def main():
    parser = argparse.ArgumentParser(description=inspect.getdoc(sys.modules[__name__]),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--delimiter', default='\n', help='Use DELIMITER instead of newline for users delimiter')
    parser.add_argument('groupname', help='Group name')
    args = parser.parse_args()
    result = list_all_users_in_group(args.groupname)
    if result:
        print(args.delimiter.join(result))


if __name__ == "__main__":
    main()
