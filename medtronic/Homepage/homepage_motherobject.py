class HomepageMotherObject:

    @staticmethod
    def automation_project():
        return {
            'project_title': 'Automated_Project',
            'description': 'Automated_Project_desc',
            'operating_unit_id': 'Cardiovascular_CAS',
            'cost_center': 'cost',
            'data_sets': 'Cancer dataset',
        }

    @staticmethod
    def automation_workbench():
        return {
            'workbench_name': 'Automated_workbench',
            'workbench_description': 'Automated_Project_desc',
            'workbench_group': 'Non-GPU',
            'instance_type': 't2.micro tester',
        }

