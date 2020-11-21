from pushshift_py import PushshiftAPI
api = PushshiftAPI()


def estimate_location(reddit_username, **kwargs):
    q_gta = "Toronto|askTO|Brampton|GTA|Missisauga|Durham|Ontario|Niagara|Oakville"
    q_elsewhere = "Montreal|Calgary|Ottawa|Edmonton|Winnipeg|Vancouver|Quebec|Halifax"

    gen_gta = api.search_comments(q=q_gta, author=reddit_username, limit=kwargs.get('postUpperLim'))
    gen_elsewhere = api.search_comments(q=q_elsewhere, author=reddit_username)

    return("GTA posts: " + str(len(list(gen_gta))) + ", Elsewhere posts: " + str(len(list(gen_elsewhere))))