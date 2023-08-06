import pandas as pd
import numpy as np
from datetime import datetime


"""
Format for loading the tracks data : 
track_id    time                lon     lat     hemisphere  basin   season  sshs    slp     wind10  year    month   day     (wind925)
str         np.datetime64[ns]   float   float   str         str     str     int     float   float   int     int     int     (float)

0 <= lon <= 360
"""


def load_ibtracs(file="data/ibtracs_1980-2020_simplified.csv"):
    """
    Parameters
    ----------
    file: Path to the ibtracs_simplified file

    Returns
    -------
    pd.DataFrame
        Columns as described in the module header
    """
    tracks = pd.read_csv(file, keep_default_na=False, dtype={"USA_SSHS": str})
    tracks["USA_SSHS"] = pd.to_numeric(tracks.USA_SSHS)
    tracks = (
        tracks[tracks.USA_SSHS >= 0]
        .rename(columns={col: col.lower() for col in tracks.columns})
        .rename(columns={"usa_sshs": "sshs", "sid": "track_id", "pres": "slp"})
        .drop(columns="season")
    )
    tracks["time"] = tracks.iso_time.astype(np.datetime64)
    tracks.loc[tracks.lon < 0, "lon"] += 360
    tracks["hemisphere"] = np.where(tracks.lat > 0, "N", "S")
    tracks["basin"] = tracks.basin.replace("EP", "ENP").replace("WP", "WNP")
    tracks = add_season(tracks)
    tracks["wind10"] = tracks.wind.astype(float)
    return tracks[
        [
            "track_id",
            "time",
            "lon",
            "lat",
            "hemisphere",
            "basin",
            "season",
            "sshs",
            "slp",
            "wind10",
            "year",
            "month",
            "day",
        ]
    ]


def load_TEtracks(
    file="tests/tracks_ERA5.csv",
    surf_wind_col="wind10",
    slp_col="slp",
):
    """
    Parameters
    ----------
    file (str): csv file from TempestExtremes StitchNodes output
    surf_wind_col (str): Name of the column with the surface wind to output.
    slp_col (str): Name of the column with the sea-level pressure. If None, no sshs computation.

    Returns
    -------
    pd.DataFrame
        Columns as described in the module header
    """
    tracks = pd.read_csv(file)
    tracks = tracks.rename(columns={c: c[1:] for c in tracks.columns[1:]})
    tracks.rename(columns={surf_wind_col: "wind10", slp_col: "slp"})

    tracks["time"] = get_time(tracks.year, tracks.month, tracks.day, tracks.hour)
    tracks.loc[tracks.lon < 0, "lon"] += 360
    tracks["hemisphere"] = np.where(tracks.lat > 0, "N", "S")
    tracks["basin"] = get_basin(
        tracks.hemisphere.values, tracks.lon.values, tracks.lat.values
    )
    tracks = add_season(tracks)
    tracks[slp_col] /= 100
    if slp_col != None:
        tracks["sshs"] = sshs_from_pres(tracks.slp.values)
    else:
        tracks["sshs"] = np.nan
    if "wind925" not in tracks.columns:
        tracks["wind925"] = np.nan
    return tracks[
        [
            "track_id",
            "time",
            "lon",
            "lat",
            "hemisphere",
            "basin",
            "season",
            "sshs",
            "slp",
            "wind10",
            "year",
            "month",
            "day",
            "wind925",
        ]
    ]


_TRACK_data_vars = [
    "vor_tracked",
    "lon1",
    "lat1",
    "vor850",
    "lon2",
    "lat2",
    "vor700",
    "lon3",
    "lat3",
    "vor600",
    "lon4",
    "lat4",
    "vor500",
    "lon5",
    "lat5",
    "vor400",
    "lon6",
    "lat6",
    "vor300",
    "lon7",
    "lat7",
    "vor200",
    "lon8",
    "lat8",
    "slp",
    "lon9",
    "lat9",
    "wind925",
    "lon10",
    "lat10",
    "wind10",
]


