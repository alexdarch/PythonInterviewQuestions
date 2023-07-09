import pandas as pd
from typing import List, Iterator

def rechunk_dataframes(dataframes: List[pd.DataFrame], fixed_size: int) -> Iterator[pd.DataFrame]:
    curr_chunk = []
    for df in dataframes:
        while True:
            curr_len = sum(len(d) for d in curr_chunk)
            buffer = fixed_size - curr_len

            curr_chunk.append(df[:buffer])
            df = df[buffer:]

            # if we used up all of the df, then move on to the next
            if len(df) == 0:
                break

            # If there is something left in the df then we have hit the fixed_size
            # And therefore we yield the curr_chunk, reset the curr_chunk and continue
            if len(df) > 0:
                yield pd.concat(curr_chunk, ignore_index=True)
                curr_chunk = []
                # Move to next df or, if too large to fit into the current chunk continue exhausting this df
                if len(df) < fixed_size:
                    curr_chunk.append(df)
                    break
    remainder = pd.concat(curr_chunk, ignore_index=True)
    if not remainder.empty:
        yield remainder
