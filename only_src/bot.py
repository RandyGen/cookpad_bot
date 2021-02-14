import twitter
import markovify
import settings

api = twitter.Api(consumer_key=settings.CONSUMER_KEY,
                  consumer_secret=settings.CONSUMER_SECRET,
                  access_token_key=settings.ACCESS_TOKEN_KEY,
                  access_token_secret=settings.ACCESS_TOKEN_SECRET
                  )

all_parsed_text = ''

with open("parsed_data.txt", "r", encoding='UTF-8', errors='ignore') as f:
    parsed_texts = f
    for parsed_text in parsed_texts:
        all_parsed_text = all_parsed_text + parsed_text

print('All Texted')

e = 0

while True:
    try:
        # Build model
        sentence = ''
        text_model = markovify.NewlineText(all_parsed_text, state_size=2)
        # Output
        for i in range(4):
            sentence += str(i + 1) + ". " + str(text_model.make_short_sentence(30, tries=100)).strip() + "\n"
            # print(sentence)
        api.PostUpdate(sentence)

    except Exception as e:
        print(e)
        break
    except twitter.error.TwitterError:
        e += 1
        print("Now making...(" + str(e) + ")")
        continue
    break

print('Finish!!!')
