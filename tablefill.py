import serpapi

params = {
    "google_domain": "google.com",
    "api_key": "3ecaca48981e5c573bdd0a7e7302aa35cb5e418860521c6c7438a954e1ea3178"
}


def get_answer_box(q):
    p = {'q': q, **params}
    result = serpapi.GoogleSearch(p)
    result = result.get_dict()
    print(result)
    if 'answer_box' in result.keys():
        if 'list' in result['answer_box'].keys():
            return ', '.join(result['answer_box']['list']), result['answer_box']['link']
        if 'snippet' in result['answer_box'].keys():
            return result['answer_box']['snippet'], result['answer_box']['link']
    if 'answer_box_list' in result.keys():
        if 'list' in result['answer_box_list'][0].keys():
            return ', '.join(result['answer_box_list'][0]['list']), result['answer_box_list'][0]['link']
    return '', ''


def search_whole_table(df):
    urls = []
    for i in df.index:
        for c in df.columns:
            print(f'{i} {c}')
            result, url = get_answer_box(f'{i} {c}')
            urls += [url]
            print(result)
            df.at[i, c] = result
    return df, urls
