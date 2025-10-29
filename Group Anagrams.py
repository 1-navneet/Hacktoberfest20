from collections import defaultdict

def groupAnagrams(strs):
    mp = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        mp[key].append(s)

    return list(mp.values())
