import os
import sys

from typing import Tuple

from bigeye_cli.functions import cli_client_factory
from bigeye_cli import global_options
from bigeye_sdk.controller.lineage_controller import LineageController
from bigeye_sdk.functions.delta_functions import infer_column_mappings
from bigeye_sdk.functions.table_functions import fully_qualified_table_to_elements
from bigeye_sdk.model.delta_facade import (
    SimpleDeltaConfigurationFile,
    SimpleDeltaConfiguration,
    SimpleTargetTableComparison,
)

from typing import Optional, List

import typer

from bigeye_cli.model.cicd_conf import SimpleDeltaCicdConfigFile
from bigeye_sdk.log import get_logger
from bigeye_cli.model.vendor_report import VendorReport
from bigeye_sdk.model.protobuf_message_facade import (
    SimpleColumnMapping,
    SimpleNamedSchedule,
)

log = get_logger(__file__)

app = typer.Typer(no_args_is_help=True, help="Deltas Commands for Bigeye CLI")


@app.command()
def suggest_deltas(
    bigeye_conf: str = global_options.bigeye_conf,
    config_file: str = global_options.config_file,
    workspace: str = global_options.workspace,
    source_warehouse_id: int = typer.Option(
        None, "--source_warehouse_id", "-swid", help="Source Warehouse ID"
    ),
    target_warehouse_id: int = typer.Option(
        None, "--target_warehouse_id", "-twid", help="Source Warehouse ID"
    ),
    source_warehouse_name: str = typer.Option(
        None, "--source_warehouse_name", "-swn", help="Source Warehouse Name"
    ),
    target_warehouse_name: str = typer.Option(
        None, "--target_warehouse_name", "-twn", help="Source Warehouse Name"
    ),
    fq_schema_name_pairs: Optional[List[str]] = typer.Option(
        None,
        "--schema_name_pair",
        "-snp",
        help="Fully qualified schema name pairs.  e.g. -snp source_schema_1:target_schema_1 "
        "-snp source_warehouse.source_schema:target_warehouse.target_schema",
    ),
    output_path: str = typer.Option(
        ...,
        "--output_path",
        "-op",
        help="File to write the delta configuration.",
    ),
    update_lineage: bool = typer.Option(
        False,
        "--update_lineage",
        "-ul",
        help="Should lineage between source and target be checked/created if doesn't exist.",
    ),
):
    """Suggests and creates Deltas with default behavior and outputs all Simple Delta Configurations to a file."""

    client = cli_client_factory(bigeye_conf, config_file, workspace)

    if source_warehouse_name and target_warehouse_name:
        log.info(
            f"Creating deltas between warehouse: {source_warehouse_name} and warehouse ID {target_warehouse_name}"
        )
        r = client.suggest_deltas(
            warehouse_name_pairs=[(source_warehouse_name, target_warehouse_name)]
        )

    elif source_warehouse_id and target_warehouse_id:
        log.info(
            f"Creating deltas between warehouse ID: {source_warehouse_id} and warehouse ID {target_warehouse_id}"
        )
        r = client.suggest_deltas(
            warehouse_id_pairs=[(source_warehouse_id, target_warehouse_id)]
        )

    elif fq_schema_name_pairs:
        schema_name_pairs: List[Tuple[str, str]] = [
            tuple[str, str](p.split(":")) for p in fq_schema_name_pairs
        ]
        log.info(f"Creating deltas between: {schema_name_pairs}.")
        r = client.suggest_deltas(fq_schema_name_pairs=schema_name_pairs)
    else:
        sys.exit(
            "Identify one of the following: warehouse ids: warehouse ids and schema name pairs; "
            "or table id pairs."
        )

    r.save(output_path=output_path, default_file_name="delta_config")
    typer.echo(output_path)

    if update_lineage:
        lineage_controller = LineageController(client=client)
        lineage_controller.create_relations_from_delta_configuration(r.deltas)

    raise typer.Exit()


@app.command()
def create_delta(
    bigeye_conf: str = global_options.bigeye_conf,
    config_file: str = global_options.config_file,
    workspace: str = global_options.workspace,
    delta_conf_file: str = typer.Option(
        ..., "--delta_conf", "-dc", help="Simple Delta configuration file."
    ),
    update_lineage: bool = typer.Option(
        False,
        "--update_lineage",
        "-ul",
        help="Should lineage between source and target be checked/created if doesn't exist.",
    ),
):
    """Creates deltas between tables from a Simple Delta configuration file that contains multiple delta configurations.
    Enforces 1:1 column comparisons by case-insensitive column names if no column mappings are declared in
    configuration."""

    client = cli_client_factory(bigeye_conf, config_file, workspace)
    sdc = SimpleDeltaConfigurationFile.load(delta_conf_file)
    comparison_table_configurations = client.create_deltas_from_simple_conf(
        sdcl=sdc.deltas
    )

    if update_lineage:
        lineage_controller = LineageController(client=client)
        lineage_controller.create_relations_from_delta_configuration(
            comparison_table_configurations
        )

    raise typer.Exit()


@app.command()
def run_delta(
    bigeye_conf: str = global_options.bigeye_conf,
    config_file: str = global_options.config_file,
    workspace: str = global_options.workspace,
    delta_id: int = typer.Option(..., "--delta_id", "-did", help="Id of delta."),
):
    """Runs a delta by Delta ID."""
    print("Running a Delta now ... ")
    client = cli_client_factory(bigeye_conf, config_file, workspace)
    client.run_a_delta(delta_id=delta_id)


