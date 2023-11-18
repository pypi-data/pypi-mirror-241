import os
import yaml
import typer

app = typer.Typer()

class InfrastructureService:
    def __init__(self):
        pass

    def _create_queue(self, name: str, type: str, stub_filename: str):
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Determine the appropriate stub file based on the 'type' and 'dlq' arguments
        stub_file_path = os.path.join(script_dir, "..", "stubs", "infrastructure", stub_filename)

        if not os.path.exists(stub_file_path):
            raise FileNotFoundError(f"Stub file not found: {stub_file_path}")

        with open(stub_file_path, "r") as stub_file:
            stub_content = stub_file.read()

        # Replace "{{name}}" placeholder with the provided 'name' parameter
        stub_content = stub_content.replace("{{name}}", name)

        # Load the content of the existing 'serverless.yml' file
        serverless_file_path = os.path.join(os.getcwd(), 'serverless.yml')

        if not os.path.exists(serverless_file_path):
            raise FileNotFoundError(f"serverless.yml not found in the current working directory")

        with open(serverless_file_path, "r") as serverless_file:
            serverless_content = serverless_file.read()

        # Parse the content of 'serverless.yml' as a dictionary
        serverless_dict = yaml.safe_load(serverless_content)

        # Ensure 'resources' key exists in 'serverless_dict'
        if 'resources' not in serverless_dict:
            serverless_dict['resources'] = {}

        # Check if 'Resources' key is None or empty
        if not serverless_dict['resources'].get('Resources'):
            serverless_dict['resources']['Resources'] = {}

        # Check if the resource with the same 'name' already exists
        if name in serverless_dict['resources']['Resources']:
            print(f"Updating existing resource '{name}'")
            # Update the properties of the existing resource
            existing_resource = serverless_dict['resources']['Resources'][name]
            new_resource = yaml.safe_load(stub_content)
            existing_resource.update(new_resource)
        else:
            print(f"Inserting new resource '{name}'")
            # Insert the resource from the specific stub dictionary
            serverless_dict['resources']['Resources'][name] = yaml.safe_load(stub_content)

        # Save the updated dictionary back to 'serverless.yml'
        with open('serverless.yml', 'w') as serverless_file:
            yaml.dump(serverless_dict, serverless_file, default_style='', default_flow_style=False, sort_keys=False)

        print(f"Updated 'serverless.yml' for '{name}'")

    def create_sqs_queue(self, queue_type: str = 'sqs', name: str ='', type: str = 'standard', dlq: bool = False):
        if queue_type == 'sqs':
            if dlq:
                stub_filename = "standard_with_dlq.stub" if type.lower() == "standard" else "fifo_with_dlq.stub"
            else:
                stub_filename = "standard_sqs.stub" if type.lower() == "standard" else "fifo_sqs.stub"
        else:
            stub_filename = "standard_dlq.stub" if type.lower() == "standard" else "fifo_dlq.stub"


        self._create_queue(name, type, stub_filename)
