import random
import requests
import credentails
import random




f_word = input("Please type an word that begins with the letter f: ")
word = f_word

ryhme_word = []

while True:

    api_url = 'https://api.api-ninjas.com/v1/rhyme?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': credentails.api_key})
    if response.status_code == requests.codes.ok:
        ryhme_word = response.text
        ryhme_word = ryhme_word.split(",")
        ryhme_word_clean = random.choice(ryhme_word)
        ryhme_word_final = ryhme_word_clean.replace('"', '')
        ryhme_word_final_1 = ryhme_word_final.replace(" ", "")
        print(ryhme_word_final_1)
    else:
        print("Error:", response.status_code, response.text)



    word = "elegant"
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)
    response = requests.get(api_url, headers={'X-Api-Key': credentails.api_key})
    if response.status_code == requests.codes.ok:
        syn_word = response.text
        syn_word = syn_word.split(",")
        print(syn_word)
        print(len(syn_word))

        syn_word_clean = random.choice(syn_word)
        syn_word_final = syn_word_clean.replace('"', '')
        syn_word_final_1 = syn_word_final.replace(" ", "")
        print(syn_word_final_1)
    else:
        print("Error:", response.status_code, response.text)

    if syn_word_final_1 != "[]":
        break







# pronouns = ["We", "I", "They", "He", "She", "Jack", "Jim"]
# verbs = ["was", "is", "isn't", "wasn't"]
# actions = ["playing a game", "watching television", "talking", "dancing", "speaking"]
# a = (random.choice(pronouns))
# b = (random.choice(actions))
# c = (random.choice(nouns))

# print("" + a + " " + b + " " + c + " " + syn_word + " , like a " + ryhme_word + ". Weezy f baby and the f is for " + f_word)
