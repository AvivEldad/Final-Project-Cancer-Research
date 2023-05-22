import pandas as pd
import oncosensepy as osp

if __name__ == '__main__':
    data_name = 'Table1_myData66'
    data_set_path = r'Data/' + data_name + '.xlsx'

    l_df, g_df = osp.get_LG_data(data_set_path)

    err_limit_lambda = pd.read_excel(data_set_path, sheet_name='ErrorLimitLambda').columns.values[0]

    important_l = osp.important_L(l_df, err_limit_lambda, 2, new_sheet=False, sheet_name='important_L',
                                  path=data_set_path)

    # filter_dosage = osp.filter_by_col(important_l, 'dosage', ['0.00001nm', '1nm', '40nm', '1uM'], new_sheet=False,
    #                                   sheet_name='important_L', path=data_set_path)
    #
    # filter_time = osp.filter_by_col(filter_dosage, 'time', ['0hr', '24hr'], new_sheet=False, sheet_name='important_L',
    #                                 path=data_set_path)
    #
    # important_g = osp.sort_G_values(g_df, important_l.columns[6:], save_plot_path='', save=False, new_sheet=False,
    #                                 sheet_name='Sorted_G', data_path=data_set_path)

    # Aviv - fix that function
    analyzed_pairs_dict = osp.analyze_pairs(important_l, ['MCF7', 'SKBR3-MCH'], fixed_col='time', p_value=0.05,
                                            only_avg=True, data_path=data_set_path)

    # Elchanan - continue from here
    # control_treatment_df = osp.analyze_control_treatment(important_l, 'MCF7')
    # osp.create_new_sheet(control_treatment_df, data_set_path, 'MCF7_control_vs_treatment')
