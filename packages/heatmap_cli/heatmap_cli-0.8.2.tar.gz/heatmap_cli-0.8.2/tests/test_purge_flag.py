# pylint: disable=C0114,C0116

import pytest


@pytest.mark.parametrize("option", ["-p", "--purge"])
def test_debug_logs(cli_runner, csv_file, option):
    csv = csv_file("sample.csv")
    ret = cli_runner(csv, "-d", option)
    assert "purge=True" in ret.stderr


@pytest.mark.skip(reason="TODO")
def test_purge_output_folder_if_exists(cli_runner, csv_file):
    csv = csv_file("sample.csv")
    output_folder = csv.resolve().parent.joinpath("output")
    output_folder.mkdir(parents=True, exist_ok=True)
    ret = cli_runner(csv, "-d", "-p", "-y")
    assert f"Purge output folder: {output_folder}" in ret.stderr


@pytest.mark.skip(reason="TODO")
def test_prompt_for_purging(cli_runner, csv_file):
    csv = csv_file("sample.csv")
    output_folder = csv.resolve().parent.joinpath("output")
    ret = cli_runner(csv, "-d", "-p")
    assert (
        f"Are you sure to purge output folder: {output_folder}? [y/N] "
        in ret.stderr
    )


def test_no_purge_output_folder_if_not_exists(cli_runner, csv_file):
    csv = csv_file("sample.csv")
    output_folder = csv.resolve().parent.joinpath("output")
    ret = cli_runner(csv, "-d", "-p")
    assert f"Purge output folder: {output_folder}" not in ret.stderr
