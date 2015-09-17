#! /usr/bin/env python
# -*- coding: utf-8 -*-

import grp
import pwd
import sys
import inspect


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
    if len(sys.argv) == 2:
        result = list_all_users_in_group(sys.argv[1])
        if result:
            print ('\n'.join(result))
    else:
        print(inspect.cleandoc(list_all_users_in_group.__doc__))
        sys.exit('\nUsage: {} groupname'.format(sys.argv[0]))
