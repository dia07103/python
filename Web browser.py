import webbrowser
keyword=input('What do you want to search?\n')

keyword1=keyword.replace(' ','+')
keyword2=keyword.replace(' ','%20')

websites='https://www.google.com/search?ei=j5ooXKr6HYqdsAfC2bngBQ&q=' + keyword1

videos='https://www.youtube.com/results?search_query=' + keyword1

news='https://www.google.com/search?q=' + keyword1

blogs='https://en.search.wordpress.com/?src=organic&q=' + keyword1

viralnews='https://www.google.ae/search?ei=0JwoXMTgKdC1sAeB8ISwDQ&q=' + keyword1 + ' viral' + ' news'

stockimages='https://www.pexels.com/search/' + keyword2

webbrowser.open(websites)
webbrowser.open(videos)
webbrowser.open(news)
webbrowser.open(blogs)
webbrowser.open(viralnews)
webbrowser.open(stockimages)