def load_TRACKtracks(
    file="tests/tr_trs_pos.2day_addT63vor_addmslp_add925wind_add10mwind.tcident.new",
    data_vars=_TRACK_data_vars,
):
    """
    Parameters
    ----------
    file (str): Path to the TRACK output file
    data_vars (list): list of the variables in the file

    Returns
    -------
    pd.DataFrame
        Columns as described in the module header
    """
    f = open(file)
    tracks = pd.DataFrame()
    line0 = f.readline()
    line1 = f.readline()
    line2 = f.readline()
    nb_tracks = int(line2.split()[1])
    c = 0
    track_id = 0
    time_step = []
    lon = []
    lat = []
    data = [[]]
    for line in f:
        if line.startswith("TRACK_ID"):
            data = pd.DataFrame(
                np.array(data), columns=data_vars[: np.shape(np.array(data))[1]]
            )
            tracks = tracks.append(
                ## <- This part is taking a long time. Idea: Replace with a list and transform into pandas in the end ?
                pd.DataFrame(
                    {
                        "track_id": [track_id] * len(time_step),
                        "time_step": time_step,
                        "lon": lon,
                        "lat": lat,
                    }
                ).join(data)
            )
            c += 1
            season = line.split()[-1][:-6]
            track_id = season + "-" + str(c)
            time_step = []
            lon = []
            lat = []
            data = []

        elif line.startswith("POINT_NUM"):
            pass
        else:
            time_step.append(line.split()[0])
            lon.append(float(line.split()[1]))
            lat.append(float(line.split()[2]))
            rest = line.split()[3:]
            mask = np.array(rest) == "&"
            data.append(np.array(rest)[~mask])

    f.close()
    SH = tracks.lat.mean() < 0
    tracks["year"] = tracks.time_step.str[:4].astype(int)
    tracks["month"] = tracks.time_step.str[-6:-4].astype(int)
    tracks["day"] = tracks.time_step.str[-4:-2].astype(int)
    tracks["hour"] = tracks.time_step.str[-2:].astype(int)
    if SH:
        tracks.loc[tracks.month <= 6, "year"] += 1
    tracks["time"] = get_time(tracks.year, tracks.month, tracks.day, tracks.hour)
    if SH:
        tracks["hemisphere"] = "S"
        tracks = add_season(tracks)
    else:
        tracks["hemisphere"] = "N"
        tracks = add_season(tracks)
    tracks["basin"] = get_basin(tracks.hemisphere, tracks.lon, tracks.lat)
    tracks["slp"] = tracks.slp.astype(float)
    tracks["sshs"] = sshs_from_pres(tracks.slp)
    if "wind10" not in tracks.columns:
        tracks["wind10"] = np.nan
    else:
        tracks["wind10"] = tracks.wind10.astype(float)
    if "wind925" not in tracks.columns:
        tracks["wind925"] = np.nan
    else:
        tracks["wind925"] = tracks.wind925.astype(float)
    return tracks[
        [
            "track_id",
            "time",
            "lon",
            "lat",
            "hemisphere",
            "basin",
            "season",
            "sshs",
            "slp",
            "wind10",
            "year",
            "month",
            "day",
            "wind925",
        ]
    ]


def get_time(year, month, day, hour):
    time = (
        year.astype(str)
        + "-"
        + month.astype(str)
        + "-"
        + day.astype(str)
        + " "
        + hour.astype(str)
        + ":00"
    ).astype(np.datetime64)
    return time


def sshs_from_wind(wind):
    sshs = np.where(wind <= 60 / 3.6, -1, None)
    sshs = np.where((sshs == None) & (wind < 120 / 3.6), 0, sshs)
    sshs = np.where((sshs == None) & (wind < 150 / 3.6), 1, sshs)
    sshs = np.where((sshs == None) & (wind < 180 / 3.6), 2, sshs)
    sshs = np.where((sshs == None) & (wind < 210 / 3.6), 3, sshs)
    sshs = np.where((sshs == None) & (wind < 240 / 3.6), 4, sshs)
    sshs = np.where((sshs == None) & (~np.isnan(wind)), 5, sshs)
    sshs = np.where(sshs == None, np.nan, sshs)
    return sshs


def sshs_from_pres(p):
    sshs = np.where(p > 990, -1, None)
    sshs = np.where((sshs == None) & (p >= 980), 0, sshs)
    sshs = np.where((sshs == None) & (p >= 970), 1, sshs)
    sshs = np.where((sshs == None) & (p >= 965), 2, sshs)
    sshs = np.where((sshs == None) & (p >= 945), 3, sshs)
    sshs = np.where((sshs == None) & (p >= 920), 4, sshs)
    sshs = np.where((sshs == None) & (~np.isnan(p)), 5, sshs)
    sshs = np.where(sshs == None, np.nan, sshs)
    return sshs


def get_basin(hemisphere, lon, lat):
    basin = np.where((hemisphere == "N") & (lon > 40) & (lon <= 100), "NI", "")
    basin = np.where(
        (hemisphere == "N")
        & (lon > 100)
        & ((lon <= 200) | ((lat >= 35) & (lon <= 250))),
        "WNP",
        basin,
    )
    basin = np.where(
        (hemisphere == "N")
        & (basin != "WNP")
        & (lon > 200)
        & ((lon <= 260) | ((lat <= 15) & (lon <= 290))),
        "ENP",
        basin,
    )
    basin = np.where((hemisphere == "N") & (basin != "ENP") & (lon > 260), "NA", basin)
    basin = np.where((hemisphere == "S") & (lon > 20) & (lon <= 130), "SI", basin)
    basin = np.where((hemisphere == "S") & (lon > 130) & (lon <= 300), "SP", basin)
    basin = np.where((hemisphere == "S") & (basin == ""), "SA", basin)
    return basin


