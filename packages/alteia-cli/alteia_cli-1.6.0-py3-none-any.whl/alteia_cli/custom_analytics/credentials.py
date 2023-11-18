import json
from enum import Enum
from pathlib import Path
from typing import Dict, List, cast

import typer
from alteia.core.errors import ResponseError
from alteia.core.resources.resource import Resource, ResourcesWithTotal
from tabulate import tabulate

from alteia_cli import AppDesc, utils
from alteia_cli.color_manager import UniqueColor
from alteia_cli.sdk import alteia_sdk

app = typer.Typer()
app_desc = AppDesc(
    app, name="credentials", help="Interact with Docker registry credentials."
)


class CredentialsType(str, Enum):
    docker = "docker"
    object_storage = "object-storage"
    stac_catalog = "stac-catalog"


class ObjectStorageType(str, Enum):
    s3 = "s3"
    azure_blob = "azure-blob"


@app.command(name="create")
def create(
    filepath: Path = typer.Option(
        ...,  # '...' in typer.Option() makes the option required
        exists=True,
        readable=True,
        help="Path of the Credential JSON file.",
    ),
    company: str = typer.Option(default=None, help="Company identifier."),
):
    """
    Create a new credential entry.
    """

    sdk = alteia_sdk()
    credentials_list = json.load(open(filepath))
    if not isinstance(credentials_list, list):
        credentials_list = [credentials_list]
    for cred in credentials_list:
        if not company and not cred.get("company", None):
            typer.secho(
                "✖ Cannot create a credential entry with the name {!r}. "
                "You have to define a company".format(cred.get("name")),
                fg=typer.colors.RED,
            )
            raise typer.Exit(2)
        elif company and not cred.get("company", None):
            cred["company"] = company

        found_cred = cast(
            ResourcesWithTotal,
            sdk.credentials.search(
                filter={
                    "name": {"$eq": cred.get("name")},
                    "company": {"$eq": cred.get("company")},
                },
                return_total=True,
            ),
        )
        if found_cred.total >= 1:
            typer.secho(
                "✖ Cannot create a credential entry with the name {!r}. "
                "One already exists on {}".format(
                    cred.get("name"), sdk._connection._base_url
                ),
                fg=typer.colors.RED,
            )
            raise typer.Exit(2)

        try:
            created_cred = sdk.credentials.create(
                name=cred["name"],
                credentials=cred["credentials"],
                company=cred["company"],
            )
            typer.secho("✓ Credentials created successfully", fg=typer.colors.GREEN)
            return created_cred
        except Exception as ex:
            print("Impossible to save {} with error {}".format(cred["name"], ex))
            raise typer.Exit(code=1)


@app.command(name="list")
def list_credentials(
    company: str = typer.Option(
        default=None,
        help="Company identifier.",
    ),
    type: CredentialsType = typer.Option(
        default=CredentialsType.docker.value, help="Type of credentials"
    ),
):
    """
    List the existing credentials.
    """
    sdk = alteia_sdk()
    credential_type = type
    list_filter = {"type": {"$eq": credential_type.value}}

    unique_color_company = UniqueColor()
    if company:
        list_filter.update({"company": {"$eq": company}})
    with utils.spinner():
        credentials: List[Resource] = sdk.credentials.search(filter=list_filter)  # type: ignore
    if len(credentials) > 0:
        table: Dict[str, List[str]] = init_credential_list_table(credential_type)

        for credential in credentials:
            table["Credentials name"].append(
                utils.green_bold(getattr(credential, "name"))
            )

            fill_table_by_credential_type(table, credential, credential_type)

            company_desc = utils.describe_company(sdk, getattr(credential, "company"))
            if company_desc:
                company_name = company_desc.name
                short_name = getattr(company_desc, "short_name", "")
            else:
                company_name = getattr(credential, "company")
                short_name = ""

            color_company = unique_color_company.get_colored(company_name)
            table["Company"].append(typer.style(company_name, fg=color_company, bold=True))
            table["Company shortname"].append(typer.style(short_name, fg=color_company, bold=True))

        typer.secho(
            tabulate(table, headers="keys", tablefmt="pretty", colalign=["left"])
        )
    else:
        typer.secho("No credentials founds", fg=typer.colors.YELLOW)
    print()


@app.command(name="delete")
def delete_credentials(name: str = typer.Argument(...)):
    """
    Delete a credential entry by its name.
    """
    sdk = alteia_sdk()
    found_cred = cast(
        ResourcesWithTotal,
        sdk.credentials.search(
            filter={
                "name": {"$eq": name},
            },
            return_total=True,
        ),
    )
    if found_cred.total < 1:
        typer.secho(
            "✖ Credential {!r} not found on {!r}".format(
                name, sdk._connection._base_url
            ),
            fg=typer.colors.RED,
        )
        raise typer.Exit(2)

    try:
        sdk.credentials.delete(
            found_cred.results[0].id, company=found_cred.results[0].company
        )
    except ResponseError as e:
        typer.secho(
            "✖ Cannot delete the credentials {!r}".format(name), fg=typer.colors.RED
        )
        typer.secho("details: {}".format(str(e)), fg=typer.colors.RED)
        raise typer.Exit(2)

    typer.secho(
        "✓ Credentials {!r} deleted successfully".format(name), fg=typer.colors.GREEN
    )


def init_credential_list_table(
    credential_type: CredentialsType,
) -> Dict[str, List[str]]:
    table: Dict[str, List[str]] = {
        "Credentials name": [],
        "Company": [],
        "Company shortname": [],
    }

    if credential_type == CredentialsType.docker:
        table["Registry"] = []

    if credential_type == CredentialsType.object_storage:
        table["URI"] = []

    if credential_type == CredentialsType.stac_catalog:
        table["Catalog"] = []

    return table


def fill_table_by_credential_type(
    table: Dict[str, List[str]], credential: Resource, credential_type: CredentialsType
):
    if credential_type == CredentialsType.docker:
        table["Registry"].append(get_credential_colour_field(credential, "registry"))
    if credential_type == CredentialsType.object_storage:
        if (
            getattr(credential, "credentials", {}).get("type", "")
            == ObjectStorageType.s3
        ):
            table["URI"].append(get_credential_colour_field(credential, "bucket"))
        else:
            table["URI"].append(get_credential_colour_field(credential, "account_url"))
    if credential_type == CredentialsType.stac_catalog:
        table["Catalog"].append(get_credential_colour_field(credential, "catalog"))


def get_credential_colour_field(credential: Resource, field: str) -> str:
    return utils.green_bold(getattr(credential, "credentials", {}).get(field, ""))


if __name__ == "__main__":
    app()
