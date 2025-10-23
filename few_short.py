import json
import pandas as pd

class FewShortPosts:
    def __init__(self , file_path = 'data/preprocess_post.json'):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)
    
    def load_posts(self, file_path):
        with open(file_path , encoding='utf-8') as f:
            posts = json.load(f)
            self.df = pd.json_normalize(posts)
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            all_tags = self.df['tags'].apply(lambda x : x).sum()
            self.unique_tags = set(list(all_tags))
    
    def categorize_length(self , line_count):
        if line_count < 5:
            return 'Short'
        elif 5 <= line_count <= 20:
            return 'Medium'
        else:
            return 'Long'
    
    def get_filtered_posts(self , language , length , tag):
        df_filtered = self.df[
            (self.df['language'] == language) &
            (self.df['length'] == length) &
            (self.df['tags'].apply(lambda tags : tag in tags))
        ]
        return df_filtered.to_dict(orient = 'records')
    
    def get_tags(self):
        return self.unique_tags

if __name__ == '__main__':
    fs = FewShortPosts()
    posts = fs.get_filtered_posts(language='English' , length='Short' , tag='Job Search')
    print(posts)