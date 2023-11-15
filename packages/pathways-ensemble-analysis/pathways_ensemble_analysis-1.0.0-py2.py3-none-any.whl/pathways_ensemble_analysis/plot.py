import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import logging
from typing import Dict, List, Optional
from pandas_indexing import assignlevel

logger = logging.getLogger(__name__)


def heatmap(
    matrix: pd.DataFrame,
    not_rated_matrix: Optional[pd.DataFrame] = None,
    figsize: Optional[tuple] = None,
    gridspec_kw: Optional[Dict[str, List[float]]] = None,
) -> plt.axes:
    """Displays heatmap of evaluated criteria

    Parameters
    ----------
    matrix : pd.DataFrame
        DataFrame with evaluated critera: index - criteria; columns - pathways
    not_rated_matrix : pd.DataFrame, optional
        DataFrame with evaluated but not rated critera: index - criteria; columns - pathways
    figsize : tuple, optional
        Figure size passed to plt.subplots
    gridspec_kw : Dict[str, List[float]], optional
        gridspec_kw, as a default used for specifying horizontal and vertical axes' ratios

    Returns
    -------
    plt.axes
        Axes of the plot
    """
    # Preprocess matrix
    sorted_matrix = matrix.copy()
    sorted_matrix = sorted_matrix.loc[
        :, sorted_matrix.sum().sort_values(ascending=False).index
    ]

    total = pd.DataFrame(sorted_matrix.sum(), columns=[r"$\bf{Total}$"]).T

    # Plot figure
    rows = 2 if not_rated_matrix is None else 4

    criteria = matrix.index
    nb_criteria = len(criteria)
    len_criteria_max = max([len(s) for s in criteria])

    pathways = matrix.columns
    nb_pathways = len(pathways)
    len_pathways_max = max([len(" ".join(s)) for s in pathways])

    if not_rated_matrix is None:
        if not figsize:
            figsize = (
                1 + len_criteria_max / 10 + nb_pathways / 4,
                len_pathways_max / 10 + nb_criteria / 3,
            )

        if not gridspec_kw:
            gridspec_kw = {
                "height_ratios": [nb_criteria, 1],
                "width_ratios": [nb_pathways, 1],
            }
    else:
        nr_criteria = not_rated_matrix.index
        nb_nr_criteria = len(nr_criteria)
        len_nr_criteria_max = max([len(s) for s in nr_criteria])

        if not figsize:
            figsize = (
                1 + max(len_criteria_max, len_nr_criteria_max) / 10 + nb_pathways / 4,
                len_pathways_max / 10 + nb_criteria / 3 + nb_nr_criteria / 3,
            )

        if not gridspec_kw:
            gridspec_kw = {
                "height_ratios": [nb_criteria, 1, 1, nb_nr_criteria],
                "width_ratios": [nb_pathways, 1],
            }

    fig, ax = plt.subplots(rows, 2, figsize=figsize, gridspec_kw=gridspec_kw)

    # Plot evaluation matrix
    im = ax[0][0].imshow(sorted_matrix, aspect="auto", cmap="viridis_r")

    ax[0][0].xaxis.tick_top()

    ax[0][0].set_xticks(np.arange(len(sorted_matrix.columns)))
    ax[0][0].set_yticks(np.arange(len(sorted_matrix.index)))

    xticklabels = [" ".join(c) for c in sorted_matrix.columns]
    ax[0][0].set_xticklabels(xticklabels, rotation=90)
    ax[0][0].set_yticklabels(sorted_matrix.index)

    cbar = plt.colorbar(im, cax=ax[0][1])
    cbar.ax.set_ylabel("Values", rotation=-90, va="bottom")

    # Plot total rating
    im = ax[1][0].imshow(total, aspect="auto", cmap="viridis_r")
    ax[1][0].get_xaxis().set_visible(False)

    ax[1][0].set_yticks(np.arange(len(total.index)))
    ax[1][0].set_yticklabels(total.index)

    cbar = plt.colorbar(im, cax=ax[1][1])

    # If provided, plot not rated criteria
    if not_rated_matrix is not None:
        ax[2][0].text(0, 0, "Not ranked criteria", ha="left", va="bottom")
        ax[2][0].axis("off"), ax[2][1].axis("off")

        not_rated_matrix = not_rated_matrix[sorted_matrix.columns]

        im = ax[3][0].imshow(not_rated_matrix, aspect="auto", cmap="viridis_r")

        ax[3][0].get_xaxis().set_visible(False)
        ax[3][0].set_yticks(np.arange(len(not_rated_matrix.index)))
        ax[3][0].set_yticklabels(not_rated_matrix.index)

        cbar = plt.colorbar(im, cax=ax[3][1])

    fig.tight_layout()
    fig.subplots_adjust(hspace=0.1)

    return ax


