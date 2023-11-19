import click
import keyring
import requests

baseURL = "https://api.cloudimate.tech/api/"

headers = {
    "X-User-Email": keyring.get_password("cloudimate", "email"),
    "X-Region": keyring.get_password("cloudimate", "region"),
    "Authorization": f"Bearer {keyring.get_password('cloudimate', 'api_key')}",
}


@click.group()
def cm():
    """Cloudimate CLI tool"""
    pass


@cm.command()
@click.argument("resource_type")
@click.argument("template_name")
def provision(resource_type, template_name):
    """Provision a resource with a given template."""
    if resource_type == "environment":
        response = requests.post(baseURL(f"/aws/createEnvironmentStructure"), headers=headers, json={"template_name": template_name})
        if response.status_code == 200:
            click.echo("")
        else:
            click.echo("Failed to provision environment")
            click.echo(f"HTTP Error: {response.status_code}")


@cm.command()
@click.argument("command")
def explain(command):
    """Explains what a command does in more detail. Use \'cm explain [command]\'"""
    switcher = {
        "provision": "provision (method) + [template type] environment or fleet + [template name] ",
        "set": "set (method) + [information type] credentials \n  credentials: enter your email, api key, and default region. Your credentials should match the credentials used to set up your Cloudimate account",
        "get": "get (method) + [information type] template type or credentials + [template name] (optional) ",
        "list": "list (method) + [command] or [command parameter] like TemplateTypes ",
        "test": "test (method) + [command parameter] connection",
    }
    click.echo(
        f"\nExplain [{command}]:\n"
        + switcher.get(command, f"Couldn't find command '{command}'")
    )


@cm.command()
@click.argument("target")
@click.argument("arg")
def set(target, arg):
    """Sets information"""
    if target == "credentials":
        email = input("Enter your email: ").replace(" ", "")
        api_key = input("Enter your API key: ").replace(" ", "")
        region = input("Enter your region: ").replace(" ", "")
        keyring.set_password("cloudimate", "email", email)
        keyring.set_password("cloudimate", "api_key", api_key)
        keyring.set_password("cloudimate", "region", region)
        click.echo(
            f"Credentials set successfully.\n  email: '{email}'\n  api key: '{api_key}'\n  region: '{region}'"
        )

    if target == "arn":
        response = requests.post(
            baseURL(f"/updateAwsCredentials"), headers=headers, json={"arn": arg}
        )
        if response.status_code == 200:
            click.echo("Cloudimate account ARN set successfully")
        else:
            click.echo("Failed to retrieve templates")
            click.echo(f"HTTP Error: {response.status_code}")


@cm.command()
@click.argument("target")
def get(target):
    """Retrieves information such as credentials and templates"""

    if target == "credentials":
        email = keyring.get_password("cloudimate", "email")
        region = keyring.get_password("cloudimate", "region")
        click.echo(
            f"Credentials retrieved successfully.\n  email: '{email}'\n  api key: '{api_key}'\n  region: '{region}'"
        )

    elif target in [
        "FleetTemplates",
        "CronTemplates",
        "EnvironmentTemplates",
        "RDSTemplates",
        "EC2Templates",
    ]:
        response = requests.get(baseURL(f"/get{target}"), headers=headers)
        if response.status_code == 200:
            try:
                templates = response.json()
                click.echo("Templates:\n")
                for template in templates:
                    click.echo(
                        f"  Template: {template['template_name']}\n  Description: {template['description']}\n\n"
                    )
            except requests.exceptions.JSONDecodeError:
                click.echo("Failed to parse response as JSON.")
        else:
            click.echo("Failed to retrieve templates")
            click.echo(f"HTTP Error: {response.status_code}")
    else:
        click.echo(f"No parameters found for '{target}'")


@cm.command()
@click.argument("target")
@click.argument("template_name")
def delete(target, template_name):
    """Deletes templates"""

    if target in [
        "FleetTemplate",
        "CronTemplate",
        "EnvironmentTemplate",
        "RDSTemplate",
        "EC2Template",
    ]:
        response = requests.delete(baseURL(f"/delete{target}/{template_name}"), headers=headers)
        if response.status_code == 200:
           click.echo(f"Deletion of template \'{template_name}\' was successful")
        else:
            click.echo("Failed to retrieve templates")
            click.echo(f"HTTP Error: {response.status_code}")
    else:
        click.echo(f"No parameters found for '{target}'")

@cm.command()
@click.argument("target")
def test(target):
    """Tests things such as connection to Cloudimate"""

    if target == "connection":
        response = requests.get(baseURL(f"/aws/testConnection"), headers=headers)
        if response.status_code == 200:
            click.echo("Connection test was successful")
        else:
            click.echo(f"HTTP Error: {response.status_code}")
    else:
        click.echo(f"No parameters found for '{target}'")


@cm.command()
@click.argument("thing")
def list(thing):
    """Used for getting information on command parameters within the CLI application"""
    if thing == "TemplateTypes":
        click.echo(
            f"template types:\n  FleetTemplates\n CronTemplates\n EnvironmentTemplates\n EC2Templates\n  RDSTemplates\n"
        )


def baseURL(url):
    return "https://api.cloudimate.tech/api" + url


if __name__ == "__main__":
    cm()

    