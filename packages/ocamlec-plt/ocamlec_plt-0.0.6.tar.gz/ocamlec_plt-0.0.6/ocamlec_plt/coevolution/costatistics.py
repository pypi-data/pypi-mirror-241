#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:59:46 2023

@author: mariohevia
"""

import ocamlec_plt.utils as utils
import seaborn as sns
import pandas as pd

    



def _get_game_alg_benchmark(filepath):
    """
    Reads the data from filepath and returns it ready to plot.

    Returns
    -------
    pd.DataFrame

    """
    df_benchmarks = utils.ocamlFileToPandas(filepath)
    all_games = df_benchmarks["game_id"].unique()
    all_algs = df_benchmarks["alg_id"].unique()
    all_algs.sort()
    lst_benchmarks = [df_benchmarks[df_benchmarks["game_id"] == g] for g in all_games]
    return all_games, all_algs, lst_benchmarks

def plot_game_alg_benchmark(input_path, output_path="", height=4.8, width=6.4, ext=".pdf", log_scale=True, **kwargs):
    """
    Plots results from "print_game_alg_benchmark" statistic.

    Parameters
    ----------
    input_path : str
        Path to file.
    output_path : str, optional
        Path to directory where the plots will be saved. The default is the
        current directory.
    height : float, optional
        Height of the figure. The default is 4.8.
    width : float, optional
        Width of the figure. The default is 6.4.
    ext : str, optional
        Extension of the output files. The default is ".pdf".
    log_scale : bool, optional
        If True it log-scales the y axis. The default is True.
    **kwargs : key, value mappings
        Other keyword arguments are passed through to seaborn.boxplot().

    Returns
    -------
    None.

    """
    games, algs, dfs = _get_game_alg_benchmark(input_path)
    for i, df in enumerate(dfs):
        ax = sns.boxplot(data=df, x="alg_id", y="t", order=algs, **kwargs)
        ax.set_facecolor("#e6e6e6")
        ax.set_xlabel("Algorithms")
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(), rotation=45, ha='right')
        ax.set_title(games[i])
        if log_scale:
            ax.set_yscale('log')
        fig = ax.get_figure()
        fig.set_figheight(height)
        fig.set_figwidth(width)
        fig.savefig(output_path+games[i]+ext, bbox_inches = 'tight')
        fig.clf()
    # output_files = [output_path+g+ext for g, _ in processed_stat__data]

    
class payoff_stats(utils.stat):
    
    def __init__(self):
        super().__init__()
        
    def plot_one_run_in_ax(self, ax, stat_type):
        if stat_type=="median":
            return ax # TODO
        elif stat_type=="mean":
            return ax # TODO
        else:
            raise ValueError("Unrecognized string "+stat_type+" in stat_type")
        
    def plot_several_runs_in_ax(self, ax_pred, ax_prey, pred_stat, prey_stat, stat_type, **kwargs):
        """
        pred_stat is generally "pred_" + "q1", "median", "q3", "max", "min", "mean" or "std_dev"
        prey_stat is generally "prey_" + "q1", "median", "q3", "max", "min", "mean" or "std_dev"
        """
        # TODO: stat_type not used
        if stat_type not in ["median", "mean"]:
            raise ValueError("Unrecognized string "+stat_type+" in stat_type")
        ax_pred = sns.lineplot(ax=ax_pred, data=self._stat__data, x="t", y=pred_stat, legend='full', **kwargs)
        ax_pred = sns.lineplot(ax=ax_prey, data=self._stat__data, x="t", y=prey_stat, legend='full',  **kwargs)
        return ax_pred, ax_prey
    

class compare_champions(utils.stat):
    """
    The compare_champions class is used to plot the champions comparison.
    """
    
    def __init__(self):
        super().__init__()
    
    def __plotAxChampions(self, ax, alg, ts, median, q1, q3):
        """
        Plots the data into one axis from a single algorithm/pop from a Champions experiment.
        Used by plotChampions and plotChampionsVSCommon
        """
        ax.plot(ts, median, label=alg)
        ax.fill_between(ts, q1, q3, hatch= '//', alpha = 0.3)
        return ax
    
    def __getChampions(self, legend_key=None):
        """
        Gives the data ready to plot from a single Champions experiment.
        Used by plotChampions and plotChampionsVSCommon
        """
        ts = self._stat__data['t'].unique().tolist()
        data_names = ['min', 'q1', 'median', 'q3', 'max', 'mean']
        data_dict = {'ts':ts}
        for coea in ['coea1', 'coea2']:
            for pop in ['pred', 'prey']:
                for name in data_names:
                    key = coea+'_'+pop+'_'+name
                    data_dict[key] = [self._stat__data[self._stat__data['t'] == i].loc[:, key].median() for i in ts]
        # TODO: Decide whether or not to use this
        if legend_key!=None:
            alg_1 = self._stat__data["coea1:"+legend_key].unique().tolist()[0]
            alg_2 = self._stat__data["coea2:"+legend_key].unique().tolist()[0]
        else:
            alg_1, alg_2 = "coea1", "coea2"
        return alg_1, alg_2, data_dict
    
    def plot_several_runs_in_ax(self, ax_pred, ax_prey, pred_stat, prey_stat, stat_type, legends=(None,None), **kwargs):
        # TODO: stat_type not used
        if stat_type not in ["median", "mean"]:
            raise ValueError("Unrecognized string "+stat_type+" in stat_type")
        if pred_stat not in ["q1", "median", "q3", "max", "min", "mean", "std_dev"]:
            raise ValueError("Unrecognized string "+pred_stat+" in pred_stat")
        if prey_stat not in ["q1", "median", "q3", "max", "min", "mean", "std_dev"]:
            raise ValueError("Unrecognized string "+prey_stat+" in prey_stat")
        alg_1, alg_2, data_dict = self.__getChampions()
        if legends!=(None,None):
            alg_1 = legends[0]
            alg_2 = legends[1]
        
        ax_pred = self.__plotAxChampions(ax_pred, alg_1, data_dict['ts'], data_dict['coea1_pred_median'],
                                         data_dict['coea1_pred_q1'], data_dict['coea1_pred_q3'])
        ax_pred = self.__plotAxChampions(ax_pred, alg_2, data_dict['ts'], data_dict['coea2_pred_median'],
                                         data_dict['coea2_pred_q1'], data_dict['coea2_pred_q3'])
        
        ax_prey = self.__plotAxChampions(ax_prey, alg_1, data_dict['ts'], data_dict['coea1_prey_median'],
                                         data_dict['coea1_prey_q1'], data_dict['coea1_prey_q3'])
        ax_prey = self.__plotAxChampions(ax_prey, alg_2, data_dict['ts'], data_dict['coea2_prey_median'],
                                         data_dict['coea2_prey_q1'], data_dict['coea2_prey_q3'])
        return ax_pred, ax_prey