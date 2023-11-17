import functools
import json
from collections.abc import Iterable
from pathlib import Path
from typing import Union

import numpy as np
import pandas as pd
import polars as pl
import polars.selectors as cs
import tqdm

PolarsFrame = Union[pl.LazyFrame, pl.DataFrame]

pd.options.mode.chained_assignment = None

BASE_PATH = Path(__file__).resolve().parents[0]
DAT_PATH = BASE_PATH / "data"

STATE_ABBREV_TO_FIPS = {
    "AL": "01",
    "AK": "02",
    "AZ": "04",
    "AR": "05",
    "CA": "06",
    "CO": "08",
    "CT": "09",
    "DE": "10",
    "DC": "11",
    "FL": "12",
    "GA": "13",
    "HI": "15",
    "ID": "16",
    "IL": "17",
    "IN": "18",
    "IA": "19",
    "KS": "20",
    "KY": "21",
    "LA": "22",
    "ME": "23",
    "MD": "24",
    "MA": "25",
    "MI": "26",
    "MN": "27",
    "MS": "28",
    "MO": "29",
    "MT": "30",
    "NE": "31",
    "NV": "32",
    "NH": "33",
    "NJ": "34",
    "NM": "35",
    "NY": "36",
    "NC": "37",
    "ND": "38",
    "OH": "39",
    "OK": "40",
    "OR": "41",
    "PA": "42",
    "RI": "44",
    "SC": "45",
    "SD": "46",
    "TN": "47",
    "TX": "48",
    "UT": "49",
    "VT": "50",
    "VA": "51",
    "WA": "53",
    "WV": "54",
    "WI": "55",
    "WY": "56",
    "AS": "60",
    "FM": "64",
    "GU": "66",
    "MH": "68",
    "MP": "69",
    "PW": "70",
    "PR": "72",
    "UM": "74",
    "VI": "78",
}

VALID_STATES = [
    "01",
    "02",
    "04",
    "05",
    "06",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "53",
    "54",
    "55",
    "56",
    "72",
]


# @functools.lru_cache()
# def get_house_number(address: str) -> Optional[str]:
#     res, _ = usaddress.tag(address)

#     return res.get("AddressNumber", None)


def replace_with_null(expr: pl.Expr, to_replace: Union[str, Iterable[str]]) -> pl.Expr:
    if isinstance(to_replace, str):
        to_replace = [to_replace]

    for pattern in to_replace:
        expr = pl.when(expr.str.count_matches(pattern) > 0).then(None).otherwise(expr)

    return expr.name.keep()


def apply_regex_mapping(expr: pl.Expr, mapper: dict[str, str]) -> pl.Expr:
    for k, v in mapper.items():
        expr = expr.str.replace_all(k, v)

    return expr


def reduce_whitespace(expr: pl.Expr) -> pl.Expr:
    """Strip trailing and leading whitespace and nromalize internal whitespace to one."""
    return expr.str.strip_chars().str.replace_all(" +", " ", literal=False)


@functools.lru_cache()
def split_on_number(string: str) -> tuple[str, str]:
    """In the original Zest code, if the house number is only numeric, it is assigned
    to the RIGHT column and the left column is the empty string.

    Parameters
    ----------
    string : str
        _description_

    Returns
    -------
    tuple[str, str]
        _description_
    """
    position = None
    for i, c in enumerate(string):
        if not c.isdigit():
            position = i + 1
            break

    if position is not None:
        return (string[:position], string[position:])
    else:
        return ("", string)


def clean_street_address(expr: pl.Expr) -> pl.Expr:
    return expr.str.replace_all("[^A-Za-z0-9']", " ").str.replace_all(
        "[^A-Za-z0-9\\s]", ""
    )


def replicate_house_number(pf: PolarsFrame, add_to_flg: int) -> PolarsFrame:
    original = pf.clone()

    pf = pf.with_columns(
        pl.col("replicate_flg")
        .cast(pl.Int64)
        .add(add_to_flg)
        .cast(pl.Utf8)
        .str.pad_start(6, "0"),
        pl.col("house_number").str.replace_all("[^0-9]", ""),
    )

    return pl.concat([original, pf], how="vertical").unique(
        subset=cs.all().exclude("replicate_flg"), keep="first"
    )


