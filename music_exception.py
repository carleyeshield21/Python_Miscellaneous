

# chosen_date = input('Choose a date in this format: YYYY-MM-DD\n')
# billboard_url = 'https://www.billboard.com/charts/hot-100/' + chosen_date
# billboard_url = 'https://www.billboard.com/charts/hot-100/1981-075-05'

def music_time_machine():
    import requests
    from bs4 import BeautifulSoup
    chosen_date = input('Choose a date in this format: YYYY-MM-DD\n')
    print(len(chosen_date))

    if chosen_date[4] and chosen_date[7] == '-':
        billboard_url = 'https://www.billboard.com/charts/hot-100/' + chosen_date
        response_text = requests.get(billboard_url).text
        response_soup = BeautifulSoup(response_text,
                                      'html.parser')
        peak = response_soup.select('li ul li span',
                                    class_=['o-chart-results-list__item'])
        list = [pos.get_text().strip() for pos in peak]
        wks_on_chart = []
        n = 3
        for num in range(n,103):
            wks_on_chart.append(int(list[n]))
            n += 7

        peak_pos = []
        m = 2
        for num in range(m,
                         102):
            peak_pos.append(int(list[m]))
            m += 7

        # ===============================================================
        song_title = response_soup.find_all(name='h3',
                                            class_='a-no-trucate')
        song_list = [song.getText().strip() for song in song_title]

        song_artist = response_soup.find_all(name='span',
                                             class_='a-no-trucate')
        artists_names = [artist.get_text().strip() for artist in song_artist]

        # student_scores = {student:random.randint(1,100) for student in names}
        for n in range(0,100):
            # print(f'{n+1}. {song_list[n]} -- {artists_names[n]}\n')
            print(f'{n + 1}. {song_list[n]} -- {artists_names[n]}\n      Spent'
                  f' {wks_on_chart[n]} week/s on the Billboard 100\n      Reached '
                  f'number '
                  f'{peak_pos[n]} as its highest position')
        # print(billboard_url)
    else:
        print('Please check the date and format and try again')

# music_time_machine()

try:
    music_time_machine()
except IndexError:
    print('Please check the date and format and try again')
    music_time_machine()