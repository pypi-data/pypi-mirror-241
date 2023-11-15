def data_migration_reconciliation(source_df, target_df):
    import pandas as pd
    # Check if the columns in both dataframes match
    if set(source_df.columns) != set(target_df.columns):
        print("Columns in source and target dataframes do not match.")
        return

    # empty dataframe
    reconciliation_results = pd.DataFrame(columns=['Column', 'Row no. / Position', 'Source Data', 'Target Data'])

    # Compare the data in each column
    for column in source_df.columns:
        # Check if the data in the column matches
        mask = source_df[column] != target_df[column]
        if mask.any():
            # Add the mismatched records to the reconciliation_results dataframe
            mismatch_data = pd.DataFrame({
                'Column': [column] * mask.sum(),
                'Row no. / Position': source_df.loc[mask].index + 1,
                'Source Data': source_df.loc[mask, column].tolist(),
                'Target Data': target_df.loc[mask, column].tolist()
            })
            reconciliation_results = pd.concat([reconciliation_results, mismatch_data], ignore_index=True)

    return reconciliation_results

