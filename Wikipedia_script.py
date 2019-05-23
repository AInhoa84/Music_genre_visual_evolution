#!/usr/bin/env python
# coding: utf-8



def read_wiki_page(wikipage):
    """ Returns the latest version of the requested Wikipedia page. Input: the name you want to search in Wikipedia """
    url = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles="+wikipage+"&format=json"
    ret=""
    req={}
    
    req["action"]="query"
    req["prop"]="revisions"
    req["rvprop"]="content"
    req["rvsection"]=0
    req["titles"]=wikipage
    req["format"]="json"
    
    
    r=requests.post(url, data=req )
    res = r.text
    res=json.loads(str(res))
    pages = res["query"]["pages"]
    for key, value in pages.items():
        ret=value["revisions"][0]["*"]

    time.sleep(1)    
    return ret



def read_birthplace(page): #If the artist is a person, we need the birth place, if it's a band, their origin
    """Retrieves the birth place or origin of an artist from his Wikipedia page""" 
    if 'birth_place' in page:
        pos_start=page.find('birth_place')
        pos_equal=page.find("=",pos_start)+1
        pos_end=page.find("\n",pos_equal)
        return str(page[pos_equal:pos_end])
    elif 'origin' in page:
        pos_start=page.find('origin')
        pos_equal=page.find("[[",pos_start)
        pos_end=page.find("\n",pos_equal)
        return str(page[pos_equal:pos_end])

def extract_genre(page):
    """Retrieves the music genre for an artist from his Wikipedia page"""
    pos_start=page.find('genre')
    pos_equal=page.find("[[",pos_start)+2 #We extract the main genre for each artist
    pos_end=page.find("]]",pos_equal)
    
    return str(page[pos_equal:pos_end])



def retrieve_metadata(a, b):
    """For any files containing the artist name in a column called "name_formatted", reads the file, retrieves the artists origin and music genre, and saves a new file with the data"""

    for j in range(a, b):
        print('Starting with chunk {}: '.format(j))
        df = pd.read_csv('Chunks/chunk{}.csv'.format(j), sep='\t')
        df['name_formatted'] = df['name_formatted'].str.strip()
        df['birth_place'] = np.nan
        df['genre'] = np.nan 
        for i in tqdm.tqdm(range(len(df))):
            artist = str(df['name_formatted'][i])
            list_ = get_1_artist(artist)
            df['birth_place'][i] = list_[1]
            df['genre'][i] = list_[2]
        df.to_csv('Chunks_completed/chunk{}.csv'.format(j), sep='\t', index=False, encoding='utf-8')



def reverse(name):
    """If a name is in the format: "Family name, First name", reverses the order and returns "First name Family name" without the comma"""
    
    if ',' in name:
        b = name.split(',')
        rev = b[-1::-1]
        out = ' '.join(rev)
        return out
    
    else:
        return name

def get_1_artist(artist):
    """Retrieves origin and music genre for a single artist"""
    try:
        page = read_wiki_page(artist)
        birth_place= read_birthplace(page)
        genre = extract_genre(page)
    except:
        birth_place = np.nan
        genre = np.nan
    return [artist, birth_place, genre]


def concat_chunks(a, b):
    """For any number of chunks in the folder "Chunks_completed": concatenates all of them and exports them to a single csv file"""
    
    main_df = pd.read_csv('Chunks_completed/chunk{}.csv'.format(a), sep='\t', header=0, encoding='utf-8')
    
    for j in tqdm.tqdm(range(a+1, b)):
        df = pd.read_csv('Chunks_completed/chunk{}.csv'.format(j), sep='\t', header=0, encoding='utf-8')
        df1 = pd.concat([main_df, df], ignore_index=True)
        main_df = df1
        
    main_df.to_csv('Wikipedia_chunks_all.csv', sep='\t', index=False, encoding='utf-8')




