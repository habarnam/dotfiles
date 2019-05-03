# pylint: disable=C0111
from qutebrowser.config.configfiles import ConfigAPI  # noqa: F401
from qutebrowser.config.config import ConfigContainer  # noqa: F401
config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103
config.set('colors.tabs.bar.bg', '#111111')
config.set('colors.tabs.even.bg', '#666666')
config.set('colors.tabs.even.fg', 'white')
config.set('colors.tabs.odd.bg', '#666666')
config.set('colors.tabs.odd.fg', 'white')
config.set('colors.tabs.selected.even.bg', '#004477')
config.set('colors.tabs.selected.even.fg', '#ffffff')
config.set('colors.tabs.selected.odd.bg', '#004477')
config.set('colors.tabs.selected.odd.fg', '#ffffff')
config.set('colors.webpage.bg', '#cccccc')
config.set('completion.use_best_match', False)
config.set('content.default_encoding', 'utf-8')
config.set('content.windowed_fullscreen', False)
config.set('downloads.location.directory', '~/Downloads')
config.set('downloads.location.prompt', True)
config.set('editor.command', ['nvim-qt', '{file}', '+{line}'])
config.set('fonts.completion.category', 'bold 12pt monospace')
config.set('fonts.completion.entry', '12pt monospace')
config.set('fonts.debug_console', '12pt monospace')
config.set('fonts.downloads', '10pt monospace')
config.set('fonts.hints', 'bold 12pt monospace')
config.set('fonts.keyhint', '12pt monospace')
config.set('fonts.messages.error', '12pt monospace')
config.set('fonts.messages.info', '10pt monospace')
config.set('fonts.messages.warning', '10pt monospace')
config.set('fonts.prompts', '10pt sans-serif')
config.set('fonts.statusbar', '12pt monospace')
config.set('fonts.tabs', '12pt monospace')
config.set('fonts.web.family.standard', 'sans')
config.set('fonts.web.size.default', 18)
config.set('fonts.web.size.default_fixed', 16)
config.set('fonts.web.size.minimum', 12)
config.set('hints.mode', 'number')
config.set('input.insert_mode.auto_leave', True)
config.set('input.insert_mode.auto_load', True)
config.set('tabs.indicator.padding', {
    'bottom': 2,
    'left': 0,
    'right': 4,
    'top': 2
})
config.set('tabs.indicator.width', 5)
config.set('tabs.padding', {'bottom': 4, 'left': 5, 'right': 5, 'top': 3})
config.set('tabs.title.format', '{index}{title_sep}{current_title}')
config.set('tabs.title.format_pinned', ' {index}')
config.set('tabs.width', '20%')
config.set('content.register_protocol_handler', False)
config.set('url.searchengines', {
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'g': 'https://www.google.de/search?q={}',
    'ws': 'https://en.wikipedia.org/w/index.php?search={}',
    'wk': 'https://en.wiktionary.org/w/index.php?search={}',
    'tfd': 'http://tfd.com/{}',
    'cc': 'https://www.dict.cc/?s={}',
    'im': 'https://www.imdb.com/find?q={}&s=all'
})
config.set('tabs.background', True)
config.bind('t', 'set-cmd-text -s :open -t ')
config.bind('T', 'set-cmd-text -s :open -t {url}')
config.bind('O', 'set-cmd-text -s :open {url}')
config.bind('gt', 'tab-next')
config.bind('gT', 'tab-prev')
config.bind(',v', 'spawn mpv {url}')
config.bind(';v', 'hint links spawn mpv {hint-url}')
config.bind('<Ctrl-o>', 'back')
config.bind('<Ctrl-i>', 'forward')
config.unbind('H')
config.unbind('J')
config.unbind('K')
config.unbind('L')

config.bind('<y><y>', 'yank selection')
config.bind('<z><l>', 'spawn --userscript password_fill')
config.set('window.hide_decoration', True)
config.source('nord-qutebrowser.py')
