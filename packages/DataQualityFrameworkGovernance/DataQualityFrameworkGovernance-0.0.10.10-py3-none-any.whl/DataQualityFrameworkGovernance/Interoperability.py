def data_migration_reconciliation(source_df, target_df):
    import pandas as pd
    # Check if the columns in both dataframes match
    #Heading Recon
    if set(source_df.columns) != set(target_df.columns):
        #print("Columns in source and target dataframes do not match.")

        # Create a dataframe with consolidated column names
        source_columns = set(source_df.columns)
        target_columns = set(target_df.columns)
        
        consolidated_columns = pd.DataFrame(list(source_columns.union(target_columns)), columns=['Column'])

        # Add columns to indicate matched and unmatched status
        consolidated_columns['MatchStatus'] = 'Unmatched'
        consolidated_columns['TableLocation'] = 'NotApplicable'

        # Mark columns from source / target table. Matched & NotApplicable
        consolidated_columns.loc[consolidated_columns['Column'].isin(source_columns), 'TableLocation'] = 'Source'
        consolidated_columns.loc[consolidated_columns['Column'].isin(target_columns), 'TableLocation'] = 'Target'
        matched_mask = consolidated_columns['Column'].isin(source_columns & target_columns)
        consolidated_columns.loc[matched_mask, 'MatchStatus'] = 'Matched'
        consolidated_columns.loc[matched_mask, 'TableLocation'] = 'NotApplicable'

        # Sort by MatchStatus and then by Column
        consolidated_columns.sort_values(by=['MatchStatus', 'Column'], ascending=[False, True], inplace=True)

        return consolidated_columns

    #Row level Recon
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

def data_consolidation(dataset1, dataset2, compile):
    import pandas as pd
    if compile == 1:
        _compile = 1
    else:
        _compile = 0
    
    concatenated_df = pd.concat([dataset1, dataset2], axis=_compile)
    return concatenated_df

def data_integration_reconciliation(source_df, target_df, key_columns):
    import pandas as pd
    # Check if the columns in both dataframes match
    #Heading Recon
    if set(source_df.columns) != set(target_df.columns):
        #print("Columns in source and target dataframes do not match.")

        # Create a dataframe with consolidated column names
        source_columns = set(source_df.columns)
        target_columns = set(target_df.columns)
        
        consolidated_columns = pd.DataFrame(list(source_columns.union(target_columns)), columns=['Column'])

        # Add columns to indicate matched and unmatched status
        consolidated_columns['MatchStatus'] = 'Unmatched'
        consolidated_columns['TableLocation'] = 'NotApplicable'

        # Mark columns from source / target table. Matched & NotApplicable
        consolidated_columns.loc[consolidated_columns['Column'].isin(source_columns), 'TableLocation'] = 'Source'
        consolidated_columns.loc[consolidated_columns['Column'].isin(target_columns), 'TableLocation'] = 'Target'
        matched_mask = consolidated_columns['Column'].isin(source_columns & target_columns)
        consolidated_columns.loc[matched_mask, 'MatchStatus'] = 'Matched'
        consolidated_columns.loc[matched_mask, 'TableLocation'] = 'NotApplicable'

        # Sort by MatchStatus and then by Column
        consolidated_columns.sort_values(by=['MatchStatus', 'Column'], ascending=[False, True], inplace=True)

        return consolidated_columns
    
    # else continue here,  merge source and target data on key columns
    merged_data = pd.merge(source_df, target_df, on=key_columns, how='outer', suffixes=('_source', '_target'), indicator=True)

    # Identify matching and mismatched values
    comparison_results = pd.DataFrame()
    comparison_results[key_columns] = merged_data[key_columns]

    # Add column indicating match or mismatch
    comparison_results['Status'] = 'Match'
    comparison_results['Mismatched_Columns'] = None  # initialize as None

    for column in source_df.columns:
        if column not in key_columns:
            source_column = f'{column}_source'
            target_column = f'{column}_target'

            # Check if the column is present in both dataframes
            if source_column in merged_data.columns and target_column in merged_data.columns:
                mismatched_mask = merged_data[source_column] != merged_data[target_column]
                comparison_results.loc[mismatched_mask, 'Status'] = 'Mismatch'

                # Add mismatched column names to 'Mismatched_Columns'
                comparison_results.loc[mismatched_mask, 'Mismatched_Columns'] = \
                    comparison_results['Mismatched_Columns'].apply(lambda x: [column] if x is None else x + [column])

                comparison_results[f'{column}_source'] = merged_data[source_column]
                comparison_results[f'{column}_target'] = merged_data[target_column]

    # Convert lists to comma-separated strings
    comparison_results['Mismatched_Columns'] = comparison_results['Mismatched_Columns'].apply(lambda x: ', '.join(x) if x is not None else None)
    # sort by key columns, then by 'Status' with 'Mismatch' first
    comparison_results.sort_values(by=['Status'] + [key_columns], ascending=[False, True], inplace=True)

    return comparison_results
    