def compare_ensembles(
    value_matrices: Dict[str, pd.DataFrame],
    criterion: str,
    ax: plt.axes = None,
    legend: Optional[bool] = True,
    **plot_kwargs: Optional[Dict],
) -> plt.axes:
    """Displays boxplot of a given criterion for a set of value_matrices

    Parameters
    ----------
    value_matrices : dict[str, pd.DataFrame]
        A dictionary where the keys are the names of each value_matrix (user defined),
        and the values are value matrices of the form: index - criterion; columns - pathways
        this allows value matrices for different pathway ensembles to be compared against one another
    criterion: str
        String which identifies which of the criteria in the value matrix to plot
    legend:
        Boolean argument which allows a legend to be added or not
    plot_kwargs : dict, optional
        Set of kwargs which is passed to sns.boxplot for plotting control

    Returns
    -------
    plt.axes
        Axes of the plot

    """
    if not ax:
        ax = plt.gca()

    plot_df = pd.concat(
        [
            assignlevel(value_matrix.loc[criterion], filter_set=filter_set)
            for (filter_set, value_matrix) in value_matrices.items()
        ]
    )

    sns.boxplot(
        data=plot_df.reset_index().drop(["model", "scenario"], axis=1),
        y=criterion,
        x="filter_set",
        ax=ax,
        **plot_kwargs,
    )
    ax.set_xlabel("")
    ax.set_ylabel("Criterion value", fontsize="small")
    ax.tick_params(axis="both", which="major", labelsize="small")
    ax.set_title(criterion, fontsize="medium")

    if legend is True:
        hdls = []
        for count, key in enumerate(value_matrices.keys()):
            h = ax.plot([0], [0], "-", color=sns.color_palette()[count], label=key)
            hdls.append(h[0])
        legend_labels = [
            f"{key} (n = {value_matrix.loc[criterion].dropna().shape[0]})"
            for (key, value_matrix) in value_matrices.items()
        ]
        ax.legend(hdls, legend_labels, fontsize="x-small")

    return ax


def polar_chart(
        matrix: pd.DataFrame,
        yticks: list,
        yticklabels: list,
        figsize: Optional[tuple] = None,  
        color_dict: Optional[Dict[str, str]] = None,
    ):
    """Creates a polar chart which displays the values and a boxplot for each criterion 

    Parameters
    ----------
    matrix : pd.DataFrame
        DataFrame with evaluated critera: index - criteria; columns - pathways
    yticks : list
        yticks for inner radii
    yticklabels : list
        yticklabels for inner radii
    figsize : Optional[tuple], optional
        Figure size passed to plt.subplots, by default None
    color_dict : Optional[Dict[str, str]], optional
        Color dict assigning a color to each criterion, by default None

    Returns
    -------
    _type_
        _description_
    """

    x = matrix.index
    nb_criteria = len(x)
    theta = [2 * np.pi * i / nb_criteria for i in range(nb_criteria)]

    mask = ~np.isnan(matrix)
    y = [d[m] for d, m in zip(matrix.values, mask.values)]

    fig, ax = plt.subplots(figsize=figsize, subplot_kw={"projection": "polar"})

    for (ix, row), angle in zip(matrix.iterrows(), theta):
        color = "grey" if color_dict is None else color_dict[ix]
        ax.plot(
            [angle for i in range(matrix.shape[1])],
            row.values,
            marker=".",
            linestyle="None",
            color=color,
        )

    ax.boxplot(y, positions=theta, showfliers=False, showcaps=False, whis=0, widths=0.1)

    ax.set_xticklabels(matrix.index)
    ax.set_yticks(yticks)
    ax.set_yticklabels(
        yticklabels,
        fontsize="medium",
        va="center",
        ha="left",
    )
    ax.tick_params(axis="y", which="major", labelsize="small")

    labels = []
    for label, angle in zip(ax.get_xticklabels(), np.rad2deg(theta)):
        x, y = label.get_position()
        if 90 < angle < 270:
            ha = "right"
        elif angle == 90 or angle == 270:
            ha = "center"
        else:
            ha = "left"
        lab = ax.text(
            x, y, label.get_text(), transform=label.get_transform(), ha=ha, va="center"
        )
        labels.append(lab)
    ax.set_xticklabels([])

    pos = ax.get_rlabel_position()
    ax.set_rlabel_position(pos + np.diff(np.rad2deg(theta))[0] / 2)

    return fig, ax    