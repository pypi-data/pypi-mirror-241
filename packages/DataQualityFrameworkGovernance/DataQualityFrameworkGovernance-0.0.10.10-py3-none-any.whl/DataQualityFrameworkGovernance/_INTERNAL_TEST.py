import pandas as pd

import Interoperability as io

source_dataset = pd.DataFrame({
	'Ordinal': [54, 55, 56, 57],
	'Name': ['Theresa May','Boris Johnson', 'Liz Truss', 'Rishi Sunak'],
	'Monarch': ['Elizabeth II', 'Elizabeth II', 'Elizabeth II & Charles III', 'Charles III']
	})

target_dataset = pd.DataFrame({
	'Ordinal': [55, 56, 57],
	'Name': ['Boris Johnson', 'Liz Truss', 'Rishi Sunak'],
	'Monarch': ['Elizabeth II', 'Elizabeth II', 'Charles III']
	})

comparison_results = io.data_integration_reconciliation(source_dataset, target_dataset, 'Ordinal')
print(comparison_results)