def replicate_address_2(
    pf: PolarsFrame,
    street_suffix_mapping: dict[str, str],
    add_to_flg: int,
    replicate_with_flg: bool,
) -> pl.DataFrame:
    original = pf.clone()

    if replicate_with_flg:
        pf = pf.with_columns(
            pl.col("replicate_flg")
            .cast(pl.Int64)
            .add(add_to_flg)
            .cast(pl.Utf8)
            .str.pad_start(6, "0")
        )

    pf = pf.with_columns(
        pl.col("street_address")
        .pipe(apply_regex_mapping, street_suffix_mapping)
        .map_dict({"nan": None}, default=pl.first())
        .str.split("-")
        .list.get(0)
        .str.replace_all("-", "", literal=True)
        .str.replace_all("^([0-9]{1,6}[A-Z]{1,3})", "")
        .str.replace_all("^([0-9]{1,3} [A-Z]{2})", "")
        .str.replace_all(" [0-9]{4,7} ", "")
    )

    return pl.concat([original, pf], how="vertical").unique(
        subset=cs.all().exclude("replicate_flg"), keep="first"
    )


def replicate_north_n(pf: PolarsFrame, add_to_flg: int, replicate_with_flg: bool):
    north_n_mapping = {
        "\\bNORTH\\b": "N",
        "\\bSOUTH\\b": "S",
        "\\bEAST\\b": "E",
        "\\bWEST\\b": "W",
        "\\bNORTHEAST\\b": "NE",
        "\\bNORTHWEST\\b": "NW",
        "\\bSOUTHEAST\\b": "SE",
        "\\bSOUTHWEST\\b": "SW",
        "\\bNORTE\\b": "N",
        "\\bSUR\\b": "S",
        "\\bESTE\\b": "E",
        "\\bOESTE\\b": "O",
        "\\bNORESTE\\b": "NE",
        "\\bNOROESTE\\b": "NO",
        "\\bSUDESTE\\b": "SE",
        "\\bSUDOESTE\\b": "SO",
    }

    original = pf.clone()

    pf = pf.with_columns(
        pl.col("street_address").pipe(apply_regex_mapping, north_n_mapping)
    )

    if replicate_with_flg:
        pf = pf.with_columns(
            pl.col("replicate_flg")
            .cast(pl.Int64)
            .add(add_to_flg)
            .cast(pl.Utf8)
            .str.pad_start(6, "0")
        )

    return pl.concat([original, pf], how="vertical").unique(
        subset=cs.all().exclude("replicate_flg"), keep="first"
    )


@functools.lru_cache()
def is_odd(s) -> int:
    """
    Checks if a number is odd.

    Parameters
    ----------
    s: string
        String with a number to be checked
    """
    try:
        return int(str(s)[-1]) % 2
    except Exception:
        return 0


def majority_vote_deduplication(data: pd.DataFrame, key: str):
    """
    When other deduplication methods fail we leave the most prevalent prediction

    Parameters
    ----------
    data: Dataframe
        Data to deduplicate
    key: string
        Key used in deduplication
    """
    data.sort_values(["NEW_SUPER_ZIP", "COUNTYFP", "TRACTCE", "TRACTCE", "BLKGRPCE"])
    data["TRACTCE"] = data.groupby(key)["TRACTCE"].transform(lambda x: x.mode()[0])
    data["BLKGRPCE"] = data.groupby(key)["BLKGRPCE"].transform(lambda x: x.mode()[0])
    data["NEW_SUPER_ZIP"] = data.groupby(key)["NEW_SUPER_ZIP"].transform(
        lambda x: x.mode()[0]
    )
    data["COUNTYFP"] = data.groupby(key)["COUNTYFP"].transform(lambda x: x.mode()[0])
    data = data.drop_duplicates(keep="first", subset=[key])

    return data


def _prepare_input_frame(
    pf: PolarsFrame,
    state_mapping: dict[str, str],
    street_suffix_mapping: dict[str, str],
    replicate: bool = True,
) -> pl.LazyFrame:
    pf = (
        # convert everything to strings and replace some with null
        pf.lazy()
        .cast(pl.Utf8)
        .with_columns(
            pl.col("*")
            .str.to_uppercase()
            .pipe(reduce_whitespace)
            .pipe(replace_with_null, ["^\\s*$", "^NAN$", "^NONE$"])
        )
        # remove the last character if it is not a number
        .with_columns(pl.col("house_number").str.replace("[^0-9]$", ""))
        # In the original Zest code, if the house number is only numeric, it is assigned
        # to the RIGHT column and the left column is the empty string.
        .with_columns(
            house_number_split=pl.col("house_number").map_elements(split_on_number)
        )
        .with_columns(
            house_number_LEFT=pl.col("house_number_split").list.get(0),
            house_number_RIGHT=pl.col("house_number_split").list.get(1),
        )
        .drop("house_number_split")
        .with_row_count("ZEST_KEY")
        .with_columns(pl.col("ZEST_KEY").cast(pl.Utf8))
        # Now that we have the split, strip the house number of all non-numeric
        .with_columns(pl.col("house_number").str.replace_all("[^0-9]", ""))
        # Clean street address
        .with_columns(pl.col("street_address").pipe(clean_street_address))
        # Clean state
        .with_columns(
            pl.col("state_abbrev")
            .str.replace_all("[^\\w\\s]", "")
            .map_dict(state_mapping, default=pl.first())
        )
        # Clean Zip Code
        .with_columns(
            pl.col("zip_code")
            .str.split("-")
            .list.get(0)
            .str.pad_start(5, "0")
            .str.slice(0, 5)
        )
        # Create replicate flag
        .with_columns(replicate_flg=pl.lit("000000"))
    )

    if replicate:
        pf = replicate_house_number(pf, add_to_flg=1)
        pf = replicate_address_2(
            pf, street_suffix_mapping, add_to_flg=10, replicate_with_flg=True
        )
        pf = replicate_north_n(pf, add_to_flg=100, replicate_with_flg=True)

    pf = pf.with_columns(
        pl.col("street_address").alias("ZEST_FULLNAME"),
        (pl.col("ZEST_KEY") + pl.col("replicate_flg")).alias("ZEST_KEY_LONG"),
    )

    return pf


