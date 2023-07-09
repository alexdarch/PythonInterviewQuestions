import pandas as pd
from typing import List, Iterator

def convert_to_fixed_size(dataframes: List[pd.DataFrame], fixed_size: int) -> Iterator[pd.DataFrame]:
    current_dfs = []
    for df in dataframes:
        curr_df = df.copy()
        while True:
            curr_len = sum(len(d) for d in current_dfs)
            buffer = fixed_size - curr_len

            current_dfs.append(curr_df[:buffer])
            curr_df = curr_df[buffer:]

            # if we used up all of the curr_df, then move on to the next
            if len(curr_df) == 0:
                break

            # If there is something left in the curr_df then we have hit the fixed_size
            # And therefore we yield the current_dfs, reset the current_dfs and continue
            if len(curr_df) > 0:
                yield pd.concat(current_dfs, ignore_index=True)
                current_dfs = []
                # If we are left with less than fixed then add to current and move to the next df, otherwise continue exhausting this df
                if len(curr_df) < fixed_size:
                    current_dfs = [curr_df]
                    break
    remainder = pd.concat(current_dfs, ignore_index=True)
    if not remainder.empty:
        yield remainder
