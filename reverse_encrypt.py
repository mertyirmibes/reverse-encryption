def reverse(word):
    return word[::-1]
while True:
    sentence = input("Enter word (type 'stop' to exit): ")
    if sentence.lower() == 'stop':  # 'dur' yazıldığında döngüden çıkılır
        print("End.")
        break
    print(reverse(sentence))