def _geocode_state(
    lf: pl.LazyFrame, aef: pl.LazyFrame, replicate: bool = True
) -> pd.DataFrame:
    geo_df = (
        lf.join(aef, on="ZEST_FULLNAME", how="left")
        .with_columns(
            pl.col("FROMHN_RIGHT", "TOHN_RIGHT").fill_null(-2),
            pl.col("house_number_RIGHT").cast(pl.Int64).fill_null(-1),
        )
        .with_columns(
            HN_Match=pl.when(
                (pl.col("house_number_LEFT") == pl.col("FROMHN_LEFT"))
                & (pl.col("house_number_RIGHT") >= pl.col("FROMHN_RIGHT"))
                & (pl.col("house_number_RIGHT") <= pl.col("TOHN_RIGHT"))
            )
            .then(1)
            .otherwise(0)
        )
        .with_columns(
            Parity_Match=pl.when(
                pl.col("FROMHN_RIGHT").map_elements(is_odd)
                == pl.col("house_number_RIGHT").map_elements(is_odd)
            )
            .then(1)
            .otherwise(0)
        )
        .with_columns(
            pl.col("ZCTA5CE").map_dict({"None": None}, default=pl.first()),
        )
        .with_columns(
            NEW_SUPER_ZIP=pl.when(pl.col("ZCTA5CE") == pl.col("zip_code"))
            .then(pl.col("ZCTA5CE"))
            .otherwise(pl.col("ZEST_ZIP")),
        )
        .with_columns(
            ZIP_Match=pl.when(pl.col("NEW_SUPER_ZIP") == pl.col("zip_code"))
            .then(1)
            .otherwise(0)
        )
        .collect()
        .to_pandas()
    )

    all_keys = list(geo_df["ZEST_KEY_LONG"].unique())
    odf = geo_df.copy()

    geo_df = geo_df[geo_df.ZIP_Match == 1]
    zip_match_keys = list(geo_df["ZEST_KEY_LONG"].unique())
    no_zip_match_keys = list(set(all_keys) - set(zip_match_keys))

    df_zip_only = odf[odf["ZEST_KEY_LONG"].isin(no_zip_match_keys)]
    na_match_cols = [
        "BLKGRPCE",
        "COUNTYFP",
        "FROMHN",
        "TOHN",
        "TRACTCE",
        "ZCTA5CE",
        "ZCTA5CE10",
        "ZEST_FULLNAME",
        "ZEST_ZIP",
        "small",
        "big",
        "HN_Match",
        "Parity_Match",
        "ZIP_Match_1",
        "ZIP_Match_2",
        "NEW_SUPER_ZIP",
        "ZIP_Match",
        "FROMHN_numeric",
        "TOHN_numeric",
        "house_numer_numeric",
    ]
    df_zip_only[na_match_cols] = None

    df_zip_only = df_zip_only.drop_duplicates(subset=["ZEST_KEY_LONG"])

    # ZIP matched, HN not match
    all_keys = list(geo_df["ZEST_KEY_LONG"].unique())
    odf = geo_df.copy()

    geo_df = geo_df[geo_df["HN_Match"] == 1]
    HN_match_keys = list(geo_df["ZEST_KEY_LONG"].unique())
    no_HN_match_keys = list(set(all_keys) - set(HN_match_keys))

    df_no_HN = odf[odf["ZEST_KEY_LONG"].isin(no_HN_match_keys)]
    na_match_cols = ["BLKGRPCE", "FROMHN", "TOHN", "NEW_SUPER_ZIP", "ZIP_Match"]

    df_no_HN = majority_vote_deduplication(df_no_HN, "ZEST_KEY_LONG")
    df_no_HN[na_match_cols] = None

    # ZIP matched, HN matched, Parity not matched

    all_keys = list(geo_df["ZEST_KEY_LONG"].unique())
    odf = geo_df.copy()

    geo_df = geo_df[geo_df.Parity_Match == 1]
    parity_match_keys = list(geo_df["ZEST_KEY_LONG"].unique())
    no_parity_match_keys = list(set(all_keys) - set(parity_match_keys))

    df_no_parity = odf[odf["ZEST_KEY_LONG"].isin(no_parity_match_keys)]
    df_no_parity = majority_vote_deduplication(df_no_parity, "ZEST_KEY_LONG")

    # ZIP matched, HN matched, Parity matched
    df_parity = geo_df.copy()
    df_parity = majority_vote_deduplication(df_parity, "ZEST_KEY_LONG")

    # Merge all results
    geo_df_merged = pd.concat([df_zip_only, df_no_HN, df_no_parity, df_parity])

    # Create GEOIDs
    geo_df_merged["GEOID_CT"] = geo_df_merged[["STATEFP", "COUNTYFP", "TRACTCE"]].apply(
        lambda x: "".join(x.dropna()) if "".join(x.dropna()) != "" else None, axis=1
    )
    geo_df_merged["GEOID_CT"] = geo_df_merged["GEOID_CT"].apply(
        lambda x: x if x is None or len(x) == 11 else None
    )
    geo_df_merged["GEOID_BG"] = geo_df_merged[["GEOID_CT", "BLKGRPCE"]].apply(
        lambda x: "".join(x.dropna()) if "".join(x.dropna()) != "" else None, axis=1
    )
    geo_df_merged["GEOID_BG"] = geo_df_merged["GEOID_BG"].apply(
        lambda x: x if x is None or len(x) == 12 else None
    )
    geo_df_merged["GEOID_ZIP"] = np.where(
        geo_df_merged["ZCTA5CE"].notna(),
        geo_df_merged["ZCTA5CE"],
        geo_df_merged["zip_code"],
    )

    # Choose one entry from 'replicate_flg'
    if replicate:
        geo_df_no_duplicates = (
            geo_df_merged.sort_values(["ZEST_KEY_LONG"]).groupby("ZEST_KEY").first()
        )

    cols_to_drop = [
        "BLKGRPCE",
        "COUNTYFP",
        "FROMHN",
        "TOHN",
        "TRACTCE",
        "ZCTA5CE",
        "ZCTA5CE10",
        "ZEST_FULLNAME",
        "ZEST_ZIP",
        "ZEST_KEY_LONG",
        "replicate_flg",
        "FROMHN_LEFT",
        "FROMHN_RIGHT",
        "TOHN_LEFT",
        "TOHN_RIGHT",
        "HN_Match",
        "NEW_SUPER_ZIP",
        "PARITY",
        "Parity_Match",
        "STATEFP",
        "ZIP_Match",
    ]

    geo_df_no_duplicates = geo_df_no_duplicates.drop(columns=cols_to_drop)

    return geo_df_no_duplicates


