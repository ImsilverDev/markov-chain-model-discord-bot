import markovify # make sure to do pip install markovify in terminal

def build_model(messages):
    text = '\n'.join(messages)
    model = markovify.Text(text)
    return model

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    channel = message.channel
    content = message.content

    # get all messages in the channel
    messages = []
    async for message in channel.history(limit=500): # you can change the limit here
        messages.append(message.content)

    # build the Markov chain model
    model = build_model(messages)

    # generate a new message
    new_message = model.make_sentence()

    # send the new message to the channel
    if new_message is not None:
        await channel.send(new_message)
