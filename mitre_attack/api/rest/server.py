from flask import Flask
from mitre_attack.data.matrices.enterprise import MitreAttackEnterprise

import mitre_attack.cli.click as click
import logging
import flask


logger = logging.getLogger(__name__)

app = Flask(__name__)
api = MitreAttackEnterprise()


@app.route('/tactics')
def tactics():
    response = list(api.iter_tactics())
    return flask.jsonify(response)


@app.route('/techniques')
def techniques():
    response = list(api.iter_techniques())
    return flask.jsonify(response)


@app.route('/groups')
def groups():
    response = list(api.iter_groups())
    return flask.jsonify(response)


@app.route('/software')
def software():
    response = list(api.iter_software())
    return flask.jsonify(response)


@app.route('/malware')
def malware():
    response = list(api.iter_malware_families())
    return flask.jsonify(response)


@app.route('/tools')
def tools():
    response = list(api.iter_tools())
    return flask.jsonify(response)


@app.route('/mitigations')
def mitigations():
    response = list(api.iter_mitigations())
    return flask.jsonify(response)


@app.route('/relationships')
def relationships():
    response = list(api.iter_relationships())
    return flask.jsonify(response)


@click.command()
def cli():
    app.run()


if __name__ == "__main__":
    cli()
