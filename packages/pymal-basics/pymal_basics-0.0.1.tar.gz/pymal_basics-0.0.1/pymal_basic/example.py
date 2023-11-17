from anime import Anime

obj = Anime('YOUR CLIENT ID')

ress = obj.SearchAnime('naruto', 4)
final_ress = obj.GetAnime(ress)

# You can process more data by processing the result
for anime in final_ress:
    print(f"Title: {anime['title']}, ID: {anime['id']}")