#! /usr/bin/env python
# -*- coding: utf-8 -*-

import grp
import pwd
import inspect
import argparse


def list_all_users_in_group(groupname):
    """Get list of all users of group.

    Get sorted list of all users of group GROUP,
    including users with main group GROUP.
    Origin in https://github.com/vazhnov/list_all_users_in_group

    """
    try:
        group = grp.getgrnam(groupname)
    # On error "KeyError: 'getgrnam(): name not found: GROUP'"
    except (KeyError):
        return None
    group_all_users_set = set(group.gr_mem)
    for user in pwd.getpwall():
        if user.pw_gid == group.gr_gid:
            group_all_users_set.add(user.pw_name)
    return sorted(group_all_users_set)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=inspect.cleandoc(list_all_users_in_group.__doc__),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--delimiter', default='\n', help='Use DELIMITER instead of newline for users delimiter')
    parser.add_argument('groupname', help='Group name')
    args = parser.parse_args()
    result = list_all_users_in_group(args.groupname)
    if result:
        print (args.delimiter.join(result))
