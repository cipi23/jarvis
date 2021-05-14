import webbrowser as wb


def web(recorded_audio):

    keyword = recorded_audio.split(' ')[1]
    url = "https://google.com/search?q=" + keyword

    wb.open(url)



#web('show cat')