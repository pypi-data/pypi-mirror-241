from urllib.request import urlretrieve

import pandas as pd
import rocks


from classy import cache
from classy import config
from classy import index
from classy import progress
from classy import sources
from classy import tools

BASE_URL = "http://smass.mit.edu/data"

REFERENCES = {
    "demeo2019": ["DeMeo+ 2019", "2019Icar..322...13D"],
    "polishook2014": ["Polishook+ 2014", "2014Icar..233....9P"],
}

DIR_URLS = [
    ("demeo2019", f"{BASE_URL}/minus/DeMeo2019_spectra.tar"),
    ("polishook2014", f"{BASE_URL}/minus/Spectra31AsteroidPairs_Polishook.zip"),
]

RUNS = (
    [f"sp{num:>02}" for num in range(1, 131)]
    + [f"sp{num:>02}" for num in range(200, 292)]
    + [f"dm{num:>02}" for num in range(1, 20)]
)

PATH = config.PATH_DATA / "mithneos/"

POLISHOOK_DATES = {
    "101703_IR.txt": "2013-10-03",
    "10484_Vis.txt": "2013-05-07",
    "10484_comb_IR.txt": "2011-11-27",
    "13732_IR.txt": "2014-01-07",
    "15107_IR.txt": "2013-01-17",
    "16815_IR.txt": "2013-09-28",
    "17198_comb_IR.txt": "2012-10-18",
    "17288_IR.txt": "2013-04-12",
    "1741_IR.txt": "2013-03-07",
    "19289_IR.txt": "2012-09-11",
    "1979_IR.txt": "2013-03-06",
    "1979_Vis.txt": "2013-05-07",
    "2110_comb_IR.txt": "2011-10-15",
    "25884_comb_IR.txt": "2011-10-25",
    "2897_IR.txt": "2013-03-07",
    "3749_Vis.txt": "2012-02-17",
    "3749_comb_IR.txt": "2012-01-22",
    "38707_IR.txt": "2013-05-12",
    "42946_IR.txt ": "2013-01-17",
    "44612_IR.txt": "2012-09-11",
    "4765_comb_IR.txt": "2013-01-10",
    "4905_IR.txt": "2013-08-08",
    "5026_IR.txt": "2012-04-21",
    "5026_Vis.txt": "2012-06-03",
    "52852_IR.txt": "2012-12-17",
    "54041_comb_IR.txt": "2012-12-14",
    "54827_IR.txt": "2012-08-08",
    "60546_IR.txt": "2013-02-10",
    "6070_IR.txt": "",
    "6070_Vis.txt": "2012-06-01",
    "63440_comb_IR.txt": "2021-11-09",
    "74096_IR.txt": "2013-10-13",
    "8306_IR.txt": "2013-09-07",
    "88604_IR.txt": "2013-06-12",
    "9068_IR.txt": "2013-07-11",
    "92652_IR.txt": "2013-03-06",
    "42946_IR.txt": "2013-01-17",
}

DATA_KWARGS = {
    "names": ["wave", "refl", "err", "flag"],
    "delimiter": r"\s+",
    "comment": "#",
}


def _transform_data(idx, data):
    """Apply module-specific data transforms."""

    # Logic cuts
    data = data[data.wave > 0]
    data = data[data.refl > 0]

    # 2 - reject. This is flag 0 in MITHNEOS
    data["flag"] = [0 if f != 0 else 2 for f in data["flag"].values]

    meta = {}
    return data, meta


def _retrieve_spectra():
    """Retrieve the MITHNEOS spectra from remote."""

    # Start with separate archives
    for dir, URL in DIR_URLS:
        (PATH / dir).mkdir(exist_ok=True, parents=True)
        tools.download_archive(
            URL, PATH / dir / URL.split("/")[-1], encoding=URL.split(".")[-1]
        )

    # -------
    # Scrape all mithneos runs from website and check for unpublished spectra

    with progress.mofn as mofn:
        task = mofn.add_task("MITHNEOS ObsRuns", total=len(RUNS))
        for run in RUNS:
            URL = f"{BASE_URL}/spex/{run}/"
            _download(URL, PATH / run)
            mofn.update(task, advance=1)