@app.command()
def create_template(
    bigeye_conf: str = global_options.bigeye_conf,
    config_file: str = global_options.config_file,
    workspace: str = global_options.workspace,
    fully_qualified_source_name: str = typer.Option(
        ...,
        "--source_table_name",
        "-stn",
        help="The fully qualified name of the source table",
    ),
    fully_qualified_target_name: List[str] = typer.Option(
        ...,
        "--target_table_name",
        "-ttn",
        help="The fully qualified name of the target table",
    ),
    output_path: str = typer.Option(
        ...,
        "--output_path",
        "-op",
        help="Path to write the template.",
    ),
):
    """Create a template delta configuration file based on table names."""
    if len(fully_qualified_target_name) > 2:
        sys.exit("Specify 1 target table for a standard delta or 2 for n-way delta.")

    client = cli_client_factory(bigeye_conf, config_file, workspace)

    swh, fq_source_schema, source_table = fully_qualified_table_to_elements(
        fully_qualified_source_name
    )
    source = client.get_tables(
        schema=[fq_source_schema], table_name=[source_table]
    ).tables[0]

    source_metrics_types = client.get_delta_applicable_metric_types(
        table_id=source.id
    ).metric_types

    comparisons = []

    for tn in fully_qualified_target_name:
        twh, fq_target_schema, target_table = fully_qualified_table_to_elements(tn)
        target = client.get_tables(
            schema=[fq_target_schema], table_name=[target_table]
        ).tables[0]
        target_metric_types = client.get_delta_applicable_metric_types(
            table_id=target.id
        ).metric_types
        column_mappings = infer_column_mappings(
            source_metric_types=source_metrics_types,
            target_metric_types=target_metric_types,
        )
        simple_mappings = [
            SimpleColumnMapping.from_datawatch_object(obj=cm) for cm in column_mappings
        ]

        comparisons.append(
            SimpleTargetTableComparison(
                fq_target_table_name=tn,
                delta_column_mapping=simple_mappings,
                source_filters=[],
                target_filters=[],
                group_bys=[],
            ).dict()
        )


    configuration = SimpleDeltaConfiguration(
            delta_name=f"{fully_qualified_source_name} <> {fully_qualified_target_name}",
            fq_source_table_name=fully_qualified_source_name,
            target_table_comparisons=comparisons,
            tolerance=0.0,
            notification_channels=[],
            cron_schedule=SimpleNamedSchedule(
                name="Enter schedule name",
                cron="Define cron, if schedule does not exist. Otherwise just specify name.",
            ),
        )

    template = SimpleDeltaConfigurationFile(
            type="DELTA_CONFIGURATION_FILE", deltas=[configuration]
    )

    template.save(output_path=output_path, default_file_name="delta_template")
    typer.echo(f"File written at {output_path}delta_template.yml")

    raise typer.Exit()


@app.command()
def cicd(
    bigeye_conf: str = global_options.bigeye_conf,
    config_file: str = global_options.config_file,
    workspace: str = global_options.workspace,
    delta_cicd_config: str = typer.Option(
        ...,
        "--delta_cicd_config",
        "-dcc",
        help="The yaml file containing the parameters for the DeltaCICDConfig class",
    ),
):
    """Creates a delta based on SimpleDeltaConfiguration and integrates the results with the provided VCS vendor."""
    client = cli_client_factory(bigeye_conf, config_file, workspace)

    delta_cicd = SimpleDeltaCicdConfigFile.load(file_name=delta_cicd_config).cicd_conf
    vendor_report: VendorReport = delta_cicd.report_type.value(
        github_token=os.environ["GITHUB_TOKEN"]
    )

    swh, fq_source_schema, source_table = fully_qualified_table_to_elements(
        delta_cicd.fq_source_table_name
    )
    twh, fq_target_schema, target_table = fully_qualified_table_to_elements(
        delta_cicd.fq_target_table_name
    )

    log.info("Beginning CICD delta process...")

    source = client.get_tables(
        schema=[fq_source_schema], table_name=[source_table]
    ).tables[0]
    target = client.get_tables(
        schema=[fq_target_schema], table_name=[target_table]
    ).tables[0]

    log.info("Looking for existing Delta with same name.")
    client.delete_deltas_by_name(delta_names=[delta_cicd.delta_name])

    response = client.create_delta(
        name=delta_cicd.delta_name, source_table_id=source.id, target_table_id=target.id
    )
    delta_id = response.comparison_table_configuration.id
    client.run_a_delta(delta_id=delta_id)

    # TODO: add polling logic for larger tables.
    delta_run = client.get_delta_information(delta_ids=[delta_id])
    exit_code = vendor_report.publish(
        delta_cicd.fq_source_table_name, delta_cicd.fq_target_table_name, delta_run[0]
    )

    if exit_code != 0 and delta_cicd.group_bys:
        log.info("Alerts detected. Running new delta with specified groups.")
        group_by_columns = delta_cicd.group_bys[0].source_column_name
        group_by_name = f"{delta_cicd.delta_name} -- GROUPED BY {group_by_columns}"
        client.delete_deltas_by_name(delta_names=[group_by_name])
        group_bys = [gbc.to_datawatch_object() for gbc in delta_cicd.group_bys]
        gb_response = client.create_delta(
            name=group_by_name,
            source_table_id=source.id,
            target_table_id=target.id,
            group_bys=group_bys,
        )

        client.run_a_delta(delta_id=gb_response.comparison_table_configuration.id)
        delta_gb_run = client.get_delta_information(
            delta_ids=[gb_response.comparison_table_configuration.id]
        )[0]

        if delta_gb_run.alerting_metric_count != 0:
            vendor_report.publish_group_bys(
                delta_cicd.fq_source_table_name,
                delta_cicd.fq_target_table_name,
                delta_gb_run,
            )

    sys.exit(exit_code)
