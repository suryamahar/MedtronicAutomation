from src.utils.action_helper import ActionHelper


class HomepageMotherObject:

    @staticmethod
    def automation_project():
        random_number = str(ActionHelper.generate_random_number())
        return {
            'project_title': 'Automated_Project' + random_number,
            'description': 'Automated_Project_desc',
            'operating_unit_id': 'Cardiovascular_CAS',
            'cost_center': 'cost',
            'data_sets': 'Cancer dataset',
        }

    @staticmethod
    def automation_workbench():
        random_number = str(ActionHelper.generate_random_number())
        return {
            'workbench_name': 'Automated_workbench'+random_number,
            'workbench_description': 'Automated_Project_desc'+random_number,
            'workbench_group': 'Non-GPU',
            'instance_type': 't2.micro tester',
        }
