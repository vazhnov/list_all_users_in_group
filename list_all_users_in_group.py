#! /usr/bin/env python
# -*- coding: utf-8 -*-

import grp
import pwd
import sys


def list_all_users_in_group(groupname):
    """Get list of all users of group.

    Get sorted list of all users of group GROUP,
    including users with main group GROUP."""
    group = grp.getgrnam(groupname)
    group_all_users_set = set(group.gr_mem)
    for user in pwd.getpwall():
        if user.pw_gid == group.gr_gid:
            group_all_users_set.add(user.pw_name)
    return sorted(group_all_users_set)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print (' '.join(list_all_users_in_group(sys.argv[1])))
    else:
        print(list_all_users_in_group.__doc__)
        sys.exit('Usage: {} groupname'.format(sys.argv[0]))
