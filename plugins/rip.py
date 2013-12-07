from util import hook, strip_formatting
from textwrap import wrap

WIDTH = 40

@hook.command(multiline=True)
def rip(inp, say=None):
  if inp == '': return

  if '\n' in inp:
    txt = inp.split('\n')
    width = len(max(txt, key=lambda x: len(x)))
  else:
    stripped = strip_formatting.strip(inp)
    inp = inp.strip()
    og = inp
    width = WIDTH + 4

    if len(stripped) > WIDTH:
      txt = wrap(inp, WIDTH)
    else:
      width = len(stripped) + 4
      txt = [inp]

  topfiller = str.center('', width-5, '-')

  headstone = []
  headstone.append('  _.' + topfiller + '-._')
  headstone.append(' |' + str.center('RIP', width) + '|')
  for line in txt:
    headstone.append(' |' + str.center(line.upper().encode('utf-8'), width) + '|')
  headstone.append(' |' + str.center('', width, '_') + '|')
  headstone.append('|' + str.center('', width+2, '_') + '|')

  for l in headstone:
    say(l.decode('utf-8'))

@hook.command
def bread(inp, say=None):
  inp = inp.strip()
  og = inp
  inp = inp.encode('utf-8')
  topfiller = str.center('', len(strip_formatting.strip(og))-1, '-')

  top = '  .' + topfiller + '-.\n'

  width = len(top)-3

  rip = ' |' + str.center('', width) + '|\n'
  nmr = ' |' + str.center(inp.upper(), width) + '|\n'
  lsr = ' |' + str.center('', width, '_') + '|\n'

  headstone = [top, rip, nmr, lsr]
  for l in headstone:
    say(l.decode('utf-8'))
