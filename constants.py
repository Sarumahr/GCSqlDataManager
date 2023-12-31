GC_CONDITION_ROWS = ('id', 'cond_code', 'cond_text')
GC_CONDITION_TABLE = "GC_CONDITION"
EXAMPLE_CONDITION = (999, 'ex', 'example condition')
GC_PUBLISHER_ROWS = ('id', 'name', 'date')
GC_PUBLISHER_TABLE = "GC_PUBLISHER"
EXAMPLE_PUBLISHER = (999, "example publisher", "12.12.1212")
GC_LANGUAGE_ROWS = ('id', 'lang_code', 'lang_text')
GC_LANGUAGE_TABLE = "GC_LANGUAGE"
EXAMPLE_LANGUAGE = (999, 'ex', 'example')
GC_CONSOLE_ROWS = ('id', 'upc', 'name', 'area', 'publisher', 'release_date', 'image', 'cond_pack', 'cond_book', 'cond_console', 'price', 'price_history')
GC_CONSOLE_TABLE = "GC_CONSOLE"
EXAMPLE_CONSOLE = (999, "9013274632353", "example console", "example", 999, "12.12.1212", "example", 999, 999, 999, "299,99€", 999)
GC_GAME_ROWS = ('id', 'upc', 'name', 'edition', 'lang', 'area', 'publisher', 'release_date', 'image', 'usk', 'console', 'players', 'storage', 'cond_shell', 'cond_book', 'cond_disk', 'price', 'price_history')
GC_GAME_TABLE = "GC_GAME"
EXAMPLE_GAME = (999, "9017384562983", "example", "example", 999, "example", 999, "12.12.1212", "example", "16", 999, "2", "2GB", 999, 999, 999, "19,99€", 999)
GC_PRICE_HISTORY_ROWS = ('id', 'date', 'game', 'shop', 'price')
GC_PRICE_HISTORY_TABLE = "GC_PRICE_HISTORY"
EXAMPLE_PRICE_HISTORY = (999, "12.12.1212", 999, "ebay", "12,99€")

CONFIG_PATH = "opt/conf/config.json"
