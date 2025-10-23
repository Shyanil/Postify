from llm_helper import llm
from few_short import FewShortPosts

few_short = FewShortPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"
    
def generate_post(length , language , tag):
    prompt = get_prompt(length=length , language=language, tag=tag)
    response = llm.invoke(prompt)
    return response.content

def generate_image_ideas(post_text):
    prompt = f'''
    Generate 3 to 4 concise, 
    pointwise image ideas that visually complement 
    the following LinkedIn post content. 
    Focus on relevant, engaging, and professional image concepts suitable 
    for LinkedIn posts.
    Post Content:
    {post_text}
    Image Ideas:
    1.
    2.
    3.
    4.
    Note No need make anything bold
    '''
    response = llm.invoke(prompt)
    return response.content

def get_prompt(length , language , tag):
    length_str = get_length_str(length=length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.
    best emoji for better writing
    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be given {language}
    Note No need make anything bold.
    '''

    examples = few_short.get_filtered_posts(language=language , length=length, tag=tag)
    if len(examples) >= 1:
        prompt += "4) Use the writing style as per the following examples."
        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f'\n\n Example {i+1}: \n\n {post_text}'
            if i == 1:
                break
    return prompt

if __name__ == "__main__":
    print(generate_post("Medium", "Hinglish", "Mental Health"))

