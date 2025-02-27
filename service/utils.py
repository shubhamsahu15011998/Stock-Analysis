def yield_chunks(li, chunk_size):
    for idx in range(0, len(li), chunk_size):
        yield li[idx:idx+chunk_size]
