from tkinter import messagebox

import numpy as np
import pandas as pd


def count_result(df, input_filename):
    result_list = []

    if '测试结果' in df.columns:

        total_count = df['测试结果'].size
        total_non_nan_count = df['测试结果'].count()

        df['测试结果'] = df['测试结果'].replace('', np.nan)

        value_counts = df['测试结果'].dropna().value_counts()

        percentages = value_counts / total_count * 100

        nan_count = df['测试结果'].isna().sum()

        if not total_count == nan_count + total_non_nan_count:
            messagebox.showinfo("提示", "这份表格统计列数据有问题，请人工查看: " + str(input_filename))

        if nan_count > 0:
            nan_row_indices = df[df['测试结果'].isna()].index.tolist()
            nan_series = pd.Series({'NaN': [nan_count, nan_row_indices]})

            value_counts = pd.concat([value_counts, nan_series], axis=0)

            percentages = percentages._append(pd.Series({'NaN': (nan_count / total_count) * 100}))

            value_counts = value_counts.reindex(value_counts.index.tolist() + ['NaN'] if 'NaN' not in value_counts.index else value_counts.index)
            percentages = percentages.reindex(percentages.index.tolist() + ['NaN'] if 'NaN' not in percentages.index else percentages.index)
            print(f"表【{input_filename}】包含NaN的行索引为: {nan_row_indices}")

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