def add_season(tracks):
    if "season" in tracks.columns:
        tracks = tracks.drop(columns="season")
    group = (
        tracks.groupby(["track_id"])[["year", "month"]]
        .mean()
        .astype(int)
        .join(
            tracks[["track_id", "hemisphere"]].drop_duplicates().set_index("track_id"),
            on="track_id",
        )
    )
    hemi, yr, mth = group.hemisphere.values, group.year.values, group.month.values
    season = np.where(hemi == "N", yr, None)
    season = np.where((hemi == "S") & (mth >= 7), yr, season)
    season = np.where((hemi == "S") & (mth <= 6), yr - 1, season)
    _ = np.where(
        (hemi == "S"),
        np.core.defchararray.add(season.astype(str), np.array(["-"] * len(season))),
        season,
    ).astype(str)
    season = np.where(
        (hemi == "S"), np.core.defchararray.add(_, (season + 1).astype(str)), season
    )

    group["season"] = season.astype(str)
    tracks = tracks.join(group[["season"]], on="track_id")
    return tracks


def to_dt(t):
    ts = np.floor((t - np.datetime64("1970-01-01T00:00:00")) / np.timedelta64(1, "s"))
    return np.array(
        [datetime.utcfromtimestamp(t) if not np.isnan(t) else np.nan for t in ts]
    )


# Supprimer ?
def find_match(tc_detected, tracks_ref, mindays=1, maxd=4):
    """

    Parameters
    ----------
    id_detected
    tracks_detected
    tracks_ref
    mindays
    maxd

    Returns
    -------

    """
    candidates = tracks_ref[
        (tracks_ref.time >= tc_detected.time.min())
        & (tracks_ref.time <= tc_detected.time.max())
    ].track_id.unique()
    if len(candidates) < 1:
        return pd.DataFrame({"id_ref": [np.nan], "dist": [np.nan], "temp": [np.nan]})
    matches = pd.DataFrame()
    for candidate in candidates:
        tc_candidate = tracks_ref[(tracks_ref.track_id == candidate)][
            ["lon", "lat", "time"]
        ]
        merged = pd.merge(tc_detected, tc_candidate, on="time")
        dist = np.mean(
            merged.apply(
                lambda row: np.sqrt(
                    (row.lon_x - row.lon_y) ** 2 + (row.lat_x - row.lat_y) ** 2
                ),
                axis=1,
            )
        )  # Compute distance
        temp = len(merged)
        matches = matches.append(
            pd.DataFrame({"id_ref": [candidate], "dist": [dist], "temp": [temp]})
        )
    matches = matches[matches.temp >= mindays * 4]
    matches = matches[matches.dist <= maxd]
    if len(matches) < 1:
        return pd.DataFrame({"id_ref": [np.nan], "dist": [np.nan], "temp": [np.nan]})
    return matches[matches.dist == matches.dist.min()]


def match_tracks(tracks1, tracks2, name1="algo", name2="ib", maxd=8, mindays=1):
    """

    Parameters
    ----------
    tracks1 (pd.DataFrame): First tracks DataFrame
    tracks2 (pd.DataFrame): Second tracks DataFrame
    name1 (str): name to append corresponding to the first df
    name2 (str): name to append corresponding to the second df
    maxd (numeric): Maximum allowed distance between two tracks
    mindays (int): Minimum number of days in common between two tracks

    Returns
    -------
    pd.DataFrame
        with the track ids of the matching trajectories in tracks1 and tracks2
    """
    tracks1, tracks2 = (
        tracks1[["track_id", "lon", "lat", "time"]],
        tracks2[["track_id", "lon", "lat", "time"]],
    )
    merged = pd.merge(tracks1, tracks2, on="time")
    merged["dist"] = merged.apply(
        lambda row: np.sqrt(
            (row.lon_x - row.lon_y) ** 2 + (row.lat_x - row.lat_y) ** 2
        ),
        axis=1,
    )
    dist = merged.groupby(["track_id_x", "track_id_y"])[["dist"]].mean()
    temp = (
        merged.groupby(["track_id_x", "track_id_y"])[["dist"]]
        .count()
        .rename(columns={"dist": "temp"})
    )
    matches = dist.join(temp)
    matches = matches[(matches.dist < maxd) & (matches.temp > mindays * 4)]
    matches = (
        matches.loc[matches.groupby("track_id_x")["dist"].idxmin()]
        .reset_index()
        .rename(columns={"track_id_x": "id_" + name1, "track_id_y": "id_" + name2})
    )
    return matches


if __name__ == "__main__":
    # t = load_TRACKtracks()
    pass
