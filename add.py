# import requests
# import imdb_id
# import data_ip
# import imdb as imdb_api
# def add_movie(movie_name):
#     CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
#     KEY = 'd1a7c199362fdf0bc5aa9aa09ecb4e6c'
#
#     url = CONFIG_PATTERN.format(key=KEY)
#     r = requests.get(url)
#     config = r.json()
#
#     base_url = config['images']['base_url']
#     sizes = config['images']['poster_sizes']
#     """
#         'sizes' should be sorted in ascending order, so
#             max_size = sizes[-1]
#         should get the largest size as well.
#     """
#     def size_str_to_int(x):
#         return float("inf") if x == 'original' else int(x[1:])
#     max_size = max(sizes, key=size_str_to_int)
#
#     #movie_name = input("Enter A Movie : ")
#     movie_ID = imdb_id.get_movie_id(movie_name)
#     if (movie_ID== False):
#         return 0
#     IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
#     r = requests.get(IMG_PATTERN.format(key=KEY,imdbid=movie_ID))
#     api_response = r.json()
#     # if (api_response['success']== False):
#     #     #print("the name of the movie does not exit")
#     #     return 0
# #############################3333
#     # ia = imdb_api.IMDb()
#     # results = ia.search_movie(movie_name)
#     #
#     # # Check if any of the search results match the exact title
#     # movie_exists = False
#     # for movie in results:
#     #     if movie['title'].lower() == movie_name.lower():
#     #         movie_exists = True
#     #         # break
#     #
#     # # Print the result
#     # if movie_exists:
#     #     print("The movie exists in IMDb.")
#     # else:
#     #     print("The movie does not exist in IMDb.")
#     #     return movie_exists
# #################################################3333333
#     posters = api_response['posters']
#     poster_urls = []
#     for poster in posters:
#         rel_path = poster['file_path']
#         url = "{0}{1}{2}".format(base_url, max_size, rel_path)
#         poster_urls.append(url)
#
#     for nr, url in enumerate(poster_urls):
#         if nr == 1:
#             break
#         r = requests.get(url)
#         filetype = r.headers['content-type'].split('/')[-1]
#         filename = movie_name+'_{0}.{1}'.format(nr+1,filetype)
#         with open(filename,'wb') as w:
#             w.write(r.content)
#     print(url)
#
#     data_ip.add_data(movie_name,filename,movie_ID,url)
#     return 1