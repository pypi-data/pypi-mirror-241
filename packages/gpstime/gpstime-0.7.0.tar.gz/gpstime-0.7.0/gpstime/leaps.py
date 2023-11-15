from functools import lru_cache
import os
import sys
import time
import calendar
import warnings

import appdirs


LEAPFILE_NIST = '/usr/share/zoneinfo/leapseconds'
LEAPFILE_IETF = '/usr/share/zoneinfo/leap-seconds.list'
LEAPFILE_IETF_USER = os.path.join(
    appdirs.user_cache_dir('gpstime'), 'leap-seconds.list')
LEAPFILE_IETF_URL = 'https://www.ietf.org/timezones/data/leap-seconds.list'


def ntp2unix(ts):
    """Convert NTP timestamp to UTC UNIX timestamp

    1900-01-01T00:00:00Z -> 1970-01-01T00:00:00Z

    """
    return int(ts) - 2208988800


def load_NIST(path):
    data = []
    expires = 0
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[:8] == '#expires':
                expires = int(line.split()[1])
            elif line[0] == '#':
                continue
            else:
                year, mon, day, ts, correction = line.split()[1:6]
                st = time.strptime(
                    '{} {} {} {}'.format(year, mon, day, ts),
                    '%Y %b %d %H:%M:%S',
                )
                # FIXME: do something with correction
                data.append(calendar.timegm(st))
    return data, expires


def load_IETF(path):
    data = []
    expires = 0
    first = True
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif line[:2] == '#@':
                expires = ntp2unix(line.split()[1])
            elif line[0] == '#':
                continue
            else:
                # ignore the first entry since that doesn't
                # actually correspond to a leap second
                if first:
                    first = False
                    continue
                leap, offset = line.split()[:2]
                # FIXME: do something with offset
                data.append(ntp2unix(leap))
    return data, expires


def fetch_ietf_leapfile(url=LEAPFILE_IETF_URL, path=LEAPFILE_IETF_USER):
    """Download IETF leap second data to path

    """
    import requests

    dd = os.path.dirname(path)
    if dd != '' and not os.path.exists(dd):
        os.makedirs(dd)
    r = requests.get(url)
    r.raise_for_status()
    tmp = path+'.tmp'
    with open(tmp, 'wb') as f:
        for c in r.iter_content():
            f.write(c)
    data, expires = load_IETF(tmp)

    if len(data) == 0 or expires == 0:
        raise ValueError('Failed to parse downloaded IETF leap seconds file.')
    else:
        if os.path.exists(path):
            os.remove(path)
        os.rename(tmp, path)

    return data, expires


class LeapData:
    """Leap second data.

    """
    _GPS0 = 315964800

    def __init__(self):
        """Initialize leap second data

        """
        self._data = None
        self.expires = 0
        if os.path.exists(LEAPFILE_NIST):
            self._load(load_NIST, LEAPFILE_NIST)
        if not self.valid and os.path.exists(LEAPFILE_IETF):
            self._load(load_IETF, LEAPFILE_IETF)
        if not self.valid and os.path.exists(LEAPFILE_IETF_USER):
            self._load(load_IETF, LEAPFILE_IETF_USER)
        if not self.valid:
            if not self._data:
                print("Leap second data not available.", file=sys.stderr)
            elif self.expired:
                print("Leap second data is expired.", file=sys.stderr)
            print("Updating local user leap data cache from IETF...", file=sys.stderr)
            self._load(fetch_ietf_leapfile, LEAPFILE_IETF_URL)
            if not self._data:
                raise RuntimeError("Failed to load leap second data.")
            elif self.expired:
                warnings.warn("Leap second data is expired.", RuntimeWarning)

    def _load(self, func, path):
        try:
            self._data, self.expires = func(path)
        except Exception as e:
            raise RuntimeError(f"Error loading leap file {path}: {str(e)}")

    @property
    def data(self):
        """Returns leap second data with times represented as UNIX.

        """
        if self.expired:
            warnings.warn("Leap second data is expired.", RuntimeWarning)
        return self._data

    @property
    def expired(self):
        """True if leap second data is expired

        """
        return self.expires <= time.time()

    @property
    def valid(self):
        """True if leap second data is available and not expired

        """
        return self._data and not self.expired

    def __iter__(self):
        for leap in self.data:
            yield leap

    @lru_cache(maxsize=None)
    def as_gps(self):
        """Returns leap second data with times represented as GPS.

        """
        leaps = [(leap - self._GPS0) for leap in self.data if leap >= self._GPS0]
        return [(leap + i) for i, leap in enumerate(leaps)]

    @lru_cache(maxsize=None)
    def as_unix(self, since_gps_epoch=False):
        """Returns leap second data with times represented as UNIX.

        If since_gps_epoch is set to True, only return leap second
        data since the GPS epoch (1980-01-06T00:00:00Z).

        """
        if since_gps_epoch:
            return [leap for leap in self.data if leap >= self._GPS0]
        else:
            return list(self.data)


LEAPDATA = LeapData()


if __name__ == '__main__':
    print("expires: {}".format(LEAPDATA.expires))
    for ls in LEAPDATA:
        print(ls)
