# importing the module
# import imdb
# import imdb as imdb_api
# def get_movie_id(name):
#     ia = imdb_api.IMDb()
#     results = ia.search_movie(name)
#
#     # Check if any of the search results match the exact title
#     movie_exists = False
#     for movie in results:
#         if movie['title'].lower() == name.lower():
#             movie_exists = True
#             # break
#
#     # Print the result
#     if movie_exists:
#        print("The movie exists in IMDb.")
#     else:
#         print("The movie does not exist in IMDb.")
#         return movie_exists
#     #############################################################################################
#     ia = imdb.IMDb()
#     search = ia.search_movie(name)
#     movie_id = 'tt' + search[0].getID()
#
#     return movie_id
#
#
