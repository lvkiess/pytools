import pandas as pd


def count_result(df, input_filename):
    result_list = []

    if '测试结果' in df.columns:
        value_counts = df['测试结果'].value_counts()
        total_count = len(df['测试结果'])
        percentages = value_counts / total_count * 100

        # Ensure all lists are the same length by padding with None or pd.NA
        max_length = max(len(value_counts.index), len(value_counts.values), len(percentages.values))
        result_indices = value_counts.index.tolist() + [None] * (max_length - len(value_counts.index))
        result_counts = value_counts.values.tolist() + [None] * (max_length - len(value_counts.values))
        result_percentages = percentages.values.tolist() + [None] * (max_length - len(percentages.values))

        result_list.append(pd.DataFrame({
            '测试用例': [input_filename] * max_length,
            '结果': result_indices,
            '出现次数': result_counts,
            '占比率': result_percentages
        }))
    else:
        result_list.append(pd.DataFrame({
            '测试用例': [input_filename],
            '结果': ['不存在结果栏'],
            '出现次数': [None],
            '占比率': [None]
        }))

    return pd.concat(result_list, ignore_index=True)
