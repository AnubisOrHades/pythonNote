def get_password(password):
    # B = list(bin(password)[2:])
    B = [int(i) for i in bin(password)[2:]]
    G = []
    for i in range(len(B)):
        if i == 0:
            G.append(B[i])
        else:
            G.append(B[i] ^ B[i - 1])
    # print(B)
    # print(G)
    G = [str(i) for i in G]
    # print("".join(G))
    # print(int("".join(G), 2))
    return int("".join(G), 2)


if __name__ == '__main__':
    password = 921224
