from util import hook
from datetime import datetime, timedelta
import re

cache = []
cached_filename = ''

@hook.command('1')
@hook.command
def oneyearago(inp, chan=None, say=None):
  xyearsago(1, chan, say)

@hook.command('2')
@hook.command
def twoyearsago(inp, chan=None, say=None):
  xyearsago(2, chan, say)

@hook.command('12')
@hook.command
def onetwo(inp, chan=None, say=None):
  say('--- one year ago ---')
  xyearsago(1, chan, say)
  say('--- two years ago ---')
  xyearsago(2, chan, say)

def xyearsago(x, chan, say):
  global cache, cached_filename
  dt = datetime.now()
  try:
    ndt = dt.replace(year=dt.year - x)
  except:
    # only happens on feb 29th i guess
    ndt = dt.replace(year=dt.year - x, month=3, day=1)
  # filename format: #sa-minecraft.09-13.log
  # chan = '#sa-minecraft'
  filename = 'persist/log/{}/irc.synirc.net/{}.{}-{}.log'.format(
      ndt.year, chan, str(ndt.month).rjust(2, '0'), str(ndt.day).rjust(2, '0'))
  if cached_filename == filename:
    hours = cache
  else:
    try:
      f = open(filename, 'r')
      cached_filename = filename
    except IOError, e:
      say('no logs for this channel/user mate')
      return
    hours = [
        (line, datetime.strptime(line[:8], '%H:%M:%S').replace(year=ndt.year, month=ndt.month, day=ndt.day))
        for line in f if not line[9:].startswith('-!-')]
    f.close()
    cache = hours
  line = min(hours, key=lambda x: abs(ndt - x[1]))
  idx = hours.index(line)
  for i in range(idx, idx+4):
    if i >= 0 and i < len(hours):
      say(hours[i][0].decode('utf-8'))
