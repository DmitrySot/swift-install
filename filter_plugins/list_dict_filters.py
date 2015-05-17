# --------------------------------------------------------------------------
# Copyright IBM Corp. 2015, 2015 All Rights Reserved
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# Limitations under the License.
# --------------------------------------------------------------------------
# Written By George Goldberg (georgeg@il.ibm.com)


def dict_path(d, path):
    l = d
    name = path
    for i in path.split('.'):
        l = l[i]
        name = i

    return (name, l)


def extractfromdict(d, l):
    r = []
    for f in l:
        r.append(dict_path(d, f)[1])

    return r


def propagatevalue(d, listpath, valuepath, dname=None, vname=None):
    r = []
    [_vname, v] = dict_path(d, valuepath)
    [_dname, lst] = dict_path(d, listpath)
    vname = _vname if vname is None else vname
    dname = _dname if dname is None else dname
    for f in lst:
        r.append({vname: v, dname: f})

    return r


def addfield(l, p, v):
    r = []
    lst = p.split('.')
    path = lst[:-1]
    entry = lst[-1]
    for f in l:
        c = f.copy()
        cc = c
        for i in path:
            cc = cc[i]
        cc[entry] = v
        r.append(c)

    return r


def listflatten(l):
    r = []
    for f in l:
        r.extend(f)

    return r


class FilterModule(object):

    def filters(self):
        return {
            'extractfromdict': extractfromdict,
            'propagatevalue': propagatevalue,
            'listflatten': listflatten,
            'addfield': addfield,
        }
