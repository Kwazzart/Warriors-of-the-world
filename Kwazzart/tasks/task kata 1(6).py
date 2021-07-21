def decode_bits(bin_str):
    answ = 0
    if bin_str != "":
        for indx, i in enumerate(bin_str):

            if i == "1":
                if indx % 2 == 0:
                    answ -= 1
                else:
                    answ += 1
    print(answ)

decode_bits("1")
