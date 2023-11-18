import json
import logging
import os

from unify.apimanager import ApiManager

logger = logging.getLogger(__name__)


def list_dataset_ids(api_manager, org_id):
    ds_listing_resp = api_manager.dataset_list(org_id, page_num=1, page_size=10000)
    return [d['uuid'] for d in ds_listing_resp]


def list_dataset_names(api_manager, org_id):
    ds_listing_resp = api_manager.dataset_list(org_id)
    return set([d['name'] for d in ds_listing_resp])


def write_to_file(file_path, artifact_id, ds_content, content_type):
    try:
        with open(file_path, 'w') as f:
            json.dump(ds_content, f)
        print(f"Data for {content_type} {artifact_id} written to {file_path}")
    except Exception as e:
        print(f"An error occurred while writing to {file_path}: {e}")
        if os.path.exists(file_path):
            os.remove(file_path)


def write_file(file_path, file_content):
    try:
        with open(file_path, 'w') as f:
            f.write(file_content)
        print(f"Wrote file: {file_path}")
    except Exception as e:
        print(f"An error occurred while writing to {file_path}: {e}")
        if os.path.exists(file_path):
            os.remove(file_path)


def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name


def export_all_data(api_manager: ApiManager, base_dir: str, org_id: int):
    datasets_dir_name = os.path.join(base_dir, 'datasets')
    pipelines_dir_name = os.path.join(base_dir, 'pipelines')
    datasets_directory = create_directory(datasets_dir_name)
    pipelines_directory = create_directory(pipelines_dir_name)

    export_all_datasets(api_manager, datasets_directory, org_id)
    export_all_templates(api_manager, base_dir, org_id)
    export_all_pipelines(api_manager, pipelines_directory, org_id)


def export_all_templates(api_manager, base_dir, org_id):
    template_content = api_manager.templates.download_template_batches(org_id=org_id)
    template_file_path = os.path.join(base_dir, f"templates.csv")
    print(f'Exporting templates to ${template_file_path}')
    write_file(template_file_path, template_content)


def export_all_datasets(api_manager, datasets_directory, org_id):
    dataset_ids = list_dataset_ids(api_manager, org_id)
    for ds_id in dataset_ids:
        ds_file_path = os.path.join(datasets_directory, f"{ds_id}.json")
        if not os.path.exists(ds_file_path):
            ds_content = api_manager.export_source(org_id=org_id, dataset_ids=[ds_id])
            write_to_file(ds_file_path, ds_id, ds_content, 'dataset')
        else:
            print(f'Dataset {ds_file_path} already retrieved')


def export_all_pipelines(api_manager: ApiManager, pipeline_dir: str, org_id: int):
    pipelines = api_manager.pipeline_list(org_id, page_num=1, page_size=10000)

    for p in pipelines:
        pipeline_id = p['id']['id']
        pipeline_name = p['name']
        pipeline_file_path = os.path.join(pipeline_dir, f"{pipeline_name}_{pipeline_id}.json")
        if not os.path.exists(pipeline_file_path):
            print(f'Extracting pipeline "{pipeline_name}", ID: {pipeline_id}')
            pipeline_export_content = api_manager.create_pipelines_export_data(org_id=org_id,
                                                                               pipeline_ids=[pipeline_id],
                                                                               skip=[])
            write_to_file(pipeline_file_path, pipeline_id, pipeline_export_content, 'pipeline')
        else:
            print(f'Pipeline {pipeline_file_path} already retrieved')


# Run these CLI and cluster setup commands before executing the data takeout script.
# pip install --upgrade unify-cli
# unify cluster add --remote "https://app.elementanalytics.com/" --username "myuser@my_org.com" --name "cluster_ref" --password "SECRET" --assetsync True
# unify cluster login --remote cluster_ref

if __name__ == '__main__':
    # Use this main for debugging only.
    # The utility is available via the CLI by invoking as follows:
    # unify wf data-takeout --remote cluster_ref --org 1
    cluster_id = 'cluster_ref'
    source_org_id = 1

    home_directory = os.path.expanduser('~')
    base_directory = os.path.join(home_directory, 'unify_takeout', cluster_id, str(source_org_id))
    create_directory(base_directory)

    try:
        apiManager = ApiManager(cluster=cluster_id)
        export_all_data(apiManager, base_directory, source_org_id)
    except Exception as e:
        logging.exception("An error occurred")
