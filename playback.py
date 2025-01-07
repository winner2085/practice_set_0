def main():
    sentence = input("Write a sentence: ").replace(" ", "...")
    slow_down(sentence)

def slow_down(your_sentence):    
    print(f"Slow down! {your_sentence}")

main()