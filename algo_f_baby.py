
import random
import requests
import credentails



f_word = input("Please type an word that begins with the letter f: ")
word = f_word

ryhme_word = []


api_url = 'https://api.api-ninjas.com/v1/rhyme?word={}'.format(word)
response = requests.get(api_url, headers={'X-Api-Key': credentails.api_key})
if response.status_code == requests.codes.ok:
    ryhme_word = response.text
    ryhme_word = ryhme_word.split(",")
    ryhme_word_clean = random.choice(ryhme_word)
    ryhme_word_final = ryhme_word_clean.replace('"', '')
    ryhme_word_final_01 = ryhme_word_final.replace(" ", "")
    ryhme_word_final_001 = ryhme_word_final_01.replace("]", "")
    ryhme_word_final_1 = ryhme_word_final_001.replace("[", "")
    print(ryhme_word_final_1)
else:
    print("Error:", response.status_code, response.text)


syn_word = []

word = ryhme_word_final_1
api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
response = requests.get(api_url, headers={'X-Api-Key': credentails.api_key})
if response.status_code == requests.codes.ok:
    processed = eval(response.text)
    syn_word = processed["antonyms"]
    print(syn_word)
    if len(syn_word) <= 0:
        syn_word = [ryhme_word_final_1]
    syn_word_clean = random.choice(syn_word)
    syn_word_final = syn_word_clean.replace('"', '')
    syn_word_final_1 = syn_word_final.replace(" ", "")
    print(syn_word_final_1)

else:
    print("Error:", response.status_code, response.text)
    syn_word_final_1 = ryhme_word_final_1


pronouns = ["We", "I", "They", "He", "She", "Jack", "Jim", "You", "Robert", "Matt", "Doctor Smith", "Fred", ]
verbs = ["was", "is", "isn't", "wasn't", "has been", ]
actions = ["playing a game", "watching television", "talking", "dancing", "speaking", "reading", "walking", "eating", "striking", "jumping", "trying", "blooming", "rapping", "demanding", "smoking"]
a = (random.choice(pronouns))
b = (random.choice(actions))
c = (random.choice(verbs))

generated_rap = ("" + a + " " + b + " " + c + " " + syn_word_final_1 + ", like a " + ryhme_word_final_1 + ". Weezy f baby and the f is for " + f_word)

print(generated_rap)
