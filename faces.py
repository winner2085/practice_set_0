def main():
    emoji = input("Type something with a smile or with a frown: ").replace(":)","🙂").replace(":(","🙁")
    convert(emoji)
    
def convert(emoticon):
    print(f"{emoticon}")



main()