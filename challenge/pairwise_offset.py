def pairwise_offset(sequence: list, fillvalue="*", offset=0):
    sequence = list(sequence)
    offset_sequence = sequence[:]
    for _ in range(offset):
        sequence.append(fillvalue)
        offset_sequence.insert(0, fillvalue)

    return list(zip(sequence, offset_sequence))


print(pairwise_offset([1, 2, 3, 4], offset=2))