def _build_index():
    # Create index for these archives

    log = cache.load_cat("mithneos", "obslog")
    entries = []

    for dir, _ in DIR_URLS:
        for file_ in (PATH / dir).glob("**/*txt"):
            if "__MACOS" in str(file_):
                # garbage in archive file
                continue

            if file_.name.startswith("._"):
                # more garbage in archive file
                continue

            if dir == "demeo2019" and "fi" not in file_.name:
                # only add the fi06-fi11 runs here
                continue

            if dir == "polishook2014" and file_.name not in POLISHOOK_DATES:
                # do not index three-point visible spectra
                continue

            id_ = sources.smass.get_id_from_filename(file_)
            name, number = rocks.id(id_)

            date_obs = ""  # get's filled in below
            shortbib, bibcode = REFERENCES[dir]

            if dir == "demeo2019":
                try:
                    date_obs = log.loc[
                        (log.run == file_.name.split(".")[1]) & (log["name"] == name),
                        "date_obs",
                    ].values[0]
                except IndexError:
                    date_obs = ""
            elif dir == "polishook2014":
                if file_.name in POLISHOOK_DATES:
                    date_obs = POLISHOOK_DATES[file_.name]

            filename = str(file_).split("classy/")[-1]

            if pd.isna(date_obs):
                bibcode = ""

            entry = pd.DataFrame(
                data={
                    "name": name,
                    "number": number,
                    "filename": filename,
                    "shortbib": shortbib,
                    "bibcode": bibcode,
                    "date_obs": date_obs,
                    "host": "MITHNEOS",
                    "module": "mithneos",
                    "source": "MITHNEOS",
                },
                index=[0],
            )

            entries.append(entry)

    for run in RUNS:
        # check for duplicates
        for file_ in (PATH / run).glob("**/*txt"):
            if "162117-note" in file_.name or "p2010h2" in file_.name:
                continue

            id_ = sources.smass.get_id_from_filename(file_)
            if id_ is None:
                continue
            name, number = rocks.id(id_)

            if name is None:
                continue

            filename = str(file_).split("classy/")[-1]

            match = log.loc[(log.run == run) & (log["name"] == name)]

            if not match.empty:
                date_obs = match["date_obs"].values[0]
                shortbib = match["shortbib"].values[0]
                bibcode = match["bibcode"].values[0]
            else:
                date_obs = ""
                shortbib = "Unpublished"
                bibcode = "Unpublished"

            if not shortbib:
                shortbib = "Unpublished"
            if not bibcode:
                bibcode = "Unpublished"
            if pd.isna(shortbib):
                shortbib = "Unpublished"
            if pd.isna(bibcode):
                bibcode = "Unpublished"
            if pd.isna(date_obs):
                bibcode = ""

            entry = pd.DataFrame(
                data={
                    "name": name,
                    "number": number,
                    "filename": filename,
                    "shortbib": shortbib,
                    "bibcode": bibcode,
                    "date_obs": date_obs,
                    "source": "MITHNEOS",
                    "host": "mithneos",
                    "module": "mithneos",
                },
                index=[0],
            )
            entries.append(entry)

    entries = pd.concat(entries)
    index.add(entries)


def _download(URL, PATH_OUT):
    import bs4
    import requests

    r = requests.get(URL)

    if not r.ok:
        return

    data = bs4.BeautifulSoup(r.text, "html.parser")
    for l in data.find_all("a"):
        if l["href"].endswith("txt"):
            if "README" in l["href"]:
                continue
            if "READ_ME" in l["href"]:
                continue
            if "speclib-edit-backup" in l["href"]:
                continue

            PATH_OUT.mkdir(exist_ok=True, parents=True)
            urlretrieve(URL + l["href"], PATH_OUT / l["href"])
