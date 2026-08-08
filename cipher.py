alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter not in alphabets:
            output_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabets)
            output_text += alphabets[shifted_position]
    print(f"here is the {encode_or_decode}d message:\n{output_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt or type 'decode' to decrypt\n").lower()
    text = input("Type your message\n").lower()
    shift = int(input("Type the shift number\n"))
    ceaser(text, shift, direction)

    restart = input("Type 'yes' if you want to continue, otherwise 'no'\n").lower()
    if restart == 'no':
        should_continue = False
        print("See you later")

