"""Make kd-game-1.html (the single-file copy for Claude) from index.html and words.js."""
page = open('index.html', encoding='utf-8').read()
page = page[page.index('<title>'):page.rindex('</body>')]
words = open('words.js', encoding='utf-8').read()
open('kd-game-1.html', 'w', encoding='utf-8').write(
    page.replace('<script src="words.js"></script>', '<script>\n' + words + '</script>'))