def geocode(
    pf: PolarsFrame,
    replicate: bool = True,
    dat_path: Path = DAT_PATH,
) -> pd.DataFrame:
    """Needs the columns
        - state_abbrev
        - city
        - street_address
        - house_number
        - zip_code

    Parameters
    ----------
    df : Union[pl.LazyFrame, pl.DataFrame]
        _description_
    state_fips : str
        _description_
    replicate : bool, optional
        _description_, by default True

    Returns
    -------
    pd.DataFrame
        _description_
    """

    with open(dat_path / "processed/state_mapping.json") as f:
        state_mapping = json.load(f)

    with open(dat_path / "processed/street_suffix_mapping.json") as f:
        street_suffix_mapping = json.load(f)

    lf = _prepare_input_frame(
        pf,
        state_mapping=state_mapping,
        street_suffix_mapping=street_suffix_mapping,
        replicate=replicate,
    )

    states = lf.select("state_abbrev").unique().collect()["state_abbrev"]

    done = []
    for state in tqdm.tqdm(states):
        try:
            state_fips = STATE_ABBREV_TO_FIPS[state]
        except KeyError:
            continue

        aef = pl.scan_parquet(
            dat_path
            / f"processed/geo/2019/Zest_Geo_Lookup_2019_State_{state_fips}.parquet"
        )

        done.append(
            _geocode_state(
                lf.filter(pl.col("state_abbrev") == pl.lit(state)), aef, replicate
            )
        )

    return pd.concat(done, axis=